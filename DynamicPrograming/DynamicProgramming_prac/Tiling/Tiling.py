
import math
import time 

N = 3

def solution(N):
    d = [0] * (N+1)

    d[1] = 1
    d[2] = 3

    for i in range(3, N+1):
        d[i] = d[i-1] + d[i-2] * 2 

    return d[N]

start = time.time() 
print(solution(N))
end = time.time() 
print(f"{end - start:.5f} sec")