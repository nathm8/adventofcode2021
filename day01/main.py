#!/bin/python

import fileinput

def process(depths):
    increases = 0
    prev = None

    for d in depths:
        if not prev is None and d > prev: 
            increases += 1
        prev = d
    return increases

def part1():
    depths = []
    for line in fileinput.input():
        depths.append(int(line))
    return process(depths)

def part2():
    prev1 = None
    prev2 = None
    windows = []
    for line in fileinput.input():
        d = int(line)
        if not (prev1 is None or prev2 is None):
            windows.append(d + prev1 + prev2)
        prev2 = prev1
        prev1 = d
    return process(windows)

if __name__ == '__main__':
    print(part2())