import math
import time 
import random

N = 5
Input = []
for i in range(N*2):
    num = random.randint(0,9)
    Input.append(str(num))
Input = int(''.join(Input))

def solution(Input):
    Input = list(map(int,str(Input)))
    f = 0
    b = 0 
    for i in range(len(Input)//2):
        f += Input[i]
        b += Input[-i-1]

    if f == b:
        answer = "LUCKY"
    else:
        answer = "READY"

    return answer

start = time.time() 
print(solution(Input))
end = time.time() 
print(f"{end - start:.5f} sec")