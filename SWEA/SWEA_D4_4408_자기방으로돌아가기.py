
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    students = [tuple(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 201
    
    for student in students:
        if student[0] <student[1]:
            start = (student[0]+1) // 2
            end = (student[1]+1) // 2
        else:
            start = (student[1]+1) // 2
            end = (student[0]+1) // 2
        for j in range(start,end+1):
            corridor[j] += 1

    answer = corridor[0]
    for j in range(201):
        if corridor[j] > answer:
            answer = corridor[j]

    print('#{}'.format(tc), answer)
