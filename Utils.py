# Comfortable using frequent code

def tile_xy2i(tx, ty):
    """convert tile's position 2 tile's index
    (using in Field for tiles container)"""
    return str(tx) + ':' + str(ty)

def tile_i2xy(index):
    """convert tiles's index 2 tiles's position
    (using in Field for tiles container)"""
    return index.split(':')

