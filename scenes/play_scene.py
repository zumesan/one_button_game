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

class PlayScene:
    def __init__(self, game):
        self.game = game

    def start(self):
        pass
    
    def update(self):
        pass

    def draw(self):
        self.game.player.draw()