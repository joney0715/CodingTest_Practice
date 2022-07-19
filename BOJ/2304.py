'''
N = int(input())
LHs = [0] * 1001
for i in range(N):
    l, h = map(int, input().split())
    LHs[l] = h
'''

N = 7
LHs = [0,0,4,0,6,3,0,0,10,0,0,4,0,6,0,8]

def solution(LHs):
    H = 0
    s = 0
    L_past = 0
    for L in range(len(LHs)):
        if LHs[L] != 0:
            s += H * (L - L_past)
            L_past = L
            H = LHs[L]
        else:
            continue
    return s

print(solution(LHs))








