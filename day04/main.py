#!/bin/python

import fileinput

def load_data():
    numbers = []
    boards = []
    tmp = []
    for line in fileinput.input():
        if fileinput.lineno() < 3:
            if fileinput.lineno() == 1:
                numbers = list(map(int, line.strip("\n").split(",")))
        else:
            tmp.extend(list(map(int, filter(lambda x: x!="",line.strip("\n").split(" ")))))
            if len(tmp) == 25:
                boards.append(BingoBoard(tmp))
                tmp = []
    return numbers, boards

class BingoBoard():

    def __init__(self, numbers):
        self.numbers = numbers
        self.called = [False]*25
        self.has_won = False

    def getRow(self, i):
        row = []
        for j in range(5):
            row.append(self.called[i*5+j])
        return row

    def getCol(self, j):
        col = []
        for i in range(5):
            col.append(self.called[i*5+j])
        return col

    def victoryCheck(self):
        # prevent reporting twice
        if self.has_won: return False 
        for i in range(5):
            if all(self.getRow(i)) or all(self.getCol(i)):
                self.has_won = True
                return True
        return False

    def getScore(self):
        return sum(self.numbers)

    def markNumber(self, x):
        if self.numbers.count(x) == 0: return
        i = self.numbers.index(x)
        self.numbers[i] = 0
        self.called[i] = True

    def __str__(self):
        out = ""
        i = 0
        j = 0
        for n in self.numbers:
            called = self.called[j]
            if called:
                out += " X "
            else:
                out += str(n).rjust(2," ")+" "
            i += 1
            j += 1
            if i == 5:
                out += "\n"
                i = 0
        return out

def part1():
    numbers, boards = load_data()
    for n in numbers:
        for b in boards:
            b.markNumber(n)
            if (b.victoryCheck()):
                return b.getScore()*n

def part2():
    numbers, boards = load_data()
    winning_boards = 0
    last_board_to_win = None
    for n in numbers:
        for b in boards:
            b.markNumber(n)
            if (b.victoryCheck()):
                winning_boards += 1;
                last_board_to_win = b
        if winning_boards == len(boards):
            return last_board_to_win.getScore()*n

if __name__ == '__main__':
    print(part2())