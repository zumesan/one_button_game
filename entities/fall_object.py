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
        self.hit_area = (3, 1, 10, 14)  # 当たり判定エリア
        self.kind = kind

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

        self.y += min(self.fall_speed * 1.4, 14)

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