############################################################
#                                                          #
#  calc_score.py                                           #
#                                                          #
#    スコア計算処理ファイル                                    #
#                                                          #
#      2025/xx/xx   新規作成                                 #
#                                                          #
#                                                          #
############################################################


############################################################
#                                                          #
#  calc_kind_speed                                         #
#                                                          #
#    スコア計算補助処理　　                                    #
#                                                          #
#      内容:落下物の種類、落下速度に応じたスコアを計算 　　　　     #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
def calc_kind_speed(kind, speed):
    return kind * speed


############################################################
#                                                          #
#  calc_score                                              #
#                                                          #
#    スコア計算処理　　                                       #
#                                                          #
#      内容:落下物の種類、レベル、落下速度に応じたスコアを計算      #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
def calc_score(kind, level, fall_speed):
    score = 0

    if level == 5:
        score += calc_kind_speed(kind, fall_speed) * level * 20
    if level == 4:
        score += calc_kind_speed(kind, fall_speed) * level * 10
    if level == 3:
        score += calc_kind_speed(kind, fall_speed) * level * 5
    if level == 2:
        score += calc_kind_speed(kind, fall_speed) * level * 2
    if level == 1:
        score += calc_kind_speed(kind, fall_speed)
    
    return score
