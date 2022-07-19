import math
import time 

N = 99
#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * (N+1)

d[1] = 1
d[2] = 1

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

start = time.time() 
print(d[N])
end = time.time() 
print(f"{end - start:.5f} sec")