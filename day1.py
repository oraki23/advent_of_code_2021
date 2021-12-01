
from os import read

def part1():
    day = 1
    part = 1
    measurements = list(map(int, readFile(day).split('\n')))

    count_increased = 0
    for i, measure in enumerate(measurements):
        if i != 0:
            diff = measure - measurements[i-1]
            if diff > 0:
                count_increased += 1

    print('part ' + str(part) + ': ' + str(count_increased))

def part2():
    day = 1
    part = 2
    measurements = list(map(int, readFile(day).split('\n')))

    count_increased = 0
    for i, measure in enumerate(measurements):
        if len(measurements) > i+3:
            window1 = measure + measurements[i+1] + measurements[i+2]
            window2 = measurements[i+1] + measurements[i+2] + measurements[i+3]

            diff = window2 - window1
            if diff > 0:
                count_increased += 1

    print('part ' + str(part) + ': ' + str(count_increased))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()