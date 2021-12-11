#!/bin/python

import fileinput

def load_data():
    
    for line in fileinput.input():
        positions = list(map(int,line.strip("\n").split(",")))
    return positions

def part1():
    positions = load_data()
    dists = []
    for p in positions:
        dist = 0
        for p2 in positions:
            if p == p2: continue
            dist += abs(p-p2)
        dists.append(dist)
    return min(dists)

def triangle_number(n):
    return sum(range(n+1))

def part2():
    positions = load_data()
    dists = []
    for p in range(max(positions)):
        dist = 0
        for p2 in positions:
            if p == p2: continue
            dist += triangle_number(abs(p-p2))
        dists.append(dist)
    return min(dists)


if __name__ == '__main__':
    print(part2())