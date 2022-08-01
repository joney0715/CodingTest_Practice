from itertools import combinations
import math
import time 
import random
from itertools import combinations

N = 50
Input = []
for i in range(5):
    num = random.randint(0,N)
    Input.append(num)
Input = list(set(Input))
#Input = [2,3,6,8]
#N = 8

def solution(Input,N):
    
    def grouping(Input):
        Input.sort()
        group = [Input[0]]
        for i in range(1,len(Input)):
            if Input[i] - Input[i-1] > 1:
                group.append(Input[i])
        return group

    pick = []
    for i in range(1,N+1):
        if i not in Input:
            pick.append(i)
    
    answer = []
    for i in range(1,len(pick)+1):
        combination = list(combinations(pick, i))
        ans = []
        for j in range(len(combination)):
            card = [x for x in Input]
            for k in range(len(combination[j])):
                card.append(combination[j][k])
            group = grouping(card)
            s = sum(group)
            ans.append(s)
        m = min(ans)
        answer.append(m)

    return answer

start = time.time() 
print(solution(Input,N))
end = time.time() 
print(f"{end - start:.5f} sec")