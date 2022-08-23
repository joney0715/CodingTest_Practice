
def min_sum(row, n_sum):
    global N_sum

    # 값이 더해지는 도중에 이미 더 큰 경우
    if n_sum > N_sum:
        return

    # 마지막 행에 도착 (재귀 종료 조건)
    if row == N:
        if n_sum < N_sum:
            N_sum = n_sum
            return

    for col in range(N):
        # 아직 방문하지 않은 열
        if not visit[col]:
            # 열 방문 이후 해당 열은 사용 못함
            visit[col] = True
            # 다음 행 재귀
            min_sum(row+1, n_sum + N_list[row][col])
            # 방문 초기화
            # 재귀에서 돌아왔을 때 다음 경우 계산을 위해 필요
            visit[col] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 처음 비교를 위해 가장 적당한 큰 값 넣기
    N_sum = 100000

    visit = [False] * N
    min_sum(0, 0)

    print('#{}'.format(tc), N_sum)
