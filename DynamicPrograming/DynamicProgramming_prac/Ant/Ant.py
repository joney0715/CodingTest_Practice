import math
import time 
import random

N = 100
Input = []
for i in range(N):
    num = random.randint(0,1000)
    Input.append(num)

#Input = [1,3,1,5,4,1,6]

def solution(Input):
    d = [0] * (len(Input) + 1)

    #처음 1개와 2개일 경우 최대 값을 정의
    d[0] = Input[0]
    d[1] = max(Input[0], Input[1])

    #i번째와 i-2번째까지의 최대치의 합
    #i-1번째까지의 최대치의 합
    #위 두 가지를 비교하여 더 큰 것을 선택
    for i in range(2, len(Input)):
        d[i] = max(d[i-1], d[i-2] + Input[i])

    return d[len(Input)-1]

start = time.time() 
print(solution(Input))
end = time.time() 
print(f"{end - start:.5f} sec")