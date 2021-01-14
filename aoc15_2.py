import time
import numpy as np
from itertools import chain

numbers = (i for i in reversed([16,12,1,0,15,7,11]))
used_numbers = set([16,12,1,0,15,7])

def find(target, numbers):
    now = 0
    for index,i in enumerate(numbers):
        if i == target:
            return (index + 2)

for i in range(10):
    # if i%10000 ==0:
    #     print(i)
    numbers, numbers_2 = tee(y)
    current = next(numbers)
    print(current)
    nextn = 0
    if current in used_numbers:
        nextn = find(current,numbers)
    used_numbers.add(current)
    numbers_copy = chain((i for i in [nextn]),(i for i in numbers_2))
    for number in numbers_copy:
        print(number)
    numbers = numbers_copy
    print("----")
print(nextn)
#print(numbers)
#print(numbers)
    
