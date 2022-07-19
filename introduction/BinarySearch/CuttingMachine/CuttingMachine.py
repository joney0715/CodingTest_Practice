#이진탐색을 이용한 문제 풀이
import math
import time 
import random

N = 1000000
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)
Input.sort()

i = 2000000000
M = random.randint(0,i)

#Input = [19,15,10,17]



def solution(Input, M):
    Input.sort()

    def binary_search(Input, start, end, M): 

        middle = (start + end) // 2

        cutted = [i - middle for i in Input]
        for i in range(len(cutted)-1):
            if cutted[i] <= 0:
                cutted[i] = 0

        m = sum(cutted)

        if end <= start:
            return middle

        if m == M:
            return middle

        elif m > M:
            return binary_search(Input, middle+1, end, M)
        
        else:
            return binary_search(Input, start, middle-1, M)

    answer = binary_search(Input, 0, Input[len(Input)-1], M)

    return answer


start = time.time() 
print(solution(Input, M))
end = time.time() 
print(f"{end - start:.5f} sec")

        
