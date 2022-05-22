#여러 개의 노드가 있을 때
#특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
#양의 간선만 있을때 가능
import math
import time 
import random

#노드 개수
#이하 반복문에서 n+1을 하는 이유는 노드 번호와 리스트의 번호를 일치 시키기 위해서임
n = 6
# 간선 개수
m = 11

#시작 노드 정의
start = 1

#방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n + 1)

#초기값으로 모든 거리가 무한이라고 정의
INF = int(1e9)
distance = [INF] * (n + 1)

#각 노드와 노드에 연결된 노드에 대한 정보를 담은 리스트
#graph[i]노드에서 graph[i](연결된 노드, 간선 길이)
graph = [[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)],[]]

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_distance():
    #초기값으로 최단 거리가 무한이라고 가정
    min_value = INF
    #가장 최단 거리가 짧은 노드를 인덱스라 정의
    index = 0

    #노드를 하나씩 확인
    for i in range(1,n+1):
        #i노드의 거리가 최단 거리보다 짧은 경우
        #그리고 방문하지 않은 경우
        if distance[i] < min_value and not visited[i]:
            #최단 거리를 초기화
            min_value = distance[i]
            #인덱스를 i노드로 교체
            index = i

    #인덱스 출력
    return index

def dijkstra(start):
    #시작 노드의 거리 초기화
    #자기 자신의 노드 거리는 0
    distance[start] = 0
    #시작 노드 방문 처리
    visited[start] = True

    #시작 노드와 연결된 노드들의 최단 거리 초기화
    #시작 노드가 1인 경우, 노드2가 거리 2, 노드3이 거리5, 노드4가 거리1
    for j in graph[start]:
        distance[j[0]] = j[1]

    #시작 노드를 제외한 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #최단 거리중에 가장 짧은 노드를 검출
        #시작 노드가 1인 경우, 1은 방문 처리이므로 제외, 2,3,4 중에는 4가 가장 짧음
        #나머지 노드는 거리가 무한인 채로 있기 때문에 제외
        now = get_smallest_distance()

        #가장 짧은 최단 거리가 방문 처리
        visited[now] = True

        #가장 짧은 최단 거리를 가진 노드와 연결된 노드들을 확인
        #시작 노드가 1인 경우 노드4와 연결된 노드들을 확인
        for j in graph[now]:
            #가장 짧은 최단 거리를 가진 노드를 거쳐 다음 노드로 가는 거리 계산
            cost = distance[now] + j[1]
            #가장 짧은 최단 거리를 가진 노드를 거쳐 다음 노드로 가는 거리가 기존의 방법보다 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#dijkstra의 return은 없지만 이 함수를 실행하면 무한으로 정의돼있던 distance가 실제 거리로 바뀜
timestart = time.time() 
dijkstra(start)
end = time.time() 
print(f"{end - timestart:.5f} sec")

#시작 노드에서 모든 노드로 가는 최단 거리를 출력
#노드0은 없으므로 리스트에서 0번째 요소는 삭제
del distance[0]
print(distance)




