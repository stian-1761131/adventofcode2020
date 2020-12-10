d10input = []
with open('d10input.txt','r') as f:
    d10input = [int(line.strip('\n')) for line in f.readlines()]

d10input.sort()
d10input.insert(0,0)
d10input.append(d10input[-1]+3)

""" part 1
jolt1 = 0
jolt2 = 0
jolt3 = 0

if int(d10input[0]) == 1 :
    jolt1 += 1
elif int(d10input[0]) == 2 :
    jolt2 += 1
elif int(d10input[0]) == 3 :
    jolt3 += 1

jolt3 += 1

for i in range(len(d10input)-1) :
    if int(d10input[i+1]) - int(d10input[i]) == 1 :
        jolt1 += 1
    elif int(d10input[i+1]) - int(d10input[i]) == 2 :
        jolt2 += 1
    elif int(d10input[i+1]) - int(d10input[i]) == 3 :
        jolt3 += 1
"""

"""Part 2 using DP for the first time :o"""
#create a dictionary to store the values for each i so that we don't have to re-compute them every time
nums_dict = {}
#write a recursive function to get the amount of paths up to i
def count_ways(i) :
    if i == len(d10input) -1 :
        #theres only 1 way to get to the end from the end
        return 1
    if i in nums_dict.keys() :
        return nums_dict[i]
    num = 0
    for j in range(i + 1, len(d10input)) :
        if d10input[j] - d10input[i] <= 3 :
            num += count_ways(j)
    nums_dict[i] = num
    return num

print(count_ways(0))