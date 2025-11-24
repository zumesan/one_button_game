############################################################
#                                                          #
#  play_scene.py                                           #
#                                                          #
#    PlaySceneクラス                                        #
#                                                          #
#      2025/xx/xx   新規作成                                #
#                                                          #
#                                                          #
############################################################

import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Player

class PlayScene:
    def __init__(self, game):
        self.game = game

    def start(self):
        # プレイ画面を初期化
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        # プレイヤー初期化
        self.game.player = Player(self.game)

    def update(self):
        self.game.player.update()

    def draw(self):
        # 画面クリア
        pyxel.cls(0)
        
        self.game.player.draw()