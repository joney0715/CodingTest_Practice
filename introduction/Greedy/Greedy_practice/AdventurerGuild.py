import math
import time 
import random

N = 50
Input = []
for i in range(N):
    num = random.randint(0,5)
    Input.append(num)

#Input = [3,2,1,2,2]

def solution(Input):
    #공포도가 낮은 순으로 정렬
    #최대의 길드 수를 구해야하므로 오름차순으로 정렬 필요
    Input.sort()

    #길드 수
    guild = 0
    #길드 맴버 수
    member = 0

    #맴버 한명 씩 길드에 넣기
    for i in Input:
        #반복문으로 뽑힌 맴버를 추가
        member += 1
        #뽑힌 맴버의 공포도와 길드의 맴버 수를 비교
        #뽑힌 맴버의 공포도 보다 맴버 수가 많은 경우
        #길드로서 성립 
        if member >= i:
            guild += 1
            #길드가 성립했으므로 맴버 수 초기화
            member = 0

    return guild

start = time.time() 
print(solution(Input))
end = time.time() 
print(f"{end - start:.5f} sec")