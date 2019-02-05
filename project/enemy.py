from lib.utools import *

# --- Monster Data START ---

MONSTER_DATA = {
    "greenSlime": {"name": "草精灵", "hp": 10, "atk": 2, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "redSlime": {"name": "火精灵", "hp": 15, "atk": 3, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0,
                 "value": 10},
    "blackSlime": {"name": "青头怪", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "slimelord": {"name": "怪王", "hp": 100, "atk": 120, "def": 0, "money": 10, "experience": 0, "point": 0,
                  "special": [1, 9]},
    "bat": {"name": "水精灵", "hp": 20, "atk": 4, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "bigBat": {"name": "草精灵", "hp": 30, "atk": 4, "def": 2, "money": 0, "experience": 0, "point": 0, "special": 0},
    "redBat": {"name": "火精灵", "hp": 40, "atk": 6, "def": 2, "money": 0, "experience": 0, "point": 0, "special": 0},
    "vampire": {"name": "水精灵", "hp": 50, "atk": 8, "def": 2, "money": 0, "experience": 0, "point": 0, "special": 0},
    "skeleton": {"name": "草精灵", "hp": 60, "atk": 6, "def": 3, "money": 0, "experience": 0, "point": 1, "special": 0},
    "skeletonSoilder": {"name": "火精灵", "hp": 80, "atk": 10, "def": 5, "money": 0, "experience": 0, "point": 1,
                        "special": 0},
    "skeletonCaptain": {"name": "水精灵", "hp": 100, "atk": 14, "def": 7, "money": 0, "experience": 0, "point": 1,
                        "special": 0},
    "ghostSkeleton": {"name": "草精灵", "hp": 150, "atk": 20, "def": 12, "money": 0, "experience": 0, "point": 1,
                      "special": 0},
    "zombie": {"name": "火精灵", "hp": 200, "atk": 25, "def": 16, "money": 0, "experience": 0, "point": 1, "special": 0},
    "zombieKnight": {"name": "水精灵", "hp": 250, "atk": 30, "def": 20, "money": 0, "experience": 0, "point": 1,
                     "special": 0},
    "rock": {"name": "草精灵", "hp": 200, "atk": 20, "def": 18, "money": 0, "experience": 0, "point": 1, "special": 2},
    "slimeMan": {"name": "火精灵", "hp": 300, "atk": 28, "def": 24, "money": 0, "experience": 0, "point": 1, "special": 2,
                 "atkValue": 2, "defValue": 3},
    "bluePriest": {"name": "水精灵", "hp": 400, "atk": 36, "def": 30, "money": 0, "experience": 0, "point": 1,
                   "special": 2},
    "redPriest": {"name": "高级法师", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "brownWizard": {"name": "初级巫师", "hp": 100, "atk": 120, "def": 0, "money": 16, "experience": 0, "point": 0,
                    "special": 15, "value": 100, "range": 2},
    "redWizard": {"name": "高级巫师", "hp": 1000, "atk": 1200, "def": 0, "money": 160, "experience": 0, "point": 0,
                  "special": 15, "value": 200, "zoneSquare": True},
    "yellowGuard": {"name": "土精灵", "hp": 120, "atk": 24, "def": 16, "money": 0, "experience": 0, "point": 1,
                    "special": 0},
    "blueGuard": {"name": "中级卫兵", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "redGuard": {"name": "高级卫兵", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "swordsman": {"name": "双手剑士", "hp": 100, "atk": 120, "def": 0, "money": 6, "experience": 0, "point": 0,
                  "special": [5, 23]},
    "soldier": {"name": "冥战士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "yellowKnight": {"name": "金骑士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "redKnight": {"name": "红骑士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "darkKnight": {"name": "黑骑士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "blackKing": {"name": "草之源", "hp": 720, "atk": 380, "def": 32, "money": 0, "experience": 0, "point": 1,
                  "special": 2, "notBomb": False},
    "yellowKing": {"name": "水之源", "hp": 360, "atk": 460, "def": 30, "money": 0, "experience": 0, "point": 1,
                   "special": 2},
    "greenKing": {"name": "火之源", "hp": 280, "atk": 940, "def": 32, "money": 0, "experience": 0, "point": 1,
                  "special": 2},
    "blueKnight": {"name": "蓝骑士", "hp": 100, "atk": 120, "def": 0, "money": 9, "experience": 0, "point": 0,
                   "special": 8},
    "goldSlime": {"name": "黄头怪", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "poisonSkeleton": {"name": "紫骷髅", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0,
                       "special": 0},
    "poisonBat": {"name": "紫蝙蝠", "hp": 100, "atk": 120, "def": 0, "money": 14, "experience": 0, "point": 0,
                  "special": 13},
    "steelRock": {"name": "铁面人", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "skeletonPriest": {"name": "骷髅法师", "hp": 100, "atk": 100, "def": 0, "money": 0, "experience": 0, "point": 0,
                       "special": 18, "value": 20},
    "skeletonKing": {"name": "骷髅王", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "skeletonWizard": {"name": "骷髅巫师", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0,
                       "special": 0},
    "redSkeletonCaption": {"name": "骷髅武士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0,
                           "special": 0},
    "badHero": {"name": "迷失勇者", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "demon": {"name": "魔神武士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "demonPriest": {"name": "魔神法师", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "goldHornSlime": {"name": "金角怪", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0,
                      "special": 0},
    "redKing": {"name": "土之源", "hp": 810, "atk": 330, "def": 33, "money": 0, "experience": 0, "point": 1, "special": 2},
    "whiteKing": {"name": "白衣武士", "hp": 100, "atk": 120, "def": 0, "money": 17, "experience": 0, "point": 0,
                  "special": 16},
    "blackMagician": {"name": "黑暗大法师", "hp": 100, "atk": 120, "def": 0, "money": 12, "experience": 0, "point": 0,
                      "special": 11, "value": 0.3333333333333333, "add": True, "notBomb": True},
    "silverSlime": {"name": "银头怪", "hp": 100, "atk": 120, "def": 0, "money": 15, "experience": 0, "point": 0,
                    "special": 14},
    "swordEmperor": {"name": "剑圣", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "whiteHornSlime": {"name": "尖角怪", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0,
                       "special": 0},
    "badPrincess": {"name": "痛苦魔女", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "badFairy": {"name": "黑暗仙子", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "grayPriest": {"name": "中级法师", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "redSwordsman": {"name": "剑王", "hp": 100, "atk": 120, "def": 0, "money": 7, "experience": 0, "point": 0,
                     "special": 6, "n": 8},
    "whiteGhost": {"name": "水银战士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "poisonZombie": {"name": "绿兽人", "hp": 100, "atk": 120, "def": 0, "money": 13, "experience": 0, "point": 0,
                     "special": 12},
    "magicDragon": {"name": "魔龙", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "octopus": {"name": "血影", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "darkFairy": {"name": "仙子", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "greenKnight": {"name": "强盾骑士", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "angel": {"name": "天使", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "elemental": {"name": "元素生物", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 0},
    "steelGuard": {"name": "铁守卫", "hp": 0, "atk": 0, "def": 0, "money": 0, "experience": 0, "point": 0, "special": 18,
                   "value": 20},
    "evilBat": {"name": "邪恶蝙蝠", "hp": 1000, "atk": 1, "def": 0, "money": 0, "experience": 0, "point": 0,
                "special": [2, 3]}
}
MONSTER_START_NUM = 200
MONSTER_IMG = crop_images(load_image("img/enemys.png"),
                          MONSTER_START_NUM,
                          pygame.Rect(0, 0, BLOCK_UNIT*2, BLOCK_UNIT))


# :TODO:
def register_monster(enemy_id, info):
    pass


def get_damage_info(enemy_id):
    pass

# --- Monster Data END ---

# !insert! === 在这里写敌人相关的自定义操作 ===
