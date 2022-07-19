#피보나치 수열을 재귀함수로 재현
#1 1 2 3 5 8 13 21 ....

import math
import time 

def Fibo(N):
    if N == 1 or N ==2:
        return 1
    return Fibo(N-1) + Fibo(N-2)

N = 99

start = time.time() 
print(Fibo(N))
end = time.time() 
print(f"{end - start:.5f} sec")