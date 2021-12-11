#!/bin/python

import fileinput
from functools import reduce

def load_data():
    heightmap = []
    for line in fileinput.input():
        row = []
        for l in line.strip("\n"):
            row.append(int(l))
        heightmap.append(row)
    return heightmap

def neighbours(y, x, height, width):
    for i,j in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
        if i < 0 or i == height or j < 0 or j == width:
            continue
        yield i, j

def part1():
    heightmap = load_data()
    width, height = len(heightmap[0]), len(heightmap)
    lowpoint_indices = []
    for y in range(height):
        for x in range(width):
            lowpoint = True
            for i,j in neighbours(y, x, height, width):
                if heightmap[i][j] <= heightmap[y][x]:
                    lowpoint = False
                    break
            if lowpoint:
                lowpoint_indices.append((y,x))
    risk = 0
    for y,x in lowpoint_indices:
        risk += heightmap[y][x]+1
    return risk

def part2():
    heightmap = load_data()
    width, height = len(heightmap[0]), len(heightmap)
    lowpoint_indices = []
    for y in range(height):
        for x in range(width):
            lowpoint = True
            for i,j in neighbours(y, x, height, width):
                if heightmap[i][j] <= heightmap[y][x]:
                    lowpoint = False
                    break
            if lowpoint:
                lowpoint_indices.append((y,x))

    basins = []
    for lp in lowpoint_indices:
        basins.append({lp})
    for basin in basins:
        frontier = list(basin)
        while len(frontier) > 0:
            y, x = frontier.pop()
            for i, j in neighbours(y, x, height, width):
                if heightmap[i][j] < 9 and not (i,j) in basin:
                    basin.add((i,j))
                    frontier.append((i,j))
    return reduce(lambda x,y: x*y, sorted(map(len, basins))[-3:])

if __name__ == '__main__':
    print(part2())
