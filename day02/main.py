#!/bin/python

import fileinput

def part1():
    horz = 0
    depth = 0

    for line in fileinput.input():
        command, amount = line.split(" ")
        if command == "forward":
            horz += int(amount)
        if command == "down":
            depth += int(amount)
        if command == "up":
            depth -= int(amount)

    return depth*horz

def part2():
    horz = 0
    depth = 0
    aim = 0

    for line in fileinput.input():
        command, amount = line.split(" ")
        if command == "forward":
            horz += int(amount)
            depth += aim*int(amount)
        if command == "down":
            aim += int(amount)
        if command == "up":
            aim -= int(amount)

    return depth*horz    

if __name__ == '__main__':
    print(part2())