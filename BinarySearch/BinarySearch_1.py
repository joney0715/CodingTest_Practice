#이진 탐색은 이미 정렬되어 있는 리스트에서 타겟의 데이터를 빠르게 찾을 수 있는 알고리즘
import math
import time 
import random

N = 10
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)
Input.sort()
target = random.randint(0,N)

def solution(Input, target):
    def binary_search(Input, target, start, end):
        if start > end:
            return None
        middle = (start + end) // 2
        
        if target == Input[middle]:
            return middle

        elif target > Input[middle]:
            return binary_search(Input, target, middle+1, end)

        else:
            return binary_search(Input, target, start, middle-1)
    
    answer = binary_search(Input, target, Input[0], Input[len(Input)-1])

    return answer+1

print(Input)
print(target)
start = time.time() 
print(solution(Input, target))
end = time.time() 
print(f"{end - start:.5f} sec")


