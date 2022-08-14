N = int(input())

l_list = []
for _ in range(N):
    start, end = map(int, input().split())
    l_list.append((start, end))

l_list = sorted(l_list, key=lambda l: (l[1],l[0]))

count = 1
end = l_list[0][1]
for i in range(1,N):
    if l_list[i][0] >= end:
        count +=1
        end = l_list[i][1]

print(count)
