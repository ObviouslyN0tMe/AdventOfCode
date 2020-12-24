import timeit
# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]


def filpTiles(instructions):
    tiles = {}
    flipped_counter = 0
    for instruction in instructions:
        # count directions
        ne_count = instruction.count("ne")
        nw_count = instruction.count("nw")
        se_count = instruction.count("se")
        sw_count = instruction.count("sw")
        e_count = instruction.count("e") - ne_count - se_count
        w_count = instruction.count("w") - nw_count - sw_count
        # x-coord
        coords_x = e_count - w_count + 0.5 * (ne_count + se_count - nw_count - sw_count)
        # y-coord
        coords_y = 0.5 * (ne_count + nw_count - se_count - sw_count)
        # flip tile
        coords = (coords_x, coords_y)
        flipped = tiles.get(coords, False)
        tiles[coords] = not flipped
        # count flipped tiles
        if flipped:
            flipped_counter -= 1
        else:
            flipped_counter += 1
    return flipped_counter, tiles


def getNeighbours(coords, tiles):
    flipped_count = 0
    coord_x = coords[0]
    coord_y = coords[1]
    # calc all neighbours coords
    neighbours_coords = [(coord_x + 1, coord_y), (coord_x - 1, coord_y),
                         (coord_x - 0.5, coord_y - 0.5), (coord_x - 0.5, coord_y + 0.5),
                         (coord_x + 0.5, coord_y - 0.5), (coord_x + 0.5, coord_y + 0.5)]
    # count flipped neighbours
    for neighbour_coords in neighbours_coords:
        if tiles.get(neighbour_coords, False):
            flipped_count += 1
    return neighbours_coords, flipped_count


def doDailyFlipping(tiles):
    new_tiles = {}
    for coords, flipped in tiles.items():
        neighbours_coords, flipped_count = getNeighbours(coords, tiles)
        # flip tile according to rules
        if flipped and flipped_count not in [1, 2]:
            new_tiles[coords] = False
        elif not flipped and flipped_count == 2:
            new_tiles[coords] = True
            # add neighbours to observered tiles
            for neighbour_coords in neighbours_coords:
                if neighbour_coords not in tiles.keys():
                    new_tiles[neighbour_coords] = False
        else:
            new_tiles[coords] = flipped
            if not flipped:
                # add neighbours to observered tiles
                for neighbour_coords in neighbours_coords:
                    if neighbour_coords not in tiles.keys():
                        new_tiles[neighbour_coords] = False
    return new_tiles


def countFlippedAfterXDays(x, tiles):
    total_flipped_count = 0
    # add neighbours to observered tiles
    new_tiles = tiles.copy()
    for coords, flipped in tiles.items():
        neighbours_coords, flipped_count = getNeighbours(coords, tiles)
        for neighbour_coords in neighbours_coords:
            if neighbour_coords not in tiles.keys():
                new_tiles[neighbour_coords] = False
    # doDailyFlipping for x days
    for i in range(x):
        new_tiles = doDailyFlipping(new_tiles)
    for flipped in new_tiles.values():
        if flipped:
            total_flipped_count += 1
    return total_flipped_count


# for timing
def run():
    # part 2
    part1, start_tiles = filpTiles(rawdata)
    part2 = countFlippedAfterXDays(100, start_tiles)
    print("Part 1:", part1)
    print("Part 2:", part2)


setupcode = """
from __main__ import run
"""

print(timeit.timeit(stmt=run, setup=setupcode, number=1))