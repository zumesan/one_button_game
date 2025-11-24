############################################################
#                                                          #
#  title_scene.py                                          #
#                                                          #
#    TitleSceneクラス                                       #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
import pyxel
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RESOURCE_IMG_1, SCENE_PLAY, PRESS_ENTER_KEY_TEXT

class TitleScene:

    ############################################################
    #                                                          #
    #  __init__                                                #
    #                                                          #
    #    タイトル画面初期化処理                                    #
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
    #    タイトル画面開始処理                                     #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def start(self):
        # 変数の初期化
        self.game.player = None


    ############################################################
    #                                                          #
    #  update                                                  #
    #                                                          #
    #    タイトル画面更新処理                                     #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def update(self):
        game = self.game

        if pyxel.btnp(pyxel.KEY_RETURN):
            game.change_scene(SCENE_PLAY)


    ############################################################
    #                                                          #
    #  draw                                                    #
    #                                                          #
    #    タイトル画面描画処理                                     #
    #                                                          #
    #          2025/xx/xx   新規作成                            #
    #                                                          #
    #                                                          #
    ############################################################
    def draw(self):
        pyxel.blt(
            (SCREEN_WIDTH - 8) / 2 - 48,
            SCREEN_HEIGHT / 5,
            RESOURCE_IMG_1,
            0,
            0,
            96,
            16,
            0
        )

        pyxel.text(
            (SCREEN_WIDTH - 8) / 2 - (len(PRESS_ENTER_KEY_TEXT) * 3 / 2) - 8,
            SCREEN_HEIGHT / 5 * 4,
            PRESS_ENTER_KEY_TEXT,
            7,
        )