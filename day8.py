 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 8
    part = 1
    result = 0

    mapNbToNbSegment = [6,2,5,5,4,5,6,3,7,6]
    mapNbToNbSegment = [-1,2,-1,-1,4,-1,-1,3,7,-1]

    entries = [(entry[0].strip().split(' '),entry[1].strip().split(' ')) for entry in 
                [line.split('|') for line in readFile(day).split('\n')]]

    #print(entries)

    for i in map(lambda x: x[1], entries):
        for digit in i:
            number = -1
            nbOfLetters = len(digit)
            if nbOfLetters in mapNbToNbSegment:
                number = mapNbToNbSegment.index(nbOfLetters)
            
            if number == 1 or number == 4 or number == 7 or number == 8:
                result += 1


    print('part ' + str(part) + ': ' + str(result))

def part2():
    day = 8
    part = 2
    result = 0

    mapNbToNbSegment = [6,2,5,5,4,5,6,3,7,6]
    
    mapSgmtPosToPossibleLetters = ['abcdefg']*7

    entries = [(entry[0].strip().split(' '),entry[1].strip().split(' ')) for entry in 
                [line.split('|') for line in readFile(day).split('\n')]]

    print(entries)
    
    for entry in entries:
        line = entry[0]

        one = []
        four = []
        seven = []
        for digit in line:
            number = -1
            nbOfLetters = len(digit)
            if nbOfLetters in mapNbToNbSegment:
                number = mapNbToNbSegment.index(nbOfLetters)
            
            if number == 1:
                for letter in digit:
                    one.append(letter)
                    # mapSgmtPosToPossibleLetters[0] = mapSgmtPosToPossibleLetters[0].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[1] = mapSgmtPosToPossibleLetters[1].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[3] = mapSgmtPosToPossibleLetters[3].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[4] = mapSgmtPosToPossibleLetters[4].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[6] = mapSgmtPosToPossibleLetters[6].replace(letter,'')
            elif number == 4:
                for letter in digit:
                    four.append(letter)
                    # mapSgmtPosToPossibleLetters[0] = mapSgmtPosToPossibleLetters[0].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[4] = mapSgmtPosToPossibleLetters[4].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[6] = mapSgmtPosToPossibleLetters[6].replace(letter,'')
            elif number == 7:
                for letter in digit:
                    seven.append(letter)
                    # mapSgmtPosToPossibleLetters[1] = mapSgmtPosToPossibleLetters[1].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[3] = mapSgmtPosToPossibleLetters[3].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[4] = mapSgmtPosToPossibleLetters[4].replace(letter,'')
                    # mapSgmtPosToPossibleLetters[6] = mapSgmtPosToPossibleLetters[6].replace(letter,'')
            elif number == 8:
                for letter in digit:
                    pass

        #print(one)
        #print(four)
        fourDiff = [item for item in four if item not in one]
        #print(fourDiff)
        #print(seven)

        mapNbToIndex = [0]*10

        for i,digit in enumerate(line):
            number = -1
            nbOfLetters = len(digit)
            if nbOfLetters == 5: #2, 3, 5
                if sublist(one,list(digit)):
                    mapNbToIndex[i] = 3
                elif sublist(fourDiff,list(digit)):
                    mapNbToIndex[i] = 5
                else:
                    mapNbToIndex[i] = 2
            elif nbOfLetters == 6: #0, 6, 9
                if sublist(four,list(digit)):
                    mapNbToIndex[i] = 9
                elif sublist(fourDiff,list(digit)):
                    mapNbToIndex[i] = 6
                else:
                    mapNbToIndex[i] = 0
            elif nbOfLetters == 2:
                mapNbToIndex[i] = 1
            elif nbOfLetters == 3:
                mapNbToIndex[i] = 7
            elif nbOfLetters == 4:
                mapNbToIndex[i] = 4
            elif nbOfLetters == 7:
                mapNbToIndex[i] = 8

        #print(mapNbToIndex)

        puzzle = entry[1]
        puzzleNumber = [-1]*4

        for i,item in enumerate(puzzle):
            for j,other in enumerate(mapNbToIndex):
                if sorted(list(item)) == sorted(list(line[j])):
                    puzzleNumber[i] = str(other)

        puzzleNumber = int(puzzleNumber[0] + puzzleNumber[1] + puzzleNumber[2] + puzzleNumber[3])
        number = 0

        print(puzzleNumber)
        result += puzzleNumber
        

        # needToRedo = True
        # while needToRedo:
        #     needToRedo = False
        #     #print('LOOP-----------------------------------------')
        #     for i,elem in enumerate(mapSgmtPosToPossibleLetters):
        #         if(mapSgmtPosToPossibleLetters.count(elem)) > 1:
        #             # There are duplicates
        #             mapSgmtPosToPossibleLetters2 = mapSgmtPosToPossibleLetters.copy()
        #            # print('before' + str(mapSgmtPosToPossibleLetters))
        #             mapSgmtPosToPossibleLetters2[i] = ''
        #            # print(mapSgmtPosToPossibleLetters2)
        #             for j,elem2 in enumerate(mapSgmtPosToPossibleLetters2):
        #                 if elem == elem2 and len(elem) == 2:
        #                   #  print('i: ' + str(i) + ' j: ' + str(j))
        #                     for letter in elem:
        #                         for x in range(6):
        #                             if x not in [i,j]:
        #                                 if letter in mapSgmtPosToPossibleLetters[x]:
        #                                     needToRedo = True
        #                                     mapSgmtPosToPossibleLetters[x] = mapSgmtPosToPossibleLetters[x].replace(letter,'')
        #                     print('after' + str(mapSgmtPosToPossibleLetters))

        # needToRedo = True
        # while needToRedo:
        #     #print('before' + str(mapSgmtPosToPossibleLetters))
        #     needToRedo = False
        #     for i,elem in enumerate(mapSgmtPosToPossibleLetters):
        #         if(len(elem)) == 1:
        #             for j,elem2 in enumerate(mapSgmtPosToPossibleLetters):
        #                 if i != j:                           
        #                     if elem in mapSgmtPosToPossibleLetters[j]:
        #                         needToRedo = True
        #                         mapSgmtPosToPossibleLetters[j] = mapSgmtPosToPossibleLetters[j].replace(elem,'')
        #                         print('after' + str(mapSgmtPosToPossibleLetters))

        # for j,elem in enumerate(mapSgmtPosToPossibleLetters):
        #     if len(elem) > 1:
        #         pass
                            

    
    #print(mapSgmtPosToPossibleLetters)

        # for digit in i:
        #     number = -1
        #     nbOfLetters = len(digit)
        #     if nbOfLetters in mapNbToNbSegment:
        #         number = mapNbToNbSegment.index(nbOfLetters)
            
        #     if number == 1 or number == 4 or number == 7 or number == 8:
        #         result += 1


    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
