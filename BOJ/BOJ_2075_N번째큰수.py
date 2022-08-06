import heapq

N = int(input())
heap = []
row = list(map(int, input().split()))
for i in row:
    heapq.heappush(heap, i)

for _ in range(1,N):
    row = list(map(int, input().split()))
    row.sort()
    for j in row:   
        if j > heap[0]:
            heapq.heappush(heap, j)
            heapq.heappop(heap)

print(heap[0])