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