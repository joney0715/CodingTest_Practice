import math
import time 
import random

N = 200000
Input = []
for i in range(N):
    num = random.randint(0,100000000)
    Input.append(num)
k = 2000000000000

#Input = [3,1,2]
#k = 5

def solution(Input, k):
    K = k
    for i in range(K+1):
        i %= len(Input)
        if Input[i] != 0:
            Input[i] -= 1
            k -= 1
        answer = i
    for i in range(len(Input)):
        i = (i + answer +1)%len(Input)
        if Input[i] != 0:
            answer = i + 1
            break
    return answer

start = time.time() 
print(solution(Input,k))
end = time.time() 
print(f"{end - start:.5f} sec")