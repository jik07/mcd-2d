def dirt_grassH(xChange, player_rect, tile):
    if xChange > 0:
        player_rect.right = tile[0].left
    if xChange < 0:
        player_rect.left = tile[0].right

def dirt_grassV(yChange, player_rect, tile, ignore, movement):
    if yChange > 0:
        player_rect.bottom = tile[0].top
        yChange = 0
        ignore = False
        movement[2] = False
    if yChange < 0:
        player_rect.top = tile[0].bottom
        yChange = 0
        ignore = True
