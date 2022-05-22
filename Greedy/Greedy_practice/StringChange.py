import math
import time 
import random

N = 5
Input = []
for i in range(N):
    num = random.randint(0,1)
    Input.append(str(num))
Input = ["1","1","1","0","0","1"]

def solution(Input):
    #직접 만든 코드
    """
    count_0 = 0 #전부 0으로 하는 횟수
    count_1 = 0 #전부 1로 하는 횟수
    #각각의 경우에 대해 한번씩 횟수 추가
    if Input[0] == str(0):
        count_0 += 1
    else:
        count_1 += 1
    #두번째부터 카운트
    for i in range(1,len(Input)):
        #i번째가 0인데 앞순서인 i-1과 다른 경우, 전부 1로 바꾸는 경우 횟수 추가 
        if Input[i-1] != Input[i] and Input[i] == str(0):
            count_1 += 1
        #i번째가 1인데 앞순서인 i-1과 다른 경우, 전부 0로 바꾸는 경우 횟수 추가 
        if Input[i-1] != Input[i] and Input[i] == str(1):
            count_0 += 1
        #앞 순서와 같다면 횟수가 추가할 필요가 없으므로 처리하지 않음
    #작은 것 선택
    if count_0 <= count_1:
        answer = count_0
    else:
        answer = count_1
    """

    #해답 코드
    #0,1의 경우를 전부 구하고 비교하여 작은 것을 선택하는 아이디어는 같음
    count_0 = 0 #전부 0으로 하는 횟수
    count_1 = 0 #전부 1로 하는 횟수
    #각각의 경우에 대해 한번씩 횟수 추가
    if Input[0] == str(0):
        count_0 += 1
    else:
        count_1 += 1

    #--------------
    #여기까지는 직접 쓴 코드와 동일
    #--------------
    for i in range(len(Input)-1):
        #해답에서는 앞 순서가 아닌 다음 순서와 비교
        #먼저 같은지 아닌지를 비교후 0인지 1인지 확인 
        if Input[i] != Input[i+1]:
            if Input[i] == str(1):
                count_0 += 1
            else:
                count_1 += 1
                
    #가정법이 아닌 min함수 사용
    answer = min(count_0, count_1)
    return answer
    


start = time.time() 
print(solution(Input))
end = time.time() 
print(f"{end - start:.5f} sec")