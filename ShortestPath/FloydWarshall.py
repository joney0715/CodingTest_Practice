#모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야하는 경우
import math
import time 
import random
#노드 개수
#이하 반복문에서 n+1을 하는 이유는 노드 번호와 리스트의 번호를 일치 시키기 위해서임
n = 4
# 간선 개수
m = 7

#무한의 정의
INF = int(1e9)

#2차원(n+1 * n+1) 리스트로 그래프를 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#그래프안에서 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0

#각 간선에 대한 정보 정의
#a노드에서 b노드로 가는 비용을 c라고 설정
graph[1][2],graph[1][4],graph[2][1],graph[2][3],graph[3][1],graph[3][4],graph[4][3] = 4,6,3,7,5,4,2

#플로이드 알고리즘 수행
#x에서 y로 바로 가는 경로와 i를 경유해서 x에서 y로 가는 경로를 비교해서 최단 거리를 선택
for i in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][i] + graph[i][y])

#결과 출력
#편의상 만든 0번째 리스트 삭제
del graph[0]
for i in graph:
    del i[0]
print(graph)