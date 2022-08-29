
N, M = map(int, input().split())

card = list(map(int, input().split()))

max_value = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            n = card[i] + card[j] + card[k]
            if n <= M:
                if max_value < n:
                    max_value = n

print(max_value)