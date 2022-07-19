#1~N까지의 회사가 있는 미래도시
#특정 회사끼기는 서로 도로를 통해 연결
#방판원이 1번 회사에 위치해서 X번째 회사에 판매하려고 함
#양뱡향 이동 가능
#판매 전에 K번째 회사에 들러야함
#회사간 이동은 정확히 1만큼 걸림
#갈 수 없는 곳이라면 -1 출력

#회사 갯수
#N = 5
N = 4
#도로 갯수
#M = 7
M = 2
#연결된 회사
#conneted = [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]
conneted = [[1,3],[2,4]]
#목적지, 경유지
#X, K = 4, 5
X, K = 3,4
#2차원 그래프 생성후 모든 요소를 무한으로 초기화
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

#자기 자신으로 가는 경로는 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

#경로를 참조해서 그래프 초기화
#거리는 1이고 양방향으로 갈 수 있다는 점 주의
for i in conneted:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

#플로이드 알고리즘으로 최단거리를 초기화
for i in range(1, N+1):
    for x in range(1, N+1):
        for y in range(1, N+1):
            graph[x][y] = min(graph[x][y], graph[x][i]+graph[i][y])

#경유지를 고려한 목적지까지의 거리
answer = graph[1][K] + graph[K][X]
if answer >= INF:
    answer = -1

print(answer)