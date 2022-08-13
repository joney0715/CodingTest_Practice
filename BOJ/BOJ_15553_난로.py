N, K = map(int, input().split())

t1 = int(input())
k_need = 1
temp = []
on_time = 1
for _ in range(N-1):
    t = int(input())
    on_time += 1

    if t- t1 > 1:
        k_need += 1
        temp.append(t- t1-1)
    t1 = t

temp.sort()

if k_need <= K:
    print(on_time)
else:
    for i in range(k_need - K):
        on_time += temp[i]

    print(on_time)