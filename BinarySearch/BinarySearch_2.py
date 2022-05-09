#반복문을 사용한 이진 탐색
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
        #시작점이 끝점보다 커지기 전까지 반복
        while start <= end:
            #중간값 정의
            middle = (start + end) // 2
            #중간값이 타겟이라면 중간값 출력
            #리스트의 인덱스는 0부터 시작하므로 +1을 해서 출력 필요
            if target == Input[middle]:
                return middle + 1

            #타겟이 중간값보다 클 때
            #중간값과 리스트의 끝점으로 이진 탐색 실행
            elif target < Input[middle]:
                end = middle - 1

            #타겟이 중간값보다 작을 때
            #리스트의 시작점과 중간값으로 이진 탐색 실행
            else:
                start = middle + 1
        
        #끝점이 시작점보다 작을 때
        return None
    
    answer = binary_search(Input, target, Input[0], Input[len(Input)-1])

    return answer

print(Input)
print(target)
start = time.time() 
print(solution(Input, target))
end = time.time() 
print(f"{end - start:.5f} sec")



