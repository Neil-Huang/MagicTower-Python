import pygame
from lib import CurrentMap
from .sprite import EventSprite
from sysconf import *
from project.function import *


class Player(EventSprite):
    def __init__(self):
        from os import path
        player_img = pygame.image.load(path.join(img_dir, "hero48.png"))
        self.image = pygame.transform.scale(player_img, (int(BLOCK_UNIT * 4), int(BLOCK_UNIT * 4)))
        # self.image.set_colorkey(WHITE)
        super().__init__(0, self.image, [4, 4])
        self.speedx = 0
        self.speedy = 0
        self.pos = [X_COORDINATE, Y_COORDINATE]
        self.floor = PLAYER_FLOOR
        map_pos = CurrentMap.trans_loacate(*self.pos, "down")
        self.rect.centerx = map_pos[0]
        self.rect.bottom = map_pos[1]
        self.animate_speed = 250  # 移动一格所需要的毫秒数 & 换腿所需时间的两倍
        self.animate = False
        self.hp = PLAYER_HP
        self.attack = PLAYER_ATK
        self.defend = PLAYER_DEF
        self.mdefend = PLAYER_MDEF
        self.gold = PLAYER_GOLD
        self.exp = PLAYER_EXP
        self.yellowkey = PLAYER_YELLOWKEY
        self.bluekey = PLAYER_BLUEKEY
        self.redkey = PLAYER_REDKEY
        self.greenkey = PLAYER_GREENKEY
        self.steelkey = PLAYER_STEELKEY
        self.floor = PLAYER_FLOOR
        self.item = PLAYER_ITEM

    # TODO：各种block的处理
    def proc_block(self, block_id, x, y):
        if int(block_id) == 1:
            return False
        elif int(block_id) >= 21 and int(block_id) <= 69:
            pickup_item(block_id, x, y)
            return True
        elif int(block_id) >= 201:
            result = battle(block_id, x, y)
            if result == False:
                return False
        return True

    def update(self, *args):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        key_map = {pygame.K_LEFT: [-1, 0],
                   pygame.K_RIGHT: [1, 0],
                   pygame.K_UP: [0, -1],
                   pygame.K_DOWN: [0, 1]}
        if not self.moving:
            for k in key_map:
                op = key_map[k]
                if keystate[k]:
                    if not self.proc_block(CurrentMap.get_block(self.pos[0] + op[0], self.pos[1] + op[1]), self.pos[0] + op[0], self.pos[1] + op[1]):
                        self.change_face(*op)
                    else:
                        x = op[0] + self.pos[0]
                        y = op[1] + self.pos[1]

                        def temp_fun():
                            self.pos = [x, y]

                        self.move(CurrentMap.trans_loacate(x, y, "down"), callback=temp_fun)

        super().update(*args)
