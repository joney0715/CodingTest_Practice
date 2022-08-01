
from tkinter.tix import InputOnly


Input = [10,20,25,30,50]
T = 30

def solution(Input,T):
    for i in range(len(Input)):
        if Input[i]%T == 0:
            Input[i] = 0
        else:
            Input[i] = T - Input[i]%T

    answer = Input
    return answer

print(solution(Input,T))