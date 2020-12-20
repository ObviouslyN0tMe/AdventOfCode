# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


class Tile(object):
    def __init__(self, id_number, tile_content):
        self.id_number = id_number
        self.tile_content = tile_content
        self.tile_borders = {}
        self.__updateBorders__()
        self.possible_borders = list(self.tile_borders.values()) + \
                                [border[::-1] for border in list(self.tile_borders.values())]
        self.jigsaw_border = {"T": True, "L": True, "B": True, "R": True}
        self.turned = 0
        self.mirrored = False

    def __updateBorders__(self):
        top_border = self.tile_content[0]
        left_border = "".join([line[0] for line in self.tile_content])
        bottom_border = self.tile_content[-1]
        right_border = "".join([line[-1] for line in self.tile_content])
        self.tile_borders = {"T": top_border, "L": left_border, "B": bottom_border, "R": right_border}

    # turn tile right by 90°
    def turn(self):
        self.turned += 90
        self.turned %= 360
        old_content = self.tile_content.copy()
        new_content = []
        for line_index in range(1, len(old_content)+1):
            new_content.append("".join([line[-line_index] for line in old_content]))
        self.tile_content = new_content
        self.__updateBorders__()

    # mirror the tile
    def mirror(self):
        self.mirrored = not self.mirrored
        self.tile_content.reverse()
        self.turned = 90 if self.turned == 270 else 90
        self.turned = 270 if self.turned == 90 else 270
        self.__updateBorders__()

    # get any borders with starting letter of direction in string e.g.: "TLB" returns top, left and bottom borders
    def getBorders(self, directions):
        return [self.tile_borders[direction] for direction in directions]


def formatData(data):
    tiles = []
    tile_content = []
    id_number = ""
    for line in data:
        # create tile-object
        if line == "":
            tiles.append(Tile(id_number, tile_content))
            tile_content = []
        # get id_number of tile
        elif line.startswith("T"):
            id_number = line[5:-1]
        # collect tile content
        else:
            tile_content.append(line)
    tiles.append(Tile(id_number, tile_content))
    return tiles


def sortTiles(tiles):
    corner_tiles = []
    border_tiles = []
    normal_tiles = []
    tiles_to_check = tiles.copy()
    for tile in tiles:
        tiles_to_check.remove(tile)
        for direction, tile_border in tile.tile_borders.items():
            for checked_tile in tiles_to_check:
                if tile_border in checked_tile.possible_borders:
                    tile.jigsaw_border[direction] = False
                    break
        border_count = list(tile.jigsaw_border.values()).count(True)
        if border_count == 0:
            normal_tiles.append(tile)
        elif border_count == 1:
            border_tiles.append(tile)
        else:
            corner_tiles.append(tile)
        tiles_to_check.append(tile)
    return normal_tiles, border_tiles, corner_tiles


def solveJigsaw(tiles):
    pass


puzzle_tiles = formatData(rawdata)
normal_puzzle_tiles, border_puzzle_tiles, corner_puzzle_tiles = sortTiles(puzzle_tiles)
print([tile.id_number for tile in normal_puzzle_tiles])
print([tile.id_number for tile in border_puzzle_tiles])
print([tile.id_number for tile in corner_puzzle_tiles])
