'''
기본적을 파리퇴치3과 유사한 문제
N x N의 넓이의 과수원이 있을 때 바이러스를 퇴치하기 위해서 약을 뿌림
약의 위력은 P이며 중심으로 부터 P만큼 십자가로 살포되거나 엑스자 형태로 살포됨
N, P, 과수윈의 구역별 바이러스 숫자가 주어졌을 때, 가장 많은 바이러스가 죽은 케이스의 바이러스 숫자를 출력하는 문제
'''

import sys
sys.stdin = open('input_1.txt', 'r')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    # 과수원의 변의 길이, 약의 위력
    N, P = map(int, input().split())

    # 과수원 구역별 바이러스 숫자
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 죽은 바이러스 숫자를 넣을 리스트
    value = []
    # 구역 한개씩 조사
    for i in range(N):
        for j in range(N):
            # 십자
            value_1 = N_list[i][j]
            # 대각
            value_2 = N_list[i][j]

            # 십자
            for p in range(1, P+1):
                if j+p < N:
                    value_1 += N_list[i][j+p]
                if j-p >= 0:
                    value_1 += N_list[i][j-p]
                if i+p < N:
                    value_1 += N_list[i+p][j]
                if i-p >= 0:
                    value_1 += N_list[i-p][j]

            # 대각
            for q in range(1, P+1):
                if i+q < N and j+q < N:
                    value_2 += N_list[i+q][j+q]
                if i-q >= 0 and j-q >= 0:
                    value_2 += N_list[i-q][j-q]
                if i-q >= 0 and j+q < N:
                    value_2 += N_list[i-q][j+q]
                if i+q < N and j-q >= 0:
                    value_2 += N_list[i+q][j-q]

            value.append(value_1)
            value.append(value_2)

    # 최대값 탐색
    max_value = 0
    for v in value:
        if v > max_value:
            max_value = v

    print('#'+str(tc), max_value)