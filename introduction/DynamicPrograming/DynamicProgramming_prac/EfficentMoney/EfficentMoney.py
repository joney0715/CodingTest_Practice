#이거 틀림

import math
import time 
import random

N = 2
#Input = []
#for i in range(N):
#    num = random.randint(0,1000)
#    Input.append(num)

#화페 종류
Input = [2, 3]

#금액
M = 15

def solution(Input, M):
    #메모리
    d = [100000] * (M+1)

    d[0] = 0

    for i in range(2, M+1):
        for j in range(len(Input)-1):
            if d[i] != 100000:
                d[i] = min(d[i], d[i - Input[j]] + 1)

    if d[M] == 100000:
        return -1
    else:
        return d[M]


start = time.time() 
print(solution(Input, M))
end = time.time() 
print(f"{end - start:.5f} sec")