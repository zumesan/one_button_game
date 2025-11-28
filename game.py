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
from scenes import TitleScene, PlayScene, GameOverScene

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_TITLE, SCENE_PLAY, SCENE_GAME_OVER

class Game:
    # ゲーム初期化


    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    ゲーム初期化処理                                         #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ONE_BUTTON_GAME")
        pyxel.load("assets/one_button_game.pyxres")
        pyxel.tilemaps[0].blt(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player_start_position = [SCREEN_WIDTH / 2 - 8, SCREEN_HEIGHT / 5 * 4 + 8] # プレイヤーの初期位置
        self.player = None
        self.fall_objects = []

        self.scenes = {
            SCENE_TITLE: TitleScene(self),
            SCENE_PLAY: PlayScene(self),
            SCENE_GAME_OVER: GameOverScene(self),
        }

        self.play_time = 0   # ゲームのプレイ時間
        self.level = 0       # ゲームの難易度
        self.fall_speed = 0  # オブジェクトの落下速度
        self.score = 0       # スコア

        self.scene_name = SCENE_TITLE
        self.change_scene(self.scene_name)

        pyxel.run(self.update, self.draw)


    ############################################################
    #                                                          #
    #  change_scene                                            #
    #                                                          #
    #    ゲームシーン遷移処理                                     #
    #                                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def change_scene(self, scene_name):
        self.scene_name = scene_name
        self.scenes[self.scene_name].start()


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    ゲームシーン更新処理                                     #
    #                                                          #
    #      内容:現在のゲームシーンの更新処理呼び出し                  #
    #                                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):
        self.scenes[self.scene_name].update()


    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    ゲームシーン描画処理                                     #
    #                                                          #
    #      内容:現在のゲームシーンの描画処理呼び出し                  #
    #                                                          #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def draw(self):
        self.scenes[self.scene_name].draw()