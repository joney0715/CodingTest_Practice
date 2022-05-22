import math
import time 
import random
from itertools import combinations

N = 1000
Input = []
for i in range(N):
    num = random.randint(0,1000000)
    Input.append(num)

Input = [3,2,1,1,9]

#직접 만든 코드
#===============
#타임 아웃
#===============
def solution(Input): 
    #가진 화폐로 만들 수 있는 경우의 수
    money = []
    for i in range(1,len(Input)+1):
        #가진 화페를 콤비네이션을 사용해서 뽑기
        case = list(combinations(Input,i))
        for j in case:
            #뽑힌 화페의 총합
            money.append(sum(j))
    #1부터 차례로 가진 화폐로 만들 수 있는가 확인
    for a in range(1,int(1e9)):
        if a not in money:
            answer = a
            break
    return answer

#해답 코드
#알고리즘의 아이디어에 주의
def solution_answer(Input):
    #가진 화폐를 오름차순으로 정렬
    Input.sort()
    #만들 수 있는지 확인할 타겟을 설정
    #처음엔 1로 초기화
    target = 1

    #가진 화폐를 하나씩 검토
    for i in Input:
        #타겟이 검토중인 화폐보다 작은 경우, 
        #다음 화폐는 더 큰 값이기 때문에
        #타겟은 지금 가진 화페로는 만들수 없음
        if target < i:
            break
        #타겟이 검토중이 화페보다 크거나 같다면 만들수 있음
        #만들수 있기 때문에 타겟을 화폐만큼 증가
        target += i    
    answer = target
    return answer

start = time.time() 
#print(solution(Input))
print(solution_answer(Input))
end = time.time() 
print(f"{end - start:.5f} sec")