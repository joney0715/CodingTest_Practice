import math
import time 
import random
from turtle import right

N = 1000000
Input = []
for i in range(N):
    num = random.randint(0,N)
    Input.append(num)

def Quick_sort(Input):
    
    #퀵 정렬의 계산 함수
    def cal(Input, start, end):
        ##종료 조건
        #원소가 1개인 경우 종료
        if start >= end:
            return
        
        ##초기값 설정
        #피벗을 첫 번째 원소
        pivot = start
        #피벗 설정 후에 왼쪽에서부터 원소 하나 선택
        left = start + 1
        #오른쪽에서부터 원소 하나 선택
        right = end

        #왼쪽에서부터 오른쪽으로, 오른쪽에서 왼쪽으로 이동해오면서 위치가 서로 바뀔때까지 연산
        while left <= right:

            ##가정법을 사용하지 않고 데이터의 인덱스를 찾는 방법
            #피벗보다 큰 데이터를 찾을 때까지 반복
            while left <= end and Input[left] <= Input[pivot]:
                left += 1 #피벗보다 데이터가 작으면 왼쪽에서 하나 이동           
            #피벗보다 작은 데이터를 찾을 때까지 반복
            while right > start and Input[right] >= Input[pivot]:
                right -= 1 #피벗보다 데이터가 크면 오른쪽에서 하나 이동
            
            #왼쪽의 데이터가 피벗보다 크고, 오른쪽의 데이터가 피벗보다 작은 경우
            #서로 엇갈린 경우 피벗을 작은 데이터와 교체
            if left > right:
                Input[right],Input[pivot] = Input[pivot],Input[right]

            #왼쪽과 오른쪽이 엇갈리지 않았고, 왼쪽의 데이터가 피벗보다 크고, 오른쪽의 데이터가 피벗보다 작은 경우
            #작은 데이터(오른쪽 데이터)와 큰 데이터(왼쪽 데이터)를 교체
            else:
                Input[left],Input[right] = Input[right],Input[left]

        #피벗을 기준으로 왼쪽 부분과 오른쪽 부분을 분할
        #현재 비펏은 right에 존재
        #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        cal(Input, start, right - 1)
        cal(Input, right + 1, end)

    cal(Input, 0, len(Input)-1)

    return Input

start = time.time() 
print(Quick_sort(Input))
end = time.time() 
print(f"{end - start:.5f} sec")