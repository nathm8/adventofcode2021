#!/bin/python

import fileinput

def load_data():
    lines = []
    for line in fileinput.input():
        lines.append(line.strip("\n"))
    return lines

def part1():
    opens = ["(", "[", "{", "<"]
    closes = [")", "]", "}", ">"]
    lines = load_data()
    corrupted_chars = []
    for line in lines:
        queue = []
        for c in line:
            if c in opens:
                queue.append(c)
            else:
                if opens[closes.index(c)] != queue[-1]:
                    corrupted_chars.append(c)
                    break
                else:
                    queue.pop()
    points = {")":3, "]":57, "}":1197, ">":25137}
    return sum(map(lambda x: points[x], corrupted_chars))

def part2():
    opens = ["(", "[", "{", "<"]
    closes = [")", "]", "}", ">"]
    lines = load_data()
    incomplete_queues = []
    for line in lines:
        queue = []
        for c in line:
            if c in opens:
                queue.append(c)
            else:
                if opens[closes.index(c)] != queue[-1]:
                    break
                else:
                    queue.pop()
        else:
            incomplete_queues.append(queue)

    points = {"(":1, "[":2, "{":3, "<":4}
    scores = []
    for queue in incomplete_queues:
        score = 0
        while len(queue) > 0:
            score = 5*score + points[queue.pop()]
        scores.append(score)
    return sorted(scores)[int(len(scores)/2)]

if __name__ == '__main__':
    print(part2())
