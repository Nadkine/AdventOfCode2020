array = []

with open('data10.txt','r') as f:
    for line in f.readlines():
        array.append(int(line))

tribonacci = [1,1,2,4,7,13,24,44,81,149,274, 504, 927, 1705, 3136] 
array.sort()
previous = 0
jolt_difference = []
for item in array:
    jolt_difference.append(item-previous)
    previous = item
amount_ones = 0
opps = 1
for index, dif in enumerate(jolt_difference):
    if dif == 1:
        amount_ones += 1
    else:
        print(f"tribo - {tribonacci[amount_ones]}")
        opps *= tribonacci[amount_ones]
        amount_ones = 0
    if index == len(jolt_difference)-1:
        opps *= tribonacci[amount_ones]

print(opps)
