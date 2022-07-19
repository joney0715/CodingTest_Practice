#이진 탐색은 이미 정렬되어 있는 리스트에서 타겟의 데이터를 빠르게 찾을 수 있는 알고리즘
import math
import time 
import random

N = 10
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)
#이진 탐색은 정렬된 리스트가 대상인 알고리즘
Input.sort()
target = random.randint(0,N)

#입력 리스트와 타겟 값 
def solution(Input, target):
    #이진 탐색을 위한 함수 정의
    def binary_search(Input, target, start, end):
        #이진 탐색의 시작점이 끝점 보다 크면 None 출력
        if start > end:
            return None
        #중간값 정의
        middle = (start + end) // 2
        #중간값이 타겟이라면 중간값 출력
        #리스트의 인덱스는 0부터 시작하므로 +1을 해서 출력 필요
        if target == Input[middle]:
            return middle + 1
        #타겟이 중간값보다 클 때
        #중간값과 리스트의 끝점으로 이진 탐색 실행
        elif target > Input[middle]:
            return binary_search(Input, target, middle+1, end)

        #타겟이 중간값보다 작을 때
        #리스트의 시작점과 중간값으로 이진 탐색 실행
        else:
            return binary_search(Input, target, start, middle-1)
    
    answer = binary_search(Input, target, Input[0], Input[len(Input)-1])

    return answer

print(Input)
print(target)
start = time.time() 
print(solution(Input, target))
end = time.time() 
print(f"{end - start:.5f} sec")


