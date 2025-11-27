############################################################
#                                                          #
#  fall_object.py                                          #
#                                                          #
#    FallObjectクラス                                       #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################

import pyxel

from constants import RESOURCE_IMG_0, KIND_FLOWER, KIND_KNIFE, KIND_HAMMER, KIND_AXE

class FallObject:

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    落下物初期化処理                                        #
    #                                                          #
    #        game:呼び出し元インスタンス                           #
    #        kind:落下物の種類                                   #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def __init__(self, game, x, kind):
        self.game = game
        self.x = x
        self.y = 16
        self.fall_speed = game.fall_speed
        self.kind = kind

        # 種類に応じた判定エリアを設定する
        if self.kind == KIND_FLOWER:
            self.hit_area = (2, 1, 12, 14)
        if self.kind == KIND_KNIFE:
            self.hit_area = (3, 1, 10, 14)
        if self.kind == KIND_HAMMER:
            self.hit_area = (1, 1, 14, 14)
        if self.kind == KIND_AXE:
            self.hit_area = (1, 1, 14, 14)

        self.game.fall_objects.append(self)


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    落下物更新処理                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):
        
        if self.kind == KIND_FLOWER:
            self.y += min(self.fall_speed * 1.4, 24)
        if self.kind == KIND_KNIFE:
            self.y += min(self.fall_speed * 1.6, 26)
        if self.kind == KIND_HAMMER:
            self.y += min(self.fall_speed * 1.8, 28)
        if self.kind == KIND_AXE:
            self.y += min(self.fall_speed * 2.0, 30)

        # 落下物が画面外に出た?
        if self.y >= pyxel.height - 16:
            # 落下物がリストに存在する場合、リストから削除
            if self in self.game.fall_objects:
                self.game.fall_objects.remove(self)


    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    落下物描画処理                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def draw(self):
        pyxel.blt(
            self.x,
            self.y,
            RESOURCE_IMG_0,
            self.kind * 16,
            16,
            16,
            16,
            1,
        )