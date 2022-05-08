import math
import time 
import random

N = 10000
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)

# 선택 정렬 : 가장 작은 데이터를 맨 앞으로 두고, 그 다음 작은 데이터를 두번째에 두는 알고리즘
def selection_sort(Input):
    
    #리스트의 1번 데이터 부터 선택
    for i in range(len(Input)):
        #선택된 데이터가 가장 작다고 가정
        min_index = i

        #선택된 데이터의 다음 데이터를 하나씩 탐색
        for j in range(i+1,len(Input)):
            #탐색 대상 데이터가 선택된 데이터 보다 작은 경우
            if Input[min_index] > Input[j]:
                #탐색 대상 데이터가 가장 작다고 가정
                min_index = j
            #j반복문의 결과로 가장 작은 값의 인덱스가 색출

        #가장 작은 데이터와 가장 앞에 있는 데이터를 바꿈
        Input[i],Input[min_index] = Input[min_index], Input[i] #스와프
    
    answer = Input

    return answer

start = time.time() 
print(selection_sort(Input))
end = time.time() 
print(f"{end - start:.5f} sec")
