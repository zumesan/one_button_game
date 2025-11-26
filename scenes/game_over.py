############################################################
#                                                          #
#  game_over_scene.py                                      #
#                                                          #
#    GameOverSceneクラス                                    #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################

import pyxel
from constants import PRESS_ENTER_KEY_TEXT, SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_TITLE

class GameOverScene:

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    ゲームオーバー画面初期化処理                               #
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
    #    ゲームオーバー画面開始処理                                #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def start(self):
        self.game.player = None
        self.game.fall_objects = []


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    ゲームオーバー画面更新処理                                #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):
        # Returnキーが押された?
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game.change_scene(SCENE_TITLE)

    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    ゲームオーバー画面描画処理                                #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def draw(self):
        pyxel.cls(0)
        
        pyxel.text(
            (SCREEN_WIDTH - 8) / 2 - (len(PRESS_ENTER_KEY_TEXT) * 3 / 2) - 8,
            SCREEN_HEIGHT / 5 * 4,
            PRESS_ENTER_KEY_TEXT,
            7,
        )