#!/bin/python

import fileinput

def load_data():
    data = []
    for line in fileinput.input():
        data.append(line.strip("\n"))
    return data


def process(binaries):
    ones = []
    zeroes = []
    init = False

    for line in binaries:
        if not init:
            for _ in range(len(line)):
                ones.append(0)
                zeroes.append(0)
            init = True
        for i in range(len(line)):
            char = line[i]
            if char == "1":
                ones[i] += 1
            else:
                zeroes[i] += 1
    return ones, zeroes

def part1():
    ones, zeroes = process(load_data())

    gamma = ""
    epsilon = ""
    for i in range(len(ones)):
        if ones[i] > zeroes[i]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma*epsilon

def part2():
    binaries = load_data()

    oxygen = binaries.copy()
    carbon = binaries.copy()
    for i in range(len(oxygen[0])):
        ones, zeroes = process(oxygen)
        oxy = "1" if ones[i] >= zeroes[i] else "0"
        ones, zeroes = process(carbon)
        car = "0" if ones[i] >= zeroes[i] else "1"

        if len(oxygen) > 1:
            oxygen = list(filter(lambda x: x[i]==oxy, oxygen))
        if len(carbon) > 1:
            carbon = list(filter(lambda x: x[i]==car, carbon))
            
    oxygen = int(oxygen[0], 2)
    carbon = int(carbon[0], 2)
    return carbon*oxygen

if __name__ == '__main__':
    print(part2())