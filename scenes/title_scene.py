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
        game = self.game
        # 変数の初期化
        game.player = None
        game.fall_objects = [] 

        game.play_time = 0
        game.level = 0
        game.fall_speed = 0
        game.score = 0


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

        if pyxel.btnp(pyxel.KEY_SPACE):
            game.level += 1

            # 難易度設定が5を超える?
            if game.level > 4:
                game.level = 0
            # 難易度設定が1を下回る?
            if game.level < 0:
                game.level = 4

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game.level += 1
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
        # 画面クリア
        pyxel.cls(0)
        
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


        # 選択難易度表示
        pyxel.blt(
            (SCREEN_WIDTH - 8) / 2 - 16,
            SCREEN_HEIGHT / 5 * 3,
            RESOURCE_IMG_1,
            0,
            self.game.level * 8 + 32,
            32,
            8,
            0
        )

        pyxel.text(
            (SCREEN_WIDTH - 8) / 2 - (len(PRESS_ENTER_KEY_TEXT) * 3 / 2) - 8,
            SCREEN_HEIGHT / 5 * 4,
            PRESS_ENTER_KEY_TEXT,
            7,
        )