
#지도 사이즈 입력
n, m = map(int, input().split()) 

#초기 위치 입력(0:북, 1:동, 2:남, 3:서)
x, y, d = map(int, input().split())

#지도 설정(0:육지, 1: 바다)
row = []
for i in range(n):
    row.append(list(map(int, input().split()[ :m])))

#방문위치 설정
v = [[0]*m for j in range(n)]
#캐릭터의 초기위치가 맵안의 육지에 있는 경우만 처리
if x < n and y < m and row[x][y] == 0:
    #초기위치 방문 처리(1: 방문, 0: 미방문)
    v[x][y] = 1
else:
    print("캐릭터의 위치가 옳지 않습니다")
    exit()

#이동정의
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

#시뮬시작
count = 1
turn = 0
while True:
    #왼쪽으로 회전
    d = (d + 3)%4
    turn += 1
    if turn < 5:
        #이동방향 검사
        if v[x+dx[d]][y+dy[d]] == 0 and row[x+dx[d]][y+dy[d]] == 0:
            #캐릭터 이동
            x = x + dx[d]
            y = y + dy[d]
            count += 1
            #회전횟수 초기화
            turn = 0
            #방문처리
            v[x][y] = 1
    #사방이 바다거나, 방문 완료인 경우   
    else:
        if row[x-dx[d]][y-dy[d]] == 0:
            x = x - dx[d]
            y = y - dx[d]
        else:
            break
print(count)
        







