
import math
import time 
import random

#입력치
X = 24

def solution(X):
    #계산된 내용을 저장하기 위한 메모리
    d = [0] * (X + 1)
    
    for i in range(2, X+1):
        #i번째 수의 계산 횟수는 i-1번째 수의 계산 횟수보다 하나 많다고 가정(-1 연산의 경우를 가정)
        d[i] = d[i-1] + 1

        #i번째의 수가 n(2,3,5)로 나눠질 경우
        # 1. 위에서 계산한 결과 (-1 연산을 해서 i-1번째의 수의 계산 횟수를 이용하는 것)
        # 2. i / 2 번째 수의 계산 횟수에 하나 더한 결과(2를 한번 나누므로 계산 횟수가 하나 늘어남)
        # 1. 2. 를 비교해서 계산 횟수가 적은 쪽 선택 
        # elif 가 아닌 if 로 써져있는 이유는 2,3,5를 약수로 갖는 수가 있기 때문 
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    #입력치의 계산 횟수를 불러와서 출력
    return d[X]

start = time.time() 
print(solution(X))
end = time.time() 
print(f"{end - start:.5f} sec")