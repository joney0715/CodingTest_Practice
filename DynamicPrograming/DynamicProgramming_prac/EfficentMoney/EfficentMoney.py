import math
import time 
import random

N = 2
#Input = []
#for i in range(N):
#    num = random.randint(0,1000)
#    Input.append(num)

Input = [2, 3]
M = 15

def solution(Input, M):
    d = [100000] * (M+1)

    if d[M] == 100000:
        return -1
    else:
        return d[M]


start = time.time() 
print(solution(Input, M))
end = time.time() 
print(f"{end - start:.5f} sec")