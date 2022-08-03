N, K = map(int, input().split())
students = []
for i in range(N):
    s, y = map(int, input().split())
    students.append((s, y))

rooms = [0] * 12
for student in students:
    if student[0] == 0:
        rooms[student[1] -1 + 6] += 1
    else:
        rooms[student[1] -1] += 1
        
num_room = len(rooms) - rooms.count(0)
for room in rooms:
    if room > 2:
        num_room += room // K
print(num_room)


# import math

# N, K = map(int, input().split())
# student = [[0] * 7 for _ in range(3)] #성별 / 학년별

# for _ in range(N):
#     S, Y = map(int, input().split())
#     student[S][Y] += 1
        
# room = 0
# for i in student:
#     for j in i:
#         room += math.ceil(j / K)
# print(room)