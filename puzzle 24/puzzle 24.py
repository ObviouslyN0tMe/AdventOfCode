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
        coords = [0, 0]
        # count directions
        ne_count = instruction.count("ne")
        nw_count = instruction.count("nw")
        se_count = instruction.count("se")
        sw_count = instruction.count("sw")
        e_count = instruction.count("e") - ne_count - se_count
        w_count = instruction.count("w") - nw_count - sw_count
        # x-coord
        coords[0] += e_count + 0.5 * (ne_count + se_count)
        coords[0] -= w_count + 0.5 * (nw_count + sw_count)
        # y-coord
        coords[1] += 0.5 * (ne_count + nw_count)
        coords[1] -= 0.5 * (se_count + sw_count)
        # flip tile
        coords = tuple(coords)
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
    # calc all neighbours coords
    neighbours_coords = [(coords[0] + 1, coords[1]), (coords[0] - 1, coords[1])]
    for x, y in [(-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5), (0.5, 0.5)]:
        neighbours_coords.append((coords[0] + x, coords[1] + y))
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
        else:
            new_tiles[coords] = flipped
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
    tiles = new_tiles.copy()
    # doDailyFlipping for x days
    for i in range(x):
        new_tiles = doDailyFlipping(tiles)
        tiles = new_tiles.copy()
    for flipped in tiles.values():
        if flipped:
            total_flipped_count += 1
    return total_flipped_count


part1, start_tiles = filpTiles(rawdata)
part2 = countFlippedAfterXDays(100, start_tiles)
print("Part 1:", part1)
print("Part 2:", part2)
