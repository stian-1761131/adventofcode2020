import time

day15input = [7,12,1,0,16,2]
last_spoken = {}

start_time = time.time()

for i in range(len(day15input)) :
    last_spoken[day15input[i]] = i+1

last_turn = day15input[-1]
j = len(day15input)
most_recent = 0

for i in range(j, 2020) :
    if last_turn in last_spoken.keys() and last_spoken[last_turn] != i :
        next_num = i - last_spoken[last_turn]
        last_spoken[last_turn] = i
        most_recent = next_num
        #day15input.append(next_num)
        last_turn = next_num

    else :
        last_spoken[last_turn] = i
        last_turn = 0
        most_recent = 0
        #day15input.append(0)

# print(day15input[-1])
print(most_recent)
print("--- %s seconds ---" % (time.time() - start_time))