 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 12
    part = 1
    result = 0

    entries = [(line.split('-')[0],line.split('-')[1]) for line in readFile(day).split('\n')]
    #print(entries)

    connections = {}

    for i,connection in enumerate(entries):
        #print(connection[0])

        if connection[0] in connections:
            connections[connection[0]].append(connection[1])
        else:
            connections[connection[0]] = [connection[1]]

        if connection[1] in connections:
            connections[connection[1]].append(connection[0])
        else:
            connections[connection[1]] = [connection[0]]

    #print(connections)

    paths = []

    followPath(paths, connections, 'start', [])

    #print(paths)
    result = len(paths)


    print('part ' + str(part) + ': ' + str(result))

def followPath(paths, connections, start_path, current_path):
    #print('received current path: ' + str(current_path) + ' - start_path: ' + str(start_path))
    if start_path == 'end':
        paths.append(current_path)
    
    if start_path in ['start', 'end'] or start_path.islower():
        if start_path in current_path:
            return current_path
    current_path.append(start_path)
    #print(current_path)
    for way in connections[start_path]:
        new_path = current_path.copy()
        if 'end' not in new_path:
            new_path = followPath(paths, connections, way, new_path)
    return new_path

def print_beautiful(double_entry):
    for line in double_entry:
        print(line)


def part2():
    day = 12
    part = 2
    result = 0

    entries = [(line.split('-')[0],line.split('-')[1]) for line in readFile(day).split('\n')]
    #print(entries)

    connections = {}

    for i,connection in enumerate(entries):
        #print(connection[0])

        if connection[0] in connections:
            connections[connection[0]].append(connection[1])
        else:
            connections[connection[0]] = [connection[1]]

        if connection[1] in connections:
            connections[connection[1]].append(connection[0])
        else:
            connections[connection[1]] = [connection[0]]

    #print(connections)

    paths = []

    followPath_2(paths, connections, 'start', [], '')

    #print(paths)
    result = len(paths)

    print('part ' + str(part) + ': ' + str(result))

def followPath_2(paths, connections, start_path, current_path, double_visited_small_cave):
    #print('received current path: ' + str(current_path) + ' - start_path: ' + str(start_path))
    if start_path == 'end':
        paths.append(current_path)
    
    if start_path in ['start', 'end']:
        if start_path in current_path:
            return current_path
    if start_path.islower() and start_path in current_path:
        if double_visited_small_cave == '':
            double_visited_small_cave = start_path
        else:
            return current_path

    current_path.append(start_path)
    #print(current_path)
    for way in connections[start_path]:
        new_path = current_path.copy()
        if 'end' not in new_path:
            new_path = followPath_2(paths, connections, way, new_path, double_visited_small_cave)
    return new_path

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
