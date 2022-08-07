import heapq
import sys

def delete(que, v):
    while que and not v[que[0][1]]:
        heapq.heappop(que)

T = int(input())

for _ in range(T):
    N = int(input())
    que_min = []
    que_max = []
    visit = [False] * N

    for i in range(N):
        s, n = sys.stdin.readline().split()

        if s == 'I':
            heapq.heappush(que_min, (int(n), i))
            heapq.heappush(que_max, (-int(n), i))
            visit[i] = True

        else:
            if n == '1':
                delete(que_max, visit)
                if que_max:
                    visit[que_max[0][1]] = False
                    heapq.heappop(que_max)
            else:
                delete(que_min, visit)
                if que_min:
                    visit[que_min[0][1]] = False
                    heapq.heappop(que_min)
                    
    delete(que_max, visit)
    delete(que_min, visit) 

    if not que_min or not que_max:
        print("EMPTY")
    else:
        print(-que_max[0][0], que_min[0][0])