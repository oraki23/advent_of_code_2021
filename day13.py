 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 13
    part = 1
    result = 0

    entries = [line for line in readFile(day).split('\n\n')]
    marked_dots = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in entries[0].split('\n')]

    fold_along = [ (x.split('=')[0][-1], int(x.split('=')[1])) for x in 
                    [line for line in entries[1].split('\n')] ]
    #print(marked_dots)
    #print(fold_along)

    for fold_instr in fold_along:
        fold_paper(marked_dots, fold_instr[0], fold_instr[1])

    max_x = max(marked_dots,key=lambda item:item[0])[0]+1
    max_y = max(marked_dots,key=lambda item:item[1])[1]+1
    result = print_beautiful(marked_dots, max_x, max_y)

    result = calculate_result(marked_dots, max_x, max_y)

    print('part ' + str(part) + ': ' + str(result))

def calculate_result(double_entry, max_x, max_y):
    result = 0
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) in double_entry:
                result += 1
    return result

def print_beautiful(double_entry, max_x, max_y):
    result = 0
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) in double_entry:
                result += 1
                print('#', end='')
            else:
                print('.', end='')
        print()
    return result

def fold_paper(paper, axis, new_max):
    # axis defines a max we can go.
    
    # if we go above this max, we go:
    # (value - max)
    if axis == 'y':
        for i,coor in enumerate(paper):
            if coor[1] > new_max:
                new_coor = coor[1] - ((coor[1] - new_max)*2)
                paper[i] = (coor[0], new_coor)
    elif axis == 'x':
        for i,coor in enumerate(paper):
            if coor[0] > new_max:
                new_coor = coor[0] - ((coor[0] - new_max)*2)
                paper[i] = (new_coor, coor[1])



def part2():
    day = 13
    part = 2
    result = 0

    #entries = [(line.split('-')[0],line.split('-')[1]) for line in readFile(day).split('\n')]
    #print(entries)


    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
