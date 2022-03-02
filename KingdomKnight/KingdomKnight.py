
first_value = input()
row = int(first_value[1])
column = int(ord(first_value[0])) - int(ord("a")) + 1

moving_case = [[1,2],[2,1],[-1,2],[2,-1],[-1,-2],[-2,-1],[1,-2],[-2,1]]

count = 0
for move in moving_case:
    position = [column - move[0], row - move[1]]
    if position[0] >= 1 and position[1] >= 1 and position[0] <= 8 and position[1] <= 8 :
        count += 1

print(count)
