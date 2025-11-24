############################################################
#                                                          #
#  player.py                                               #
#                                                          #
#    プレイヤークラス                                         #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################

import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RESOURCE_IMG_0

class Player:
    MOVE_SPEED = 3  # プレイヤーの移動速度

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    プレイヤー初期化処理                                     #
    #                                                          #
    #        game:呼び出し元インスタンス                           #
    #        dx:プレイヤーのx座標移動距離                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def __init__(self, game):
        self.game = game
        self.x = game.player_start_position[0]
        self.y = game.player_start_position[1]
        self.dx = -Player.MOVE_SPEED
        self.direction = -1 # 移動方向(-1:左方向、1:右方向)


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    プレイヤー更新処理                                       #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):

        # スペースキーが押された?
        if pyxel.btnp(pyxel.KEY_SPACE):
            # 移動方向を変更
            self.direction *= -1
            self.dx = Player.MOVE_SPEED * self.direction

        # プレイヤー移動    
        self.x += self.dx

        # 画面の外に出た場合、反対側に移動させる
        if self.x < -8:
            self.x = pyxel.width - 8
        if self.x > pyxel.width - 8:
            self.x = -8


    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    プレイヤー描画処理                                       #
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
            8,
            0,
            16,
            16,
            1,
        )