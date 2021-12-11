 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 11
    part = 1
    result = 0

    entries = [[int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]
    #print(entries)


    #print(octoFlashed)

    steps_count = 100

    for step in range(steps_count):
        octoFlashed = [False]*len(entries)
        for i,line in enumerate(octoFlashed):
            octoFlashed[i] = [0]*len(entries[0])

        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                entries[i][j] += 1
        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                flash_octopus(i,j, octoFlashed, entries, 0)
        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                if octoFlashed[i][j] == 1:
                    entries[i][j] = 0
        
        for flashLine in octoFlashed:
            for flash in flashLine:
                if flash == 1:
                    result += 1
        #print_beautiful(entries)
        #print()
    #print_beautiful(octoFlashed)
    #print()
    #print_beautiful(entries)

    print('part ' + str(part) + ': ' + str(result))

def print_beautiful(double_entry):
    for line in double_entry:
        print(line)


def flash_octopus(i,j, octoFlashed, entries, inc):
    entries[i][j] += inc
    if entries[i][j] > 9 and octoFlashed[i][j] == 0:
        octoFlashed[i][j] = 1

        canPlusOneI = i+1 < len(entries)
        canPlusOneJ = j+1 < len(entries[0])
        canMinusOneI = i-1 >= 0
        canMinusOneJ = j-1 >= 0

        # i+
        if canPlusOneI:
            flash_octopus(i+1,j, octoFlashed, entries, 1)
        # i-
        if canMinusOneI:
            flash_octopus(i-1,j, octoFlashed, entries, 1)
        # j+
        if canPlusOneJ:
            flash_octopus(i,j+1, octoFlashed, entries, 1)        
        # j-
        if canMinusOneJ:
            flash_octopus(i,j-1, octoFlashed, entries, 1)        
        # i+ j+
        if canPlusOneI and canPlusOneJ:
            flash_octopus(i+1,j+1, octoFlashed, entries, 1)        

        # i- j+
        if canMinusOneI and canPlusOneJ:
            flash_octopus(i-1,j+1, octoFlashed, entries, 1)        

        # i+ j-
        if canPlusOneI and canMinusOneJ:
            flash_octopus(i+1,j-1, octoFlashed, entries, 1)        

        # i- j-
        if canMinusOneI and canMinusOneJ:
            flash_octopus(i-1,j-1, octoFlashed, entries, 1)        


def part2():
    day = 11
    part = 2
    result = 0

    entries = [[int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]
    #print(entries)


    #print(octoFlashed)

    steps_count = 30001

    for step in range(steps_count):
        octoFlashed = [False]*len(entries)
        for i,line in enumerate(octoFlashed):
            octoFlashed[i] = [0]*len(entries[0])

        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                entries[i][j] += 1
        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                flash_octopus(i,j, octoFlashed, entries, 0)
        for i,octopusLine in enumerate(entries):
            for j,octopus in enumerate(octopusLine):
                if octoFlashed[i][j] == 1:
                    entries[i][j] = 0
        
        total = 0
        for flashLine in octoFlashed:
            for flash in flashLine:
                if flash == 1:
                    total += 1
        if total == (len(octoFlashed) * len(octoFlashed[0])):
            print('HERE')
            result = step+1
            break
        #print_beautiful(entries)
        #print()
    print_beautiful(octoFlashed)
    print()
    print_beautiful(entries)

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
