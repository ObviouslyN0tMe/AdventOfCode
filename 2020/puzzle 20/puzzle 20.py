import math
# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


class Tile(object):
    def __init__(self, id_number, tile_content):
        self.id_number = int(id_number)
        self.tile_content = tile_content
        self.tile_borders = {}
        self.__updateBorders__()
        self.possible_borders = list(self.tile_borders.values()) + \
                                [border[::-1] for border in list(self.tile_borders.values())]
        self.jigsaw_border = {"T": True, "L": True, "B": True, "R": True}

    # update borders if content changes
    def __updateBorders__(self):
        top_border = self.tile_content[0]
        left_border = "".join([line[0] for line in self.tile_content])
        bottom_border = self.tile_content[-1]
        right_border = "".join([line[-1] for line in self.tile_content])
        self.tile_borders = {"T": top_border, "L": left_border, "B": bottom_border, "R": right_border}

    # turn tile right by 90°
    def turn(self):
        # new content
        old_content = self.tile_content.copy()
        new_content = []
        for line_index in range(1, len(old_content) + 1):
            new_content.append("".join([line[-line_index] for line in old_content]))
        self.tile_content = new_content
        # new borders
        self.__updateBorders__()
        old_jigsaw_border = self.jigsaw_border.copy()
        self.jigsaw_border["T"] = old_jigsaw_border["L"]
        self.jigsaw_border["L"] = old_jigsaw_border["B"]
        self.jigsaw_border["B"] = old_jigsaw_border["R"]
        self.jigsaw_border["R"] = old_jigsaw_border["T"]

    # mirror the tile
    def mirror(self):
        # new content
        self.tile_content.reverse()
        # new borders
        self.__updateBorders__()
        old_jigsaw_border = self.jigsaw_border.copy()
        self.jigsaw_border["T"] = old_jigsaw_border["B"]
        self.jigsaw_border["B"] = old_jigsaw_border["T"]

    # get any borders with starting letter of direction in string e.g.: "TLB" returns top, left and bottom borders
    def getBorders(self, directions):
        return [self.tile_borders[direction] for direction in directions]

    # get content without borders
    def getPicture(self):
        picture = []
        content = self.tile_content
        for line in content[1:-1]:
            picture.append(line[1:-1])
        return picture


# get tiles from input
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
    tiles_to_check = tiles.copy()
    for tile in tiles:
        tiles_to_check.remove(tile)
        for direction, tile_border in tile.tile_borders.items():
            for checked_tile in tiles_to_check:
                if tile_border in checked_tile.possible_borders:
                    tile.jigsaw_border[direction] = False
                    break
        border_count = list(tile.jigsaw_border.values()).count(True)
        if border_count == 2:
            corner_tiles.append(tile)
        tiles_to_check.append(tile)
    return corner_tiles


def searchMatchingTile(remaining_tiles, border_to_search, direction_to_search):
    matching_tile = None
    for remaining_tile in remaining_tiles:
        # 8 possible borders
        for i in range(8):
            current_border = remaining_tile.getBorders(direction_to_search)
            if current_border == border_to_search:
                matching_tile = remaining_tile
                break
            remaining_tile.turn()
            if (i+1) % 4 == 0:
                remaining_tile.mirror()
        # if matching tile is found
        if matching_tile:
            break
    return matching_tile


def solveJigsaw(remaining_tiles, start_tile):
    # prepare while loop
    current_coordinates = [0, 0]
    remaining_tiles.remove(start_tile)
    new_column = False
    # start tile bottom left at [0, 0]
    current_tile = start_tile
    while current_tile.jigsaw_border != {"T": False, "L": True, "B": True, "R": False}:
        current_tile.turn()
    current_columnstart = start_tile
    solution = {tuple(current_coordinates): start_tile}
    # place next tile until no tiles are left
    while remaining_tiles:
        # get border and direction to search, update current coordinates
        if new_column:
            border_to_search = current_columnstart.getBorders("R")
            direction_to_search = "L"
            current_coordinates[1] += 1
            current_coordinates[0] = 0
        else:
            border_to_search = current_tile.getBorders("T")
            direction_to_search = "B"
            current_coordinates[0] += 1
        # search for border in remaining tiles
        matching_tile = searchMatchingTile(remaining_tiles, border_to_search, direction_to_search)
        # if a tile was found
        if matching_tile:
            current_tile = matching_tile
            remaining_tiles.remove(matching_tile)
            solution[tuple(current_coordinates)] = matching_tile
            if new_column:
                current_columnstart = matching_tile
                new_column = False
        # else start a new row
        else:
            new_column = True
    return solution, current_coordinates[0] + 1, current_coordinates[1] + 1


def createPicture(solved_jigsaw, height, width):
    picture = []
    tile_height = len(solved_jigsaw[(0, 0)].getPicture())
    counter = 0
    for row_nr in range(height - 1, -1, -1):
        for i in range(tile_height):
            picture.append("")
        for tile_nr in range(width):
            tile = solved_jigsaw[(row_nr, tile_nr)]
            tile_picture = tile.getPicture()
            for index, content in enumerate(tile_picture):
                picture[counter*tile_height+index] += content
        counter += 1
    return picture


def identifySeamonster(picture, y, x):
    monster_indexes = {0: [18],                                              #
                       1: [0, 5, 6, 11, 12, 17, 18, 19],   #    ##    ##    ###
                       2: [1, 4, 7, 10, 13, 16]}            #  #  #  #  #  #
    for rel_y, rel_x_list in monster_indexes.items():
        for rel_x in rel_x_list:
            if picture[y+rel_y][x+rel_x] != "#":
                return False
    return True


def countSeamonsters(picture):
    counter = 0
    for y in range(len(picture) - 2):
        for x in range(len(picture[0]) - 19):
            if identifySeamonster(picture, y, x):
                counter += 1
    return counter


def countWaterRoughness(picture, seamonster_count):
    counter = 0
    for line in picture:
        counter += line.count("#")
    counter -= seamonster_count*15
    return counter


def part2ForAllPictures(picture_tile):
    for i in range(8):
        seamonster_count = countSeamonsters(picture_tile.tile_content)
        if seamonster_count > 0:
            return countWaterRoughness(picture_tile.tile_content, seamonster_count)
        picture_tile.turn()
        if (i + 1) % 4 == 0:
            picture_tile.mirror()


# part 1
puzzle_tiles = formatData(rawdata)
corner_puzzle_tiles = sortTiles(puzzle_tiles)

# part 2
solved_jigsaw, width, height = solveJigsaw(puzzle_tiles, corner_puzzle_tiles[0])
picture_list = createPicture(solved_jigsaw, height, width)
picture_tile = Tile(0, picture_list)

# output
print("Finished Jigsaw:")
[print(line) for line in picture_list]
print("Part 1:", math.prod([x.id_number for x in corner_puzzle_tiles]))
print("Part 2:", part2ForAllPictures(picture_tile))
