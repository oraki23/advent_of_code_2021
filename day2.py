
from os import read

def part1():
    day = 2
    part = 1

    horizontal_position = 0
    depth = 0

    movements = [{'operation': entry[:len(entry)-2], 'value': int(entry[len(entry)-1:])} for entry in list(readFile(day).split('\n'))]

    for move in movements:
        if move['operation'] == "forward":
            horizontal_position += move['value']
        elif move['operation'] == "down":
            depth += move['value']
        elif move['operation'] == "up":
            depth -= move['value']

    result = depth * horizontal_position

    print('part ' + str(part) + ': ' + str(result))

def part2():
    day = 2
    part = 2

    horizontal_position = 0
    depth = 0
    aim = 0

    movements = [{'operation': entry[:len(entry)-2], 'value': int(entry[len(entry)-1:])} for entry in list(readFile(day).split('\n'))]

    for move in movements:
        if move['operation'] == "forward":
            horizontal_position += move['value']
            depth += aim * move['value']
        elif move['operation'] == "down":
            aim += move['value']
        elif move['operation'] == "up":
            aim -= move['value']

    result = depth * horizontal_position

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()