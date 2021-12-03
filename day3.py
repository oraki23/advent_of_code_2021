 
from os import read
from collections import Counter

def part1():
    day = 3
    part = 1
    result = 0

    gamma = 0
    epsilon = 0

    gamma_bit = ""
    epsilon_bit = ""
    for i in range(12):
        most_common_bit = Counter([entry[i:i+1] for entry in list(readFile(day).split('\n'))]).most_common(1)[0][0]
        least_common_bit = Counter([entry[i:i+1] for entry in list(readFile(day).split('\n'))]).most_common()[-1][0]
        gamma_bit += most_common_bit
        epsilon_bit += least_common_bit
    gamma = int(gamma_bit, 2)
    epsilon = int(epsilon_bit, 2)

    result = gamma * epsilon

    print('part ' + str(part) + ': ' + str(result))

def part2():
    day = 3
    part = 2
    result = 0
    size_of_bits = 12

    gamma = 0
    epsilon = 0

    gamma_bit = ""
    epsilon_bit = ""

    filtered_most_common = [i for i in list(readFile(day).split('\n'))]
    filtered_least_common = [i for i in list(readFile(day).split('\n'))]

    filtered_lists = [filtered_most_common, filtered_least_common]
    results = ["0", "0"]

    for x in range(2):
        filtered_list = filtered_lists[x]
        for i in range(size_of_bits):
            most_common_bit = Counter([entry[i:i+1] for entry in filtered_list]).most_common(1)[0][0]
            least_common_bit = Counter([entry[i:i+1] for entry in filtered_list]).most_common()[-1][0]

            most_common_bit_count = Counter([entry[i:i+1] for entry in filtered_list]).most_common(1)[0][1]
            least_common_bit_count = Counter([entry[i:i+1] for entry in filtered_list]).most_common()[-1][1]

            if most_common_bit_count == least_common_bit_count:
                most_common_bit = str(1)
                least_common_bit = str(0)

            if x == 0:
                filtered_list = [entry for entry in filtered_list if entry[i:i+1] == most_common_bit]
            else:
                filtered_list = [entry for entry in filtered_list if entry[i:i+1] == least_common_bit]

            if len(filtered_list) <= 1:
                break
        results[x] = filtered_list[0]

    oxygen_generator = int(results[0], 2)
    co2_scrubber = int(results[1], 2)

    result = oxygen_generator * co2_scrubber

    print('part ' + str(part) + ': ' + str(result))

def readFile(day):
    f = open("day" + str(day) + "_input.txt", "r")

    return f.read()

if __name__ == '__main__':
    part1()
    part2()