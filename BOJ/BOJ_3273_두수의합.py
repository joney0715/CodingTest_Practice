N = int(input())

N_list = list(map(int, input().split()))
N_list.sort()
target = int(input())

count = 0
start = 0
end = N-1
while end > start:
    if N_list[start] + N_list[end] == target:
        count += 1
        start += 1
    elif N_list[start] + N_list[end] > target:
        end -= 1
    else:
        start += 1

print(count)