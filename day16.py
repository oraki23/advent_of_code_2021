 
from heapq import heappop, heappush
from os import read
from collections import Counter
import re
import math
import time
from typing import final

def part1():
    day = 16
    part = 1
    result = 0
    
    entries_raw = [line for line in readFile(day).split('\n')]
    entries = []
    for i,entry in enumerate(entries_raw):
        new_entry = ''
        for char in entry:
            #print(char)
            # if i == 7:
                # print(int(char,16),end=',')
                # print(format(int(char,16), '04b'),end=',')
            new_entry += format(int(char,16), '04b')

        entries.append(new_entry)
    # print()
    # print(entries[7])

    for i in range(1):
        i = 7
        resultat = [0]
        recursive_function(entries[i], resultat, 0)

    result = resultat[0]


    print('part ' + str(part) + ': ' + str(result))

def recursive_function(entry, resultat, depth):
    print('START OF RECURSIVE ===== depth: ' + str(depth))
    print(entry)
    #if len(entry) == 0:
    #    print('empty entry')
    #    return -10

    packet_version = int(entry[0:3],2)
    type_id = int(entry[3:6],2)
    print('packet_version: ' + str(packet_version))
    resultat[0] += packet_version
    print('type_id: ' + str(type_id))

    # Literal value, single binary number
    if type_id == 4:
        in_last_group = False
        j_start = 6
        final_binary = ''
        while not in_last_group:
            # print('j_start: '  + str(j_start))
            leading_bit = entry[j_start]
            other_bit = entry[j_start+1:j_start+5]
            final_binary += other_bit
            if leading_bit == '0':
                in_last_group = True
            j_start += 5
            #print(other_bit)
            
        #print(' final_binary: ' + str(final_binary))
        # print(' j_start: ' + str(j_start))
        # print(' entry len:' + str(len(entry)) )
        final_value_int = int(final_binary,2)
        print('operation type 4 (literal): ' + str(final_value_int))
        return j_start
    # Generic parsing for operators
    else:
        length_type_id = int(entry[6:7],2)
        print('length_type_id: ' + str(length_type_id))
        if length_type_id == 0:
            total_length_in_bits_of_packets = int(entry[7:22],2)
            print('total_length_in_bits_of_packets: ' + str(total_length_in_bits_of_packets))

            ending_index = (22+total_length_in_bits_of_packets)
            ended_index = 22

            #print(entry[22:(22+total_length_in_bits_of_packets)])
            while ended_index < ending_index:
                # print('========XYZ: ' + str(entry[ended_index:ending_index]))
                
                result_recursive = recursive_function(entry[:ending_index], resultat, depth+1)
                print('ended_index: ' +str(ended_index))
                print('resultrecur: ' + str(result_recursive))
                ended_index += result_recursive

                #print('ENDED: ' + str(ended_index))
                
            return ended_index

        elif length_type_id == 1:
            number_of_subpackets_immediately_contained = int(entry[7:18],2)
            print('number_of_subpackets_immediately_contained: ' + str(number_of_subpackets_immediately_contained))
            #length_remaining_bits = len(entry[18:])
            length_each = -1
            start_index = 18
            ending_index = start_index
            if number_of_subpackets_immediately_contained > 0:
                for x in range(number_of_subpackets_immediately_contained):
                    print('========XYZ: ' + str(entry[start_index+(length_each*x):]))

                    if length_each != -1:
                        result_recursive = recursive_function(entry[start_index+(length_each*x):], resultat, depth+1)
                        ending_index += (length_each)
                    else:
                        result_recursive = recursive_function(entry[start_index:], resultat, depth+1)
                        ending_index += result_recursive
                        length_each = ending_index - start_index
                        ending_index += (length_each)
            return ending_index
        else:
            print('error 1')



def print_beautiful(double_entry, max_x, max_y):
    result = 0
    for x in range(max_x):
        for y in range(max_y):
            print(str(double_entry[x][y]), end='|')
        print()
    return result

def part2():
    day = 16
    part = 2
    result = 0

    #entries = [[int(line[x]) for x in range(len(line))] for line in readFile(day).split('\n')]



    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

def RepresentsIntBool(s):
    try: 
        int(s,2)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    part1()
    part2()
