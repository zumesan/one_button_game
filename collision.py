############################################################
#                                                          #
#  collision.py                                            #
#                                                          #
#    当たり判定処理                                          #
#                                                          #
#      2025/xx/xx   新規作成                                 #
#                                                          #
#                                                          #
############################################################


############################################################
#                                                          #
#  check_collision                                         #
#                                                          #
#    衝突判定処理　　　                                       #
#                                                          #
#      内容:オブジェクト同士の衝突判定                          #
#                                                          #
#          2025/xx/xx   新規作成                            #
#                                                          #
#                                                          #
############################################################
def check_collision(player, fall_objects):
    flg = False

    player_x1 = player.x + player.hit_area[0]
    player_y1 = player.y + player.hit_area[1]
    player_x2 = player.x + player.hit_area[2]
    player_y2 = player.y + player.hit_area[3]

    fall_objects_x1 = fall_objects.x + fall_objects.hit_area[0]
    fall_objects_y1 = fall_objects.y + fall_objects.hit_area[1]
    fall_objects_x2 = fall_objects.x + fall_objects.hit_area[2]
    fall_objects_y2 = fall_objects.y + fall_objects.hit_area[3]

    if player_x1 > fall_objects_x2:
        return flg
    if player_x2 < fall_objects_x1:
        return flg
    if player_y1 > fall_objects_y2:
        return flg
    if player_y2 < fall_objects_y1:
        return flg
    
    flg = True

    return flg