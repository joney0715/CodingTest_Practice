
import math
import time 
import random

X = 6

def solution(X):
    d = [0] * (X + 1)
    
    for i in range(2, X+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
    return d[X]

start = time.time() 
print(solution(X))
end = time.time() 
print(f"{end - start:.5f} sec")