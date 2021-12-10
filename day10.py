 
from os import read
from collections import Counter
import re
import math

def part1():
    day = 10
    part = 1
    result = 0

    entries = [[line[x] for x in range(len(line))] for line in readFile(day).split('\n')]
    #print(entries)

    for line in entries:
        stack = []
        line_corrupted = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char == ')':
                lastCharacter = stack.pop()
                if lastCharacter != '(':
                    line_corrupted = True
                    result += 3
            elif char == ']':
                lastCharacter = stack.pop()
                if lastCharacter != '[':
                    line_corrupted = True
                    result += 57
            elif char == '}':
                lastCharacter = stack.pop()
                if lastCharacter != '{':
                    line_corrupted = True
                    result += 1197
            elif char == '>':
                lastCharacter = stack.pop()
                if lastCharacter != '<':
                    line_corrupted = True
                    result += 25137
            
            if line_corrupted:
                printErrorMessage(line, lastCharacter, char)
                break


    print('part ' + str(part) + ': ' + str(result))

def printErrorMessage(line, expected, found):
    for i in line:
        print(i, end='')
    print(' - Expected ' + str(expected) + ', but found ' + str(found) + ' instead.')

def part2():
    day = 10
    part = 2
    result = 0

    entries = [[line[x] for x in range(len(line))] for line in readFile(day).split('\n')]

    entries_2 = [[line[x] for x in range(len(line))] for line in readFile(day).split('\n')]

    for i,line in enumerate(entries):
        stack = []
        line_corrupted = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char == ')':
                lastCharacter = stack.pop()
                if lastCharacter != '(':
                    line_corrupted = True
            elif char == ']':
                lastCharacter = stack.pop()
                if lastCharacter != '[':
                    line_corrupted = True
            elif char == '}':
                lastCharacter = stack.pop()
                if lastCharacter != '{':
                    line_corrupted = True
            elif char == '>':
                lastCharacter = stack.pop()
                if lastCharacter != '<':
                    line_corrupted = True
            
            if line_corrupted:
                entries_2.remove(line)
                #printErrorMessage(line, lastCharacter, char)
                break
    
    results = [0]*len(entries_2)

    for i,line in enumerate(entries_2):
        stack = []
        line_corrupted = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            elif char == ')':
                lastCharacter = stack.pop()
            elif char == ']':
                lastCharacter = stack.pop()
            elif char == '}':
                lastCharacter = stack.pop()
            elif char == '>':
                lastCharacter = stack.pop()
        print(stack)

        for x in range(len(stack)):
            character = stack.pop()
            if character == '(':
                results[i] = results[i] * 5 + 1
            elif character == '[':
                results[i] = results[i] * 5 + 2
            elif character == '{':
                results[i] = results[i] * 5 + 3
            elif character == '<':
                results[i] = results[i] * 5 + 4
            
    results.sort(reverse=True)
    print(results)
    print(len(results)/2)
    print(math.ceil(len(results)/2))

    print(results[math.floor(len(results)/2)])
    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

if __name__ == '__main__':
    part1()
    part2()
