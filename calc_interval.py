############################################################
#                                                          #
#  calc_interval.py                                        #
#                                                          #
#    落下物出現インターバル計算処理ファイル                      #
#                                                          #
#      2025/xx/xx   新規作成                                 #
#                                                          #
#                                                          #
############################################################


############################################################
#                                                          #
#  calc_interval_initialize                                #
#                                                          #
#    落下物出現インターバル初期値計算処理                        #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
def calc_interval_initialize(level):
    interval = 50

    interval = max(60 - (level * 10), 10)

    return interval


############################################################
#                                                          #
#  calc_interval_change                                    #
#                                                          #
#    落下物出現インターバル変更計算処理                          #
#                                                          #
#      内容:経過時間に応じて落下物出現頻度を再計算する             #
#          50秒経過で最大値になるようにする                     #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
def calc_interval_change(interval, level):

    if level == 1:
        return max(interval - 5, 25)
    if level == 2:
        return max(interval - 5, 15)
    if level == 3:
        return max(interval - 4, 10)
    if level == 4:
        return max(interval - 3, 7)
    if level == 5:
        return max(interval - 1, 5)
    
    return interval
