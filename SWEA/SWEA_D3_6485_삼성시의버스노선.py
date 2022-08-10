
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    bus = []
    for i in range(N):
        A, B = map(int, input().split())
        bus.append((A, B))

    P = int(input())
    answer = [0] * P
    for j in range(P):
        C = int(input())

        for b in bus:
            if C in range(b[0],b[1]+1):
                answer[j] += 1

    print('#{}'.format(tc), *answer)