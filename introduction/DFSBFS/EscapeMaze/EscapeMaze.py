
m = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

def solution(m):
    position = []

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    N = len(m)
    M = len(m[0])

    def moving(x,y):
        position.append((x,y))
        
        #큐가 빌때까지 반복처리 while문 기억해둘것
        while len(position) > 0:    
            #큐에서 요소 추출 뒤 위치 초기화
            x,y = position.pop(0)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #범위아웃인 경우
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue

                #괴물 등장
                if m[nx][ny] == 0:
                    continue

                if m[nx][ny] == 1:
                    m[nx][ny] = m[x][y] + 1
                    position.append((nx,ny))
                
        return m[N-1][M-1]
    
    answer = moving(0,0)

    return answer

print(solution(m))



    
    