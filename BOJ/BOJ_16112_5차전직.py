import sys

n, k = map(int, sys.stdin.readline().split())

quest = list(map(int, sys.stdin.readline().split()))
quest = sorted(quest)

exp = 0
for i in range(1,n):
    if i < k:
        exp += quest[i]*i
    else:
        exp += quest[i]*k

print(exp)
