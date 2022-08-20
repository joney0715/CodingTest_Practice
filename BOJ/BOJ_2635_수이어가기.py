N = int(input())

max_value = 0
answer = []
for i in range(1,N+1):
    N_list = [N, i]
    n = N - i
    cnt = 2
    while n >= 0:
        N_list.append(n)
        cnt += 1
        n = N_list[-2] - N_list[-1]

    if max_value <= cnt:
        max_value = cnt
        answer = N_list

print(max_value)
print(*answer)
