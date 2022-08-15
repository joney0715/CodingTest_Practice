import sys
N = int(input())

X_list = list(map(int, input().split()))
X_sort = sorted(set(X_list))

answer = dict()
for i in range(len(X_sort)):
    answer[X_sort[i]] = i

for j in range(N):
    print(answer.get(X_list[j]), end=' ')