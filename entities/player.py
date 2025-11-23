############################################################
#                                                          #
#  player.py                                               #
#                                                          #
#    プレイヤークラス                                         #
#                                                          #
#      2025/xx/xx   新規作成                                 #
#                                                          #
#                                                          #
############################################################

import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    プレイヤー初期化処理                                     #
    #                                                          #
    #      2025/xx/xx   新規作成                                 #
    #                                                          #
    #        game:呼び出し元インスタンス                           #
    #                                                          #
    #                                                          #
    ############################################################
    def __init__(self, game):
        self.game = game


    def update(self):
        pass

    def draw(self):
        pyxel.blt(
            self.game.player_start_position[0],
            self.game.player_start_position[1],
            0,
            8,
            0,
            16,
            16,
            1,
        )