import math
import time 
import random

N = 1000
Input = []
for i in range(N):
    num = random.randint(0,10)
    Input.append(num)

#Input = [1,5,4,3,2,4,5,2]

def solution(Input):
    count = 0
    for i in range(len(Input)):
        for j in range(i,len(Input)):
            if Input[i] != Input[j]:
                count += 1
    return count

print(solution(Input))