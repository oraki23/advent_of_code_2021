 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 9
    part = 1
    result = 0

    mapMer = [ [int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]

    values = []

    for i,valueLine in enumerate(mapMer):
        for j,value in enumerate(valueLine):
            valueIsLowestOfNeighbor = True
            # check 4 directions
            if i > 0:
                if mapMer[i-1][j] <= value:
                    valueIsLowestOfNeighbor = False
            if i < len(mapMer)-1:
                if mapMer[i+1][j] <= value:
                    valueIsLowestOfNeighbor = False
            if j > 0:
                if mapMer[i][j-1] <= value:
                    valueIsLowestOfNeighbor = False
            if j < len(valueLine)-1:
                if mapMer[i][j+1] <= value:
                    valueIsLowestOfNeighbor = False
            if valueIsLowestOfNeighbor:
                result += 1 + value
                values.append((i,j,str(value)))

    print('part ' + str(part) + ': ' + str(result))


def recur_loop(mapMer, mapForBassin, mapForFun, iStart, jStart, iInc, jInc, loopId):
    sentI = iStart + iInc
    sentJ = jStart + jInc

    if (sentJ >= 0 and sentI >= 0 and sentJ < len(mapMer[0]) and sentI < len(mapMer)):
        mapForFun[sentI][sentJ] += 1

    if (sentJ >= 0 and sentI >= 0 and sentJ < len(mapMer[0]) and sentI < len(mapMer)) and mapMer[sentI][sentJ] != 9 and mapForBassin[sentI][sentJ] == -1:
        #print('TRUE')
        #print('start: ' + str(sentI) + ',' + str(sentJ) + ' Loop: ' + str(loopId))
        mapForBassin[sentI][sentJ] = mapMer[sentI][sentJ]

        recur_loop(mapMer, mapForBassin, mapForFun, sentI, sentJ, 0, 1, loopId+1)
        recur_loop(mapMer, mapForBassin, mapForFun, sentI, sentJ, 0, -1, loopId+1)
        recur_loop(mapMer, mapForBassin, mapForFun, sentI, sentJ, 1, 0, loopId+1)
        recur_loop(mapMer, mapForBassin, mapForFun, sentI, sentJ, -1, 0, loopId+1)

    return mapForBassin
def part2():
    day = 9
    part = 2
    result = 1

    mapMer = [ [int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]

    values = []

    for i,valueLine in enumerate(mapMer):
        for j,value in enumerate(valueLine):
            valueIsLowestOfNeighbor = True
            # check 4 directions
            if i > 0:
                if mapMer[i-1][j] <= value:
                    valueIsLowestOfNeighbor = False
            if i < len(mapMer)-1:
                if mapMer[i+1][j] <= value:
                    valueIsLowestOfNeighbor = False
            if j > 0:
                if mapMer[i][j-1] <= value:
                    valueIsLowestOfNeighbor = False
            if j < len(valueLine)-1:
                if mapMer[i][j+1] <= value:
                    valueIsLowestOfNeighbor = False
            if valueIsLowestOfNeighbor:
                values.append((i,j,value))
    
    counts = []
    mapForFun = [False]*len(mapMer)
    for i,line in enumerate(mapForFun):
        mapForFun[i] = [0]*len(mapMer[0])
    for entry in values:
        mapForBassin = [False]*len(mapMer)
        for i,line in enumerate(mapForBassin):
            mapForBassin[i] = [-1]*len(mapMer[0])

        #print(entry)

        iLoc = entry[0]
        jLoc = entry[1]

        # Start from 2,2
        # +1
        mapForBassin[iLoc][jLoc] = mapMer[iLoc][jLoc]
        
        recur_loop(mapMer, mapForBassin, mapForFun, iLoc, jLoc, -1, 0, 0)
        recur_loop(mapMer, mapForBassin, mapForFun, iLoc, jLoc, 1, 0, 0)
        recur_loop(mapMer, mapForBassin, mapForFun, iLoc, jLoc, 0, -1, 0)
        recur_loop(mapMer, mapForBassin, mapForFun, iLoc, jLoc, 0, 1, 0)

        count = 0
        for line in mapForBassin:
            #print(line)
            for item in line:
                if item != -1:
                    count += 1
        counts.append(count)

    counts.sort(reverse=True)
    print(counts[0:3])
    for value in counts[0:3]:
        result *= value

    for line in mapForFun:
        print(line)
        # Go in all 4 directions
        # Do Processing, +1 if not nine.
        # If not nine, continue in all directions except one came from.




        # iLoc = entry[0]
        # jLoc = entry[1]

        # sizeBassin = 1
        # # i +
        # iLoc = entry[0]
        # jLoc = entry[1]

        # iInc = 1

        # sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, iInc, 0)
        # sizeBassin += sizeBassin_to_add
        # print('==========i 0 sizeBassin_to_add: ' + str(sizeBassin_to_add))

        # ifContinue = True
        # while ifContinue:
        #     iLoc += iInc

        #     print(str(iLoc) + ',' + str(jLoc))
        #     if iLoc < 0 or iLoc > len(mapMer)-1 or mapMer[iLoc][jLoc] == 9:
        #         if not (iLoc < 0 or iLoc > len(mapMer)-1):
        #             sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, iInc, 0)
        #             sizeBassin += sizeBassin_to_add
        #             print('============i- sizeBassin_to_add: ' + str(sizeBassin_to_add))
        #         ifContinue = False

        #     if ifContinue:
        #         sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, iInc, 0)
        #         sizeBassin += sizeBassin_to_add
        #         print('=============i+ sizeBassin_to_add: ' + str(sizeBassin_to_add))


        # # i -
        # iLoc = entry[0]
        # jLoc = entry[1]
        # iInc = -1

        # ifContinue = True
        # while ifContinue:
        #     iLoc += iInc

        #     print(str(iLoc) + ',' + str(jLoc))
        #     if iLoc < 0 or iLoc > len(mapMer)-1 or mapMer[iLoc][jLoc] == 9:
        #         if not (iLoc < 0 or iLoc > len(mapMer)-1):
        #             sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, iInc, 0)
        #             sizeBassin += sizeBassin_to_add
        #             print('============i- sizeBassin_to_add: ' + str(sizeBassin_to_add))
        #         ifContinue = False

        #     if ifContinue:
        #         sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, iInc, 0)
        #         sizeBassin += sizeBassin_to_add
        #         print('============i- sizeBassin_to_add: ' + str(sizeBassin_to_add))



        # # j -
        # iLoc = entry[0]
        # jLoc = entry[1]
        #sizeBassin += recursive_loop(mapMer, iLoc, jLoc, 0, -1)

        # i+,j+
        # iLoc = entry[0]
        # jLoc = entry[1]
        # ifContinue = True
        # while ifContinue:
        #     iLoc += 1
        #     jLoc += 1

        #     if jLoc > len(mapMer)-1 or iLoc > len(mapMer)-1 or mapMer[iLoc][jLoc] == 9 or (mapMer[iLoc-1][jLoc] == 9 and mapMer[iLoc][jLoc-1] == 9):
        #         ifContinue = False

        #     if ifContinue:
        #         print('sizeBassin + 1 (i+,j+)')
        #         sizeBassin += 1
        # i+,j-
        # iLoc = entry[0]
        # jLoc = entry[1]
        # ifContinue = True
        # while ifContinue:
        #     iLoc += 1
        #     jLoc -= 1

        #     if jLoc < 0 or iLoc > len(mapMer)-1 or mapMer[iLoc][jLoc] == 9 or (mapMer[iLoc-1][jLoc] == 9 and mapMer[iLoc][jLoc+1] == 9):
        #         ifContinue = False

        #     if ifContinue:
        #         print('sizeBassin + 1 (i+,j-)')
        #         sizeBassin += 1

        # i-,j+
        # iLoc = entry[0]
        # jLoc = entry[1]
        # ifContinue = True
        # while ifContinue:
        #     iLoc -= 1
        #     jLoc += 1

        #     if jLoc > len(mapMer)-1 or iLoc < 0 or mapMer[iLoc][jLoc] == 9 or (mapMer[iLoc+1][jLoc] == 9 and mapMer[iLoc][jLoc-1] == 9):
        #         ifContinue = False

        #     if ifContinue:
        #         print('sizeBassin + 1 (i-,j+)')
        #         sizeBassin += 1

        # i-,j-
        # iLoc = entry[0]
        # jLoc = entry[1]
        # ifContinue = True
        # while ifContinue:
        #     iLoc -= 1
        #     jLoc -= 1

        #     if jLoc < 0 or iLoc < 0 or mapMer[iLoc][jLoc] == 9 or (mapMer[iLoc+1][jLoc] == 9 and mapMer[iLoc][jLoc+1] == 9):
        #         ifContinue = False

        #     if ifContinue:
        #         print('sizeBassin + 1 (i-,j-)')
        #         sizeBassin += 1

        # if sizeBassin > 0:
        #     print('=====================SIZE BASSIN: ' + str(sizeBassin))
        #     result *= sizeBassin

    print('part ' + str(part) + ': ' + str(result))

def recursive_loop(mapMer, iStart, jStart, iInc, jInc):
    sizeBassin = 0

    #print('start: ' + str(iStart) + ',' + str(jStart))
    iLoc = iStart
    jLoc = jStart
    ifContinue = True

    # Do it with starting point
    if iInc != 0:
        sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, 0, 1)
        sizeBassin += sizeBassin_to_add
        print('rec 1 sizeBassin_to_add: ' + str(sizeBassin_to_add))

        sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, 0, -1)
        sizeBassin += sizeBassin_to_add
        print('rec 2 sizeBassin_to_add: ' + str(sizeBassin_to_add))
    else: 
        while ifContinue:
            iLoc += iInc
            jLoc += jInc

            print(str(iLoc) + ',' + str(jLoc))
            if jLoc < 0 or iLoc < 0 or jLoc > len(mapMer[0])-1 or iLoc > len(mapMer)-1 or mapMer[iLoc][jLoc] == 9:
                ifContinue = False

            if ifContinue:
                print('(i ' + str(formatInc(iInc)) + ',j ' + str(formatInc(jInc)) + ',v ' + str(mapMer[iLoc][jLoc]) + ')')
                sizeBassin += 1
            
            # if iInc != 0 and ifContinue:
            #     sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, 0, 1)
            #     sizeBassin += sizeBassin_to_add
            #     print('rec 1 sizeBassin: ' + str(sizeBassin))

            #     sizeBassin_to_add = recursive_loop(mapMer, iLoc, jLoc, 0, -1)
            #     sizeBassin += sizeBassin_to_add
            #     print('rec 2 sizeBassin: ' + str(sizeBassin))

    
    if sizeBassin > 0:
        print('sizeBassin: ' + str(sizeBassin))
    return sizeBassin

def findInc(number):
    if number >= 0:
        return 1
    else:
        return -1
    
def formatInc(number):
    if number == 0:
        return 0 
    elif number > 0:
        return 1
    else:
        return -1

def findAdd(number):
    if number == 0:
        return 0 
    elif number > 0:
        return 1
    else:
        return -1

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
