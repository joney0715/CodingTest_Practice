import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    N_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    N_list.sort()
    
    count = 1
    k = N_list[0][1]
    for i in range(1,N):
        if N_list[i][1] < k:
            count += 1
            k = N_list[i][1]

    print(count)