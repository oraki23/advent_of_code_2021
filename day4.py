 
from os import read
from collections import Counter
import re

def part1():
    day = 4
    part = 1
    result = 0
    
    # Parsing
    input_file = readFile(day).split('\n\n')
    first_line = list(map(int, input_file[0].split(',')))
    boards = [[list(map(int, re.sub(' +', ' ', line.lstrip()).split(' '))) for line in board]
                for board in [board_string.split('\n')
                    for board_string in input_file[1:]]]

    winningBoard = -1
    lastDrawnNumber = -1
    lastDrawnNumberIndex = -1
    for i in range(len(first_line)):
        if i+1 < len(first_line):
            #print('Loop : ' + str(i) + ' nb drawn: ' + str(first_line[i]))
            for j, board in enumerate(boards):
                boardIsWinning = checkIfWinningBoard(board, first_line[0:i+1])
                if boardIsWinning:
                    winningBoard = j
                    lastDrawnNumber = first_line[i]
                    lastDrawnNumberIndex = i
                    break
            if winningBoard != -1:
                break

    sumOfUnmarkedNumber = calculateSumOfUnmarkedNumbers(boards[winningBoard], first_line[0:lastDrawnNumberIndex+1])
    
    result = sumOfUnmarkedNumber * lastDrawnNumber

    print('part ' + str(part) + ': ' + str(result))

def checkIfWinningBoard(board, drawnNumbers):
    completeColumn = [0]*5
    completeLine = [0]*5
    for i, line in enumerate(board):
        for j, entry in enumerate(line):
            if entry in drawnNumbers:
                completeColumn[j] += 1
                completeLine[i] += 1
    
    if 5 in completeColumn or 5 in completeLine:
        return True
    
    return False

def calculateSumOfUnmarkedNumbers(board, drawnNumbers):
    sumOfUnmarkedNumber = 0
    for i, line in enumerate(board):
        for j, entry in enumerate(line):
            if entry not in drawnNumbers:
                sumOfUnmarkedNumber += entry
    return sumOfUnmarkedNumber
    

def part2():
    day = 4
    part = 2
    result = 0

    # Parsing
    input_file = readFile(day).split('\n\n')
    first_line = list(map(int, input_file[0].split(',')))
    boards = [[list(map(int, re.sub(' +', ' ', line.lstrip()).split(' '))) for line in board]
                for board in [board_string.split('\n')
                    for board_string in input_file[1:]]]
    wonBoards = [False]*len(boards)

    lastWinningBoard = -1
    lastDrawnNumber = -1
    lastDrawnNumberIndex = -1
    for i in range(len(first_line)):
        if i+1 < len(first_line):
            #print('Loop : ' + str(i) + ' nb drawn: ' + str(first_line[i]))
            for j, board in enumerate(boards):
                if wonBoards[j] == False:
                    boardIsWinning = checkIfWinningBoard(board, first_line[0:i+1])
                    if boardIsWinning:
                        wonBoards[j] = True
                    
                    if sum(1 for i in wonBoards if i == True) == len(boards):
                        lastWinningBoard = j
                        lastDrawnNumber = first_line[i]
                        lastDrawnNumberIndex = i
                        break
            if lastWinningBoard != -1:
                break

    sumOfUnmarkedNumber = calculateSumOfUnmarkedNumbers(boards[lastWinningBoard], first_line[0:lastDrawnNumberIndex+1])
    
    result = sumOfUnmarkedNumber * lastDrawnNumber

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()