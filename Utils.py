# Comfortable using frequent code

def tile_xy2i(tx, ty):
    """convert tile's coordinate 2 tile's index
    (using in Field for tiles container)"""
    return str(tx) + ':' + str(ty)