# 고정비용, 가변비용, 노트북 가격
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:   
    p = A // (C - B)
    print(p+1)