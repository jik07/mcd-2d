def dirt_grass(horizontal, xChange, yChange, player_rect, tile, movement, ignore):
    if horizontal:
        if xChange > 0:
            player_rect.right = tile[0].left
        if xChange < 0:
            player_rect.left = tile[0].right
    else:
        if yChange > 0:
            player_rect.bottom = tile[0].top
            yChange = 0
            ignore = False
            movement[2] = False
        if yChange < 0:
            player_rect.top = tile[0].bottom
            yChange = 0
            ignore = True

    return xChange, yChange, player_rect, movement, ignore


def portal(player_rect, s, new_level, yChange, xChange, ignore):
    s[0] += 1
    s[1] = 0
    new_level = True
    player_rect.x = -200
    player_rect.y = -200
    yChange, xChange = 0, 0
    ignore = False
    return player_rect, s, new_level, yChange, xChange, ignore

def lava(player_rect, spawn, yChange, xChange, ignore):
    player_rect.x = spawn[0]
    player_rect.y = spawn[1]
    yChange, xChange = 0, 0
    ignore = False
    return player_rect, yChange, xChange, ignore
