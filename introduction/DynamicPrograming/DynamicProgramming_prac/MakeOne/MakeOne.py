#이거 틀림


import math
import time 
import random

N = 10
#X = random.randint(0,N)
X = 13
def solution(X):
    i = 0
    x = 1
    while X > x:
        if x * 5 > X:
            i += 1
            x *= 3
        elif x * 5 > X and x * 3 > X:
            i += 1
            x *= 2
        elif x * 5 > X and x * 3 > X and x * 2 > X:
            i += 1
            x += 1
        else:
            i += 1
            x = x * 5

    return i

start = time.time() 
print(solution(X))
end = time.time() 
print(f"{end - start:.5f} sec")