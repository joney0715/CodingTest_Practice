N = int(input())

nums = list(map(int, input().split()))

student = []
for i in range(N):
    if nums[i] == 0:
        student.append(i+1)
    else:
        student.insert(i-nums[i],i+1)
print(*student)