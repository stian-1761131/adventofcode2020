"""Advent of Code Day 9"""

d9input = []

with open('d9input.txt','r') as f:
    d9input = [line.strip('\n') for line in f.readlines()]

def get_possible_numbers(l_input) :
    possible_nums = []
    for num in range(len(l_input)) :
        for i in range(len(l_input)) :
            if num == i :
                continue
            elif num in possible_nums :
                continue
            else :
                possible_nums.append(int(l_input[i]) + int(l_input[num]))
    return possible_nums

num_looking_for = 552655238
num = 0
i = 0
j = 1

while i < len(d9input):
    nums_list = []
    while num <= num_looking_for and j < len(d9input):
        num += int(d9input[j])
        nums_list.append(int(d9input[j]))
        if num == num_looking_for and int(d9input[i]) != num_looking_for:
            print(min(nums_list)+max(nums_list))
            break
        else :
            j += 1

    num = 0
    i += 1
    j = i