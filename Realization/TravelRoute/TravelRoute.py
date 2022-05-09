
N = int(input()) #공간 크기 입력
x, y = 1, 1 #초기위치

#이동 계획 입력
Route = input().split()

for plan in Route:
    #입력 계획 대로 이동
    if plan == "L":
        dx, dy = -1, 0
    elif plan == "R":
        dx, dy = 1, 0
    elif plan == "U":
        dy, dy = 0, 1
    elif plan == "D":
        dy, dy = 0, -1
    
    else: #LRUD이외의 값 입력시
        print("Input param" + plan + "is wrong!")
    print(x, y)
    if x+dx > N or y+dy > N or x+dx < 1 or y+dy < 1:
        continue
    else:
        x, y = x+dx, y+dy

print(x, y)

    

