############################################################
#                                                          #
#  play_scene.py                                           #
#                                                          #
#    PlaySceneクラス                                        #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################

import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import FallObject, Player

class PlayScene:

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    プレイ画面初期化処理                                     #
    #                                                          #
    #        game:呼び出し元インスタンス                           #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def __init__(self, game):
        self.game = game


    ############################################################
    #                                                          #
    #  start                                                   #
    #                                                          #
    #    プレイ画面開始処理                                       #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def start(self):
        # プレイ画面を初期化
        pyxel.tilemaps[0].blt(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        # プレイヤー初期化
        self.game.player = Player(self.game)


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    プレイ画面更新処理                                       #
    #                                                          #
    #      内容:インスタンスの更新処理呼び出し                       #
    #                                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):
        game = self.game
        game.player.update()

        # プレイ時間カウントアップ
        game.play_time += 1

        if game.play_time % 50 == 0:
            # 落下物のインスタンスを生成
            FallObject(game)


    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    プレイ画面描画処理                                       #
    #                                                          #
    #      内容:インスタンスの描画処理呼び出し                       #
    #                                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def draw(self):
        # 画面クリア
        pyxel.cls(0)

        self.game.player.draw()

        for fall in self.game.fall_objects:
            fall.draw()

# debug
        pyxel.text(
            8,
            8,
            str(int(self.game.play_time)),
            10
        )
# debug