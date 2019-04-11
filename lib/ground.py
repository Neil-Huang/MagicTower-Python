from pygame import Surface
import pygame
from pygame.transform import scale
from pygame.sprite import Group
from sprite import EventSprite
from sysconf import *
from lib.utools import *

"""
    ground 概念说明：
    1. 画布：属于surface功能，相当于一个画板
    2. 可重定位：提供给父画布坐标转换的功能
    3. 树形结构：ground之间为树形关系，游戏全屏幕screen为根ground
    4. 访问协议：子ground从规则上不能操作父ground的属性，可以访问父的操作
    5. 坐标转换：为子类提供逻辑坐标到绝对坐标的转换，逻辑坐标系统需要自己继承了写
    6. 精灵显示：每个ground的内部存在一个SpriteGroup，根据层级在draw的时候顺序更新

    类比： 一个多层多房间的操场？

    需要改进：同级碰撞检测 并自适应调整、

"""

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)

from os import path
import copy
from sprite import EventSprite

from pygame import Rect

"""
pygame.init()
pygame.mixer.init()

# 获取敌人图像：
enemies_full_black_original = pygame.image.load("img/enemys.png")
enemy_image = crop_images(enemies_full_black_original, 200, Rect(0, 0, 64, 32))

#

img_dir = "img"
wall_original = pygame.image.load(path.join(img_dir, "wall.png"))
static_element = {'1': wall_original}

clock = pygame.time.Clock()
clock.tick(100)
"""


#  基本绘制区域
#  x, y, w, h
#  如果需要逻辑坐标 继承该类 实现trans_locate函数（逻辑转物理）
class GroundSurface:
    def __init__(self, *args):
        """
        *0 自动生成屏幕画布
        *1 Surface
        *2 (w, h)
        *4(5) x,y,w,h,(scale放大率-暂时没用)
        :param args:
        """
        L = len(args)
        scale = 1.0
        if L == 0:
            surface = pygame.display.set_mode((WIDTH, HEIGHT))
            self.rect = surface.get_rect()
        elif L == 1:
            surface = args[0]
            self.rect = surface.get_rect()
        elif L == 2:
            surface = Surface(args)
            self.rect = surface.get_rect()
        elif L >= 4:
            surface = Surface(args[2:4])
            rect = surface.get_rect()
            rect.left = args[0]
            rect.top = args[1]
            if L > 4:
                scale = args[4]
            self.rect = rect
        else:
            surface = Surface()
            print("error ground surface")
            self.rect = surface.get_rect()
        self.w = self.rect.w
        self.h = self.rect.h
        self.surface = surface
        self.scale = scale
        self.parent = None
        self.layer = 0
        self.children = []
        self.group = Group()
        # 当前画布占用情况 无记忆 不考虑缝隙等复杂情况 指定的是一个“可绘制矩形范围”
        self.curpos = {"left": 0, "top": 0,
                       "right": 0,
                       "bottom": 0,
                       "mid": 0}

    # 增加子画布 这类画布可以是别的独立画布 也可以给出参数创建
    def add_child(self, *args):
        if len(args) == 1:
            # 插入别的画布到自适应的左上角 这样做由于对齐问题只能插一行 并且导致自适应混乱 多行需要手动重定位curpos
            ground_surface = args[0]
            rect = ground_surface.rect
            rect.left = self.curpos['left']
            rect.top = self.curpos['top']
            self.curpos['left'] += rect.w
        elif len(args) == 2:  # 自适应画布 贴边或者定在中心 第一个指定类型 第二个指定大小
            ground_surface = self.create_addaptive_surface(*args)
        elif len(args) == 3:  # 插入别的画布到指定坐标 无视碰撞
            ground_surface = args[0]
            ground_surface.rect.left = args[1]
            ground_surface.rect.top = args[2]
        else:  # 用Ground方式创建画布
            ground_surface = GroundSurface(*args)

        ground_surface.layer = self.layer + 1
        ground_surface.parent = self
        ground_surface.scale *= self.scale
        self.children.append(ground_surface)

        return ground_surface

    # 自适应矩形
    def create_addaptive_surface(self, type, value):
        if type not in self.curpos:
            print("error type of ground")
            return
        w = self.rect.w
        h = self.rect.h
        t = self.curpos["top"]
        r = self.curpos["right"]
        l = self.curpos["left"]
        b = self.curpos["bottom"]
        op = {"left": Rect(l, t, value, h - t - b),
              "top": Rect(l, t, w - l - r, value),
              "right": Rect(w - value - r, t, value, h - t - b),
              "bottom": Rect(l, h - value - b, w - l - r, value),
              "mid": Rect(max(l, int((w - value) / 2)),
                          max(r, int((h - value) / 2)),
                          min(w - l - r, value), min(h - t - b, value))
              }
        rect = op[type]
        # print(rect)
        # print(rect.w)
        # print(rect.h)
        ground_surface = GroundSurface(Surface([rect.w, rect.h]))
        ground_surface.rect.left = rect.left
        ground_surface.rect.top = rect.top
        self.curpos[type] += value
        return ground_surface

    # 填充一个surface到画布上，以变形/重复等方式 fill_rect指定填充范围 默认全图
    def fill_surface(self, surface: Surface, mode="scale", fill_rect=None):
        rect = surface.get_rect()
        if fill_rect is None:
            fill_rect = self.rect
            rect.left = 0
            rect.top = 0
        else:
            rect.left = fill_rect.left
            rect.top = fill_rect.top

        if mode == "scale":
            # print(self.rect.w,self.rect.h)
            self.surface.blit(scale(surface, (fill_rect.w, fill_rect.h)), fill_rect)
        elif mode == "repeat":
            while rect.bottom <= fill_rect.bottom:
                while rect.right <= fill_rect.right:
                    self.surface.blit(surface, rect)
                    rect.left += rect.w
                rect.left = 0
                rect.top += rect.h

    # 填充一个sprite到画布上 这个Sprite会被添加到当前画布的精灵组
    def add_sprite(self, sprite, mode="normal", fill_rect=None):
        if fill_rect is not None:
            if mode == "scale":  # 这个对精灵基本没用 放弃吧
                sprite.image = scale(sprite.image, (fill_rect.w, fill_rect.h))
            sprite.rect.left = fill_rect.left
            sprite.rect.top = fill_rect.top
        self.group.add(sprite)

    #  重定位 - 画布的内部逻辑坐标转换为外部坐标（父类可视坐标系）
    def relocate(self, *args):
        x, y = self.trans_loacate(*args)
        x += self.rect.left
        y += self.rect.top
        return x, y

    #  重新设置surface大小 其他设置不变（如果增大会向右下扩张）
    def resize(self, w, h):
        self.surface = Surface((w, h))
        self.rect.w = w
        self.rect.h = h

    # 需要被实现 逻辑坐标到物理坐标的转换:
    def trans_loacate(self, *args):
        return args

    #  刷新函数： 可以根据变化层级刷新部分内容而不是全部一起刷新
    #  !不同画布不能有不同的刷新率，刷新率以最快为准，控制动画频率在sprite的update中自行控制
    def flush(self, screen=None):
        self.group.update(pygame.time.get_ticks())
        self.group.draw(self.surface)
        if screen is not None:
            screen.blit(self.surface.convert_alpha(self.surface), self.rect)
        for c in self.children:
            c.flush(screen=self.surface)

    # 填充纯色（debug使用）
    def fill(self, arg):
        self.surface.fill(arg)


"""
wall = pygame.image.load("img/wall.png")

screen = pygame.display.set_mode([WIDTH, HEIGHT])  # 初始化窗口
rootSurface = GroundSurface(screen)
s1 = rootSurface.add_child("left", 224)  # 状态栏
s1_1 = s1.add_child("top", 40)
s1_2 = s1.add_child("mid", 90)
s1_3 = GroundSurface(0, 0, 120, 120, 0.4)
s1.add_child(s1_3)
s2 = rootSurface.add_child("bottom", 64)  # 道具栏
# s3 = rootSurface.add_child(MapGround(13, 13, 32), 224, 0)
# s12.fill_surface(wall, "scale")
# s3.fill_surface(wall, "repeat")

from tower_map import MAP_DATABASE

s1_1.fill(RED)
s1_2.fill(WHITE)
s1.fill(GREEN)
s2.fill(BLUE)
# s2.add_sprite(EventSprite("201", enemy_image["201"], [1, 2]))

# s3.draw_map(MAP_DATABASE[0])

running = True
ct = 1

# clock = pygame.time.Clock()

import threading
def console():
    while True:
        try:
            print(eval(input()))
        except:
            print("error")

t = threading.Thread(target=console)
t.start()

while running:
    pygame.display.update()
    pygame.time.delay(10)
    rootSurface.flush(screen=screen)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
"""
