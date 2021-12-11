#!/bin/python

import fileinput
from copy import copy

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dirc(self, other):
        x_dirc = other.x-self.x
        if x_dirc > 0: x_dirc = 1
        if x_dirc < 0: x_dirc = -1
        y_dirc = other.y-self.y
        if y_dirc > 0: y_dirc = 1
        if y_dirc < 0: y_dirc = -1
        return Point(x_dirc, y_dirc)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self):
        return "P("+str(self.x)+","+str(self.y)+")"

class Line():
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.partOneIgnore = False#not (self.u.x == self.v.x or self.u.y == self.v.y)

    def getMaxDimension(self):
        return max(self.u.x, self.v.x, self.u.y, self.v.y)

    def getPoints(self):
        step = copy(self.u)
        dirc = self.u.dirc(self.v)
        while step != self.v:
            yield step
            step += dirc
        yield step

    def __str__(self):
        return "L("+str(self.u)+","+str(self.v)+")"

def load_data():
    lines = []
    max_dimension = 0
    for line in fileinput.input():
        p1, p2 = line.strip("\n").split(" -> ")
        l = Line(Point(*map(int, p1.split(","))), Point(*map(int, p2.split(","))))
        lines.append(l)
        d = l.getMaxDimension()
        if d > max_dimension:
            max_dimension = d
    return lines, max_dimension+1

def part1():
    lines, max_dimension = load_data()
    overlap = [ [0]*max_dimension for i in range(max_dimension)]

    for line in lines:
        if line.partOneIgnore: continue
        for p in line.getPoints():
            overlap[p.y][p.x] += 1
    
    # for x in range(max_dimension):
    #     print(overlap[x])

    overlap = [item for sublist in overlap for item in sublist]
    overlap = list(filter(lambda x: x > 1, overlap))
    return len(overlap)

def part2():
    pass

if __name__ == '__main__':
    print(part1())