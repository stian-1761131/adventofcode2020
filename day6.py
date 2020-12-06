d6input = []

with open('d6input.txt','r') as f:
        inlines = f.readlines()
        for line in inlines :
            d6input.append(line.strip('\n'))

def count_questions(input_str, num) :
    count = 0
    already_accounted_for = []
    for i in input_str :
        if input_str.count(i) == num and i not in already_accounted_for:
            count += 1
            already_accounted_for.append(i)

    return count

total_count = 0
i = 0
"""Part 1"""
# while i < len(d6input):
#     pass_in = ''
#     while d6input[i] != '' and i < len(d6input)-1:
#         n = pass_in
#         pass_in = n + d6input[i]
#         i += 1
#     total_count += count_questions(pass_in)
#     if i == len(d6input) :
#         break
#     i += 1

while i < len(d6input) :
    num_people = 0
    pass_in = ''
    while d6input[i] != '' and i < len(d6input)-1:
        num_people += 1
        n = pass_in
        pass_in = n + d6input[i]
        i += 1
    total_count += count_questions(pass_in, num_people)

    if i == len(d6input) :
        break
    i += 1

print(total_count)


