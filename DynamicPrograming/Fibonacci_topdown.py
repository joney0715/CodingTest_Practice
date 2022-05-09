#다이나믹 프로그래밍을 사용할 수 있는 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

import math
import time 

#탑 다운 다이나믹 프로그래밍이 적용된 피보나치 수열
def fibo(N):
    #N이 1,2인 경우는 1을 출력
    if N == 1 or N == 2:
        return 1

    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[N] != 0:
        return d[N]

    #아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[N] = fibo(N-1) + fibo(N-2)

    return d[N]

N = 99
#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * (N+1)

start = time.time() 
print(fibo(N))
end = time.time() 
print(f"{end - start:.5f} sec")

