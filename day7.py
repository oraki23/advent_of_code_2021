 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 7
    part = 1
    result = 0

    hor_pos = [int(pos) for pos in readFile(day).split(',')]

    less_fuel = 100000000
    for i in range(max(hor_pos)):
        total_fuel = 0
        for pos in hor_pos:
            total_fuel += abs(i - pos)
        less_fuel = min(less_fuel, total_fuel)

    result = less_fuel

    print('part ' + str(part) + ': ' + str(result))

def part2():
    day = 7
    part = 2
    result = 0

    hor_pos = [int(pos) for pos in readFile(day).split(',')]

    less_fuel = 100000000
    for i in range(max(hor_pos)):
        total_fuel = 0
        for pos in hor_pos:
            diff_pos = abs(i - pos)
            total_fuel += int((diff_pos * (diff_pos+1)) / 2.0)
        less_fuel = min(less_fuel, total_fuel)

    result = less_fuel

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()