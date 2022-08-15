N = int(input())

cow_list = []
for _ in range(N):
    a, b = map(int, input().split())
    cow_list.append((a,b))

cow_list = sorted(cow_list, key=lambda x : (x[0], x[1]))

end = 0
for cow in cow_list:
    if end <= cow[0]:
        end = cow[0] + cow[1]
        continue
    else:
        end += cow[1]
print(end)

