import math
import time 
import random

N = 2
#Input = []
#for i in range(N):
#    num = random.randint(0,1000)
#    Input.append(num)

#화페 단위 정의
Input = [2, 3]

#입력 금액 정의
M = 15

def solution(Input, M):
    #메모리 정의
    #화폐로 구성할 수 없는 경우 100000으로 정의
    #메모리의 모든 요소를 일단 화폐로 구성할 수 없는 걸로 가정
    d = [100000] * (M+1)

    #0은 화페로 구성할 수 없으므로 d[0]은 0이라고 정의
    d[0] = 0
    
    #구성 화폐를 하나씩 연산
    for i in range(len(Input)):
        #구성 화폐부터 입력 금액까지 연산
        for j in range(Input[i], M + 1):
            #연산해야하는 금액에 화폐를 뺐을때 화폐 구성이 가능한 경우
            #불가능 하다면 결국 불가능으로 출력
            if d[j - Input[i]] != 100000:
                #j에서 화페 Input[i]를 뺀 금액은 과거에 계산됐기 때문에 그 금액에 화폐 하나 추가
                # (화폐Input[i]를 빼는 작업이 들어갔기 때문)  
                d[j] = min(d[j], d[j-Input[i]] + 1)

    if d[M] == 100000:
        return -1
    else:
        return d[M]


start = time.time() 
print(solution(Input, M))
end = time.time() 
print(f"{end - start:.5f} sec")