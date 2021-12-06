 
from os import read
from collections import Counter
import re

def part1():
    day = 6
    part = 1
    result = 0

    numberOfDays = 80

    fishes = [int(fish) for fish in readFile(day).split(',')]

    for i in range(numberOfDays):
        fishesToAdd = 0
        for x,fish in enumerate(fishes):
            if fish > 0:
                fishes[x] -= 1
            else:
                fishes[x] = 6
                fishesToAdd += 1
        for f in range(fishesToAdd):
            fishes.append(8)
        #print(fishes)

    result = len(fishes)

    print('part ' + str(part) + ': ' + str(result))

def part2():
    day = 6
    part = 2
    result = 0

    numberOfDays = 256

    nbOfFishesByReproductionDay = [0]*9

    for fish in readFile(day).split(','):
        nbOfFishesByReproductionDay[int(fish)] += 1

    for reproductionDay,count in enumerate(nbOfFishesByReproductionDay):
        print(str(reproductionDay) + ' : ' + str(count))
    
    for x in range(numberOfDays):
        nbOfFishesByReproductionDayTemp = [0]*9
        for i,count in enumerate(nbOfFishesByReproductionDay):
            # Move the fishes count on day earlier
            if i == 0:
                nbOfFishesByReproductionDayTemp[6] = count
                nbOfFishesByReproductionDayTemp[8] = count
            else:
                nbOfFishesByReproductionDayTemp[i-1] += count
        
        for reproductionDay,count in enumerate(nbOfFishesByReproductionDay):
            nbOfFishesByReproductionDay[reproductionDay] = nbOfFishesByReproductionDayTemp[reproductionDay]

    for reproductionDay,count in enumerate(nbOfFishesByReproductionDay):
        print(str(reproductionDay) + ' : ' + str(count))
        result += count
  
    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()