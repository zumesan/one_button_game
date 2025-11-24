############################################################
#                                                          #
#  game.py                                                 #
#                                                          #
#    ゲーム処理                                              #
#                                                          #
#      2025/xx/xx   新規作成                                 #
#                                                          #
#                                                          #
############################################################

import pyxel

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities import Player
from scenes import PlayScene

class Game:
    # ゲーム初期化
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ONE_BUTTON_GAME")
        pyxel.load("assets/one_button_game.pyxres")
        pyxel.tilemaps[0].blt(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player_start_position = [SCREEN_WIDTH / 2 - 8, SCREEN_HEIGHT / 5 * 4 + 8]
        self.player = None

        self.scenes = {
            "play": PlayScene(self),
        }
        self.scene_name = "play"
        self.change_scene(self.scene_name)

        pyxel.run(self.update, self.draw)

    # ゲームシーン切り替え
    def change_scene(self, scene_name):
        self.scene_name = scene_name
        self.scenes[self.scene_name].start()

    # ゲーム更新処理
    def update(self):
        self.scenes[self.scene_name].update()

    # ゲーム画面描画処理
    def draw(self):
        self.scenes[self.scene_name].draw()