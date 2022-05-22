import math
import time 
import random

N = 50
Input = []
for i in range(N):
    num = random.randint(0,5)
    Input.append(str(num))


def solution(Input):
    #직접 만든 코드
    """
    Input = [int(i) for i in Input]
    result = 0
    for i in range(len(Input)):
        if Input[i] == 0 or Input[i] == 1:
            result += Input[i]
        else:
            if result != 0 and result != 1:
                result *= Input[i]
            else:
                result += Input[i]
    """
    #해답지
    #접근 방법은 같았지만 해답지가 더 깔끔한 코드
    #첫 숫자는 무조건 더하기로 들어가기 때문에 초기 결과값은 첫 숫자로 초기화
    result = Input[0]
    for i in range(1,len(Input)):
        num = int(Input[i])
        #다음 숫자가 0,1 이거나 현재 결과값이 0,1인 경우는 더하기
        if num <= 1 or result <= 1:
            result += num
        #그 외는 전부 곱하기
        else:
            result *= num
    
    return result

start = time.time() 
print(solution(Input))
end = time.time() 
print(f"{end - start:.5f} sec")