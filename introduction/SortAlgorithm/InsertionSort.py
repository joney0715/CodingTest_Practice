import math
import time 
import random

N = 10000
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)


def insertion_sort(Input):
    #두번째 데이터 부터 탐색. 첫번째 데이터는 정렬이 되어있다고 가정
    for i in range(1, len(Input)):
        # i번째 데이터부터 역순으로 탐색
        for j in range(i, 0, -1):
            #앞의 데이터와 비교
            if Input[j] < Input[j-1]:
                #앞의 데이터가 더 크면 바꿈
                Input[j], Input[j-1] = Input[j-1], Input[j]
            #더 이상 앞의 데이터가 크지 않으면 반복 멈춤
            #i번째 앞의 데이터들은 이미 정렬 되어있기 때문에 멈춰도 문제 없음
            else:
                break

    answer = Input

    return answer


start = time.time() 
print(insertion_sort(Input))
end = time.time() 
print(f"{end - start:.5f} sec")