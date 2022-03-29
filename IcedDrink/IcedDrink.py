import math 
import time 
import random

ice = []
ice_y = []
for i in range(100):
    for j in range(100):
        num = random.randint(0,1)
        ice_y.append(num)
    ice.append(ice_y)
#ice = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def solution(ice):
    answer = 0
    def IcedDrink(x,y):
        if x <= -1 or x >= len(ice) or y <= -1 or y >= len(ice[0]):
            return False

        if ice[x][y] == 0:
            ice[x][y] = 1
            IcedDrink(x-1, y)
            IcedDrink(x, y-1)
            IcedDrink(x+1, y)
            IcedDrink(x, y+1)
            return True    
        return False
    
    for i in range(len(ice)):
        for j in range(len(ice[0])):
            result = IcedDrink(i,j)
            if result == True:
                answer += 1
    return answer

start = time.time() 
print(solution(ice))
end = time.time() 
print(f"{end - start:.5f} sec")



        




