 
from heapq import heappop, heappush
from os import read
from collections import Counter
import re
import math
import time

def part1():
    day = 15
    part = 1
    result = 0
    
    entries = [[int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]

    values = [-1]*len(entries)
    for i,line in enumerate(values):
        values[i] = [100000000]*len(entries[0])

    # set vaue of 0 for node
    values[0][0] = 0

    for x,line in enumerate(entries):
        for y, entry in enumerate(entries[x]):
            canPlusOneX = x+1 < len(entries)
            canPlusOneY = y+1 < len(entries[0])
            canMinusOneX = x-1 >= 0
            canMinusOneY = y-1 >= 0

            if canPlusOneX:
                potential_value = values[x][y] + entries[x+1][y]
                values[x+1][y] = min(values[x+1][y], potential_value)
            if canPlusOneY:
                potential_value = values[x][y] + entries[x][y+1]
                values[x][y+1] = min(values[x][y+1], potential_value)
            if canMinusOneX:
                potential_value = values[x][y] + entries[x-1][y]
                values[x-1][y] = min(values[x-1][y], potential_value)
            if canMinusOneY:
                potential_value = values[x][y] + entries[x][y-1]
                values[x][y-1] = min(values[x][y-1], potential_value)                
                

    #print_beautiful(values, len(values), len(values[0]))


    result = values[-1][-1]

    print('part ' + str(part) + ': ' + str(result))


def print_beautiful(double_entry, max_x, max_y):
    result = 0
    for x in range(max_x):
        for y in range(max_y):
            print(str(double_entry[x][y]), end='|')
        print()
    return result

def part2():
    day = 15
    part = 2
    result = 0

    entries = [[int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]
    entries_2 = []

    # Add the values
    for x,line in enumerate(entries):
        new_line = [-1]*len(entries)*5
        for y, entry in enumerate(entries[x]):
            new_line[y] = entries[x][y]
            new_line[y+len(entries)*1] = entries[x][y] + 1 if entries[x][y] + 1 < 10 else entries[x][y] + 1 - 9
            new_line[y+len(entries)*2] = entries[x][y] + 2 if entries[x][y] + 2 < 10 else entries[x][y] + 2 - 9
            new_line[y+len(entries)*3] = entries[x][y] + 3 if entries[x][y] + 3 < 10 else entries[x][y] + 3 - 9
            new_line[y+len(entries)*4] = entries[x][y] + 4 if entries[x][y] + 4 < 10 else entries[x][y] + 4 - 9

        entries_2.append(new_line.copy())

    entries_4 = []
    #print_beautiful(entries_3, len(entries_3), len(entries_3[0]))
    for i in range(5):
        entries_3 = []
        for x,line in enumerate(entries_2):
            new_line = entries_2[x].copy()

            for y, entry in enumerate(entries_2[x]):
                new_line[y] = entries_2[x][y] + i if entries_2[x][y] + i < 10 else entries_2[x][y] + i - 9

            entries_3.append(new_line.copy())
            #print()
            #print_beautiful(entries_3, len(entries_3), len(entries_3[0]))
        
        for line in entries_3:
            entries_4.append(line.copy())

    #print()
    #print_beautiful(entries_4, len(entries_4), len(entries_4[0]))

    entries = entries_4
    values = [-1]*len(entries)
    for i,line in enumerate(values):
        values[i] = [10000000000]*len(entries[0])

    un_visited_nodes = []

    for x,line in enumerate(entries):
        for y, entry in enumerate(entries[x]):
            un_visited_nodes.append((values[x][y],(x,y)))

    # set vaue of 0 for node
    values[0][0] = 0

    # Problem was that you need to start always from the lowest node!
    while un_visited_nodes:
        value, (x,y) = heappop(un_visited_nodes)
        #print(value, (x,y))
        start = time.time()

        canPlusOneX = x+1 < len(entries)
        canPlusOneY = y+1 < len(entries[0])
        canMinusOneX = x-1 >= 0
        canMinusOneY = y-1 >= 0

        if canPlusOneX:
            potential_value = values[x][y] + entries[x+1][y]
            if potential_value < values[x+1][y]:
                values[x+1][y] = potential_value
                heappush(un_visited_nodes, (values[x+1][y],(x+1,y)))
        if canPlusOneY:
            potential_value = values[x][y] + entries[x][y+1]
            if potential_value < values[x][y+1]:
                values[x][y+1] = potential_value
                heappush(un_visited_nodes, (values[x][y+1],(x,y+1)))
        if canMinusOneX:
            potential_value = values[x][y] + entries[x-1][y]
            if potential_value < values[x-1][y]:
                values[x-1][y] = potential_value
                heappush(un_visited_nodes, (values[x-1][y],(x-1,y)))
        if canMinusOneY:
            potential_value = values[x][y] + entries[x][y-1]
            if potential_value < values[x][y-1]:
                values[x][y-1] = potential_value
                heappush(un_visited_nodes, (values[x][y-1],(x,y-1)))      



        end = time.time()
        #print('location: ' + str(x) + ',' + str(y) + " done in: " + str(end-start))

    #print(values[0])
    #print(values[1])

    #print_beautiful(values, len(values), len(values[0]))


    result = values[-1][-1]

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
