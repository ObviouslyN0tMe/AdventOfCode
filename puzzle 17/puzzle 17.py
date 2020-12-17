# puzzle input
with open("puzzle input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
# test input
with open("test input") as file:
    testdata = [x.strip("\n") for x in file.readlines()]

import itertools


def formatData(data):
    cubes = {}
    size = len(data)
    if size // 2 != 0:
        data.append(size*".")
    for index_l, line in enumerate(data):
        if size // 2 != 0:
            line += "."
        for index_c, cube in enumerate(line):
            cubes[-index_l + size//2, index_c - size//2, 0] = True if cube == "#" else False
    return cubes


def findNeighbours(position):
    directions = [x for x in itertools.product([-1, 0, 1], repeat=3)]
    directions.remove((0, 0, 0))
    neighbours = []
    for direction in directions:
        n1 = position[0] + direction[0]
        n2 = position[1] + direction[1]
        n3 = position[2] + direction[2]
        neighbours.append((n1, n2, n3))
    return neighbours


def countNeighbours(position, copy, cubes):
    count = 0
    neighbours = findNeighbours(position)
    for neighbour in neighbours:
        if neighbour in copy:
            if copy[neighbour]:
                count += 1
        else:
            cubes[neighbour] = False
    return count, cubes


def doCycles(cubes, count):
    for cycle in range(0, count, 1):
        copy = cubes.copy()
        for position, state in copy.items():
            neighbours, cubes = countNeighbours(position, copy, cubes)
            if neighbours == 3 or (state and neighbours == 2):
                cubes[position] = True
            else:
                cubes[position] = False
        print(len(cubes))
    return cubes


def countActiveCubes(cubes):
    active = 0
    for state in cubes.values():
        if state:
            active += 1
    return active


cubes = formatData(testdata)
cubes = doCycles(cubes, 1)
print(countActiveCubes(cubes))
