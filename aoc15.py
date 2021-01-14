import time
import numpy as np

numbers = np.array([16,12,1,0,15,7,11],dtype='int8')
used_numbers = numbers.copy()
used_numbers = set([16,12,1,0,15,7])

def find(target, numbers):
    for index,i in enumerate(reversed(numbers[:-1])):
        if i == target:
            return (index + 1)

for i in range(len(numbers)-1,2019):
    if i%10000 ==0:
        print(i)
    current = numbers[i]
    nextn = 0
    if current in used_numbers:
        nextn = find(current,numbers)
    used_numbers.add(current)
    numbers = np.append(numbers,nextn)
    numbers = numbers.astype('int16') 
print(nextn)
