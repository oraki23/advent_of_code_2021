 
from os import read
from collections import Counter
import re
import math
import time

def part1():
    day = 14
    part = 1
    result = 0
    
    nbSteps = 40

    entries = [line for line in readFile(day).split('\n\n')]
    transformations = [(line.split(' -> ')[0], line.split(' -> ')[1]) for line in entries[1].split('\n')]
    starting_entry = entries[0]

    print(starting_entry)

    groups = {}

    for i,x in enumerate(starting_entry):
        if i+1 < len(starting_entry):
            pair = str(starting_entry[i]) + str(starting_entry[i+1])
            if pair in groups:
                groups[pair] += 1
            else:
                groups[pair] = 1

    for a in range(nbSteps):
        start = time.time()
        newGroups = groups.copy()
        for j,value in enumerate(groups):
            # execute as many time (if 0, none)

            for transformation in transformations:
                if transformation[0] == value:
                    #print('newGroups[' + str(value) + '] = ' + str(newGroups[value]))
                    if newGroups[value] > 0:
                        newGroups[value] -= (1 * groups[value])
                    #print('newGroups[' + str(value) + '] = ' + str(newGroups[value]))

                    #print('value: ' + value)
                    #print('transformation[1] ' + transformation[1])
                    new_value_1 = value[0] + transformation[1]
                    #print('new value 1: ' + str(new_value_1))
                    new_value_2 = transformation[1] + value[1]
                    #print('new value 2: ' + str(new_value_2))

                    if new_value_1 in newGroups:
                        newGroups[new_value_1] += (1 * groups[value])
                    else:
                        newGroups[new_value_1] = (1 * groups[value])
                    #print('newGroups[' + str(new_value_1) + '] = ' + str(newGroups[new_value_1]))
                
                    if new_value_2 in newGroups:
                        newGroups[new_value_2] += (1 * groups[value])
                    else:
                        newGroups[new_value_2] = (1 * groups[value])
                    #print('newGroups[' + str(new_value_2) + '] = ' + str(newGroups[new_value_2]))
                    break

        groups = newGroups

        end = time.time()
        print('Step no: ' + str(a+1) + " done in: " + str(end-start))


    count_nb_of_char = {}

    for i,b in enumerate(groups):
        char_1 = b[0]
        char_2 = b[1]
        #if b[0] == b[1] and b[0] == 'B':
        # print(b[0])
        # print(b[1])
        # print()

        if char_1 in count_nb_of_char:
            count_nb_of_char[char_1] += (1 * groups[b])
        else:
            count_nb_of_char[char_1] = (1 * groups[b])

        if char_2 in count_nb_of_char:
            count_nb_of_char[char_2] += (1 * groups[b])
        else:
            count_nb_of_char[char_2] = (1 * groups[b])            

    print(count_nb_of_char['B'])

    for i,b in enumerate(count_nb_of_char):
        count_nb_of_char[b] = math.floor(count_nb_of_char[b] / 2)

    partial = []
    partial.append(starting_entry[0])
    partial.append(starting_entry[-1])
    for letter in partial:
        if letter in count_nb_of_char:
            count_nb_of_char[letter] += 1
        else:
            count_nb_of_char[letter] = 1    

    print(count_nb_of_char)

    result = max(count_nb_of_char.values()) - min(count_nb_of_char.values())

    print('part ' + str(part) + ': ' + str(result))


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

def part2():
    day = 14
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
