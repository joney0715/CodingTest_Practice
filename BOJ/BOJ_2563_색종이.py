N = int(input())
mapping = [[0]*100 for _ in range(101)]

for i in range(N):
    L, H = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if mapping[H+i][L+j] == 0:
                mapping[H+i][L+j] = 1

count = 0
for row in mapping:
    count += row.count(1)
print(count)