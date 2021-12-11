#!/bin/python

import fileinput

def load_data():
    
    for line in fileinput.input():
        fishes = list(map(int,line.strip("\n").split(",")))
    fish_map = {x: 0 for x in range(9)}
    for fish in fishes:
        fish_map[fish] += 1
    return fish_map

def part1():
    fishes = load_data()
    for _ in range(256):
        new_fishes = {x: 0 for x in range(9)}
        for age, count in fishes.items():
            if age == 0:
                new_fishes[8] += count
                new_fishes[6] += count
            else:
                new_fishes[age-1] += count
        fishes = new_fishes
    return sum(fishes.values())

if __name__ == '__main__':
    print(part1())