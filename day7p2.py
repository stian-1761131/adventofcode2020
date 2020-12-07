"""Advent of Code Day 7"""
d8input = []
total_bags = 0
has_to_hold = {}
check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
check2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

with open('day8input.txt','r') as f:
        inlines = f.readlines()
        for line in inlines :
            d8input.append(line.strip('\n'))

def get_first_bag(input_str) :
    count_spaces = 0
    return_str = ""
    for i in input_str :
        if i == " " or i == ',' or i == '.':
            count_spaces += 1
        if count_spaces == 3 :
            break
        return_str = return_str + i
    
    if return_str[-1] == 's' :
        return return_str[:-1]
    else :
        return return_str

for line in d8input :
    bag = get_first_bag(line)
    num_bags = 0
    num_holding_bag = 0
    holds = []
    for char in range(len(line)) :
        if line[char] in check :
            new_bag = get_first_bag(line[int(char)+2:])
            num_bags = int(line[char])
            num_holding_bag += int(line[char])
            if bag not in has_to_hold.keys() :
                has_to_hold[bag] = [new_bag, num_bags]
            else :
                has_to_hold[bag].append(new_bag)
                has_to_hold[bag].append(num_bags)

input_arr = has_to_hold['shiny gold bag']

def count_bags(arr_input) :
    global has_to_hold
    global check
    global total_bags
    global check2
    return_num = 0
    for i in range(len(arr_input)) :
        if arr_input[i] in check2 :
            continue
        elif arr_input[i] not in has_to_hold.keys() :
            return_num += arr_input[i+1]
        elif arr_input[i] in has_to_hold.keys() :
            num_of_bags = arr_input[i+1]
            return_num += num_of_bags + (num_of_bags * count_bags(has_to_hold[arr_input[i]]))

    return return_num

print(count_bags(has_to_hold['shiny gold bag']))