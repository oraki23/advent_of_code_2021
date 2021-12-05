 
from os import read
from collections import Counter
import re

def part1():
    day = 5
    part = 1
    result = 0

    max_xAndY = 1000
    
    entries = [[tuple(map(int, (xAndY for xAndY in coordinates.split(','))))
                for coordinates in entry.split(' -> ')]
                for entry in readFile(day).split('\n')]
    
    # Filter for only horizotal and vertical lines
    entries = [entry for entry in entries 
                if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]]

    board = createEmptyBoard(max_xAndY)

    for entry in entries:
        iDirection = 1 if entry[0][0] == entry[1][0] else 0
        jDirection = 0 if entry[0][0] == entry[1][0] else 1

        startingEntryI = 0 if entry[0][iDirection] - entry[1][iDirection] < 0 else 1
        endingEntryI = 1 if entry[0][iDirection] - entry[1][iDirection] < 0 else 0

        i = entry[startingEntryI][iDirection]
        j = entry[startingEntryI][jDirection]
        while i <= entry[endingEntryI][iDirection]:
            if iDirection == 1:
                board[i][j] += 1
            else:
                board[j][i] += 1
            
            i += 1

    for line in board:
        for column in line:
            if column >= 2:
                result += 1

    print('part ' + str(part) + ': ' + str(result))

def printBoard(board):
    for line in board:
        for column in line:
            if column == 0:
                print('.', end="")
            else:
                print(column, end="")
        print('')

def createEmptyBoard(size):
    grid2 = []
    for i in range(size):
        grid2.append([0 for j in range(size)])
    return grid2

def part2():
    day = 5
    part = 2
    result = 0

    max_xAndY = 1000
    
    entries = [[tuple(map(int, (xAndY for xAndY in coordinates.split(','))))
                for coordinates in entry.split(' -> ')]
                for entry in readFile(day).split('\n')]
    
    # Filter for only horizotal and vertical lines
    entriesWithDiag = [entry for entry in entries 
                if entry[0][0] != entry[1][0] and entry[0][1] != entry[1][1]]

    # Filter for only horizotal and vertical lines
    entries = [entry for entry in entries 
                if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]]

    board = createEmptyBoard(max_xAndY)

    for entry in entries:
        iDirection = 1 if entry[0][0] == entry[1][0] else 0
        jDirection = 0 if entry[0][0] == entry[1][0] else 1

        startingEntryI = 0 if entry[0][iDirection] - entry[1][iDirection] < 0 else 1
        endingEntryI = 1 if entry[0][iDirection] - entry[1][iDirection] < 0 else 0

        i = entry[startingEntryI][iDirection]
        j = entry[startingEntryI][jDirection]
        while i <= entry[endingEntryI][iDirection]:
            if iDirection == 1:
                board[i][j] += 1
            else:
                board[j][i] += 1
            
            i += 1

    for diagEntry in entriesWithDiag:
        print('diagentry: ' + str(diagEntry))

        incrementX = 1 if diagEntry[0][0] - diagEntry[1][0] < 0 else -1
        incrementY = 1 if diagEntry[0][1] - diagEntry[1][1] < 0 else -1

        #print('Increment: ' + str(incrementX) + ',' + str(incrementY))

        i = diagEntry[0][0]
        j = diagEntry[0][1]

        while i != diagEntry[1][0]+incrementX and j != diagEntry[1][1]+incrementY:
            print(str(i) + ', ' + str(j))
            board[j][i] += 1
                
            i += incrementX
            j += incrementY

    #printBoard(board)

    for line in board:
        for column in line:
            if column >= 2:
                result += 1

  
    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()