
mapping = [[0]*100 for _ in range(101)]

for i in range(4):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for x in range(x_2 - x_1):
        for y in range(y_2 - y_1):
            if mapping[y_1 + y][x_1 + x] == 0:
                mapping[y_1 + y][x_1 + x] = 1

count = 0
for row in mapping:
    count += row.count(1)
print(count)