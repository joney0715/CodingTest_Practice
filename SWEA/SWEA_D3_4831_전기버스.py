# 4828 전기 버스 풀이
# 2022-08-09

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = [0]
    charge.extend(list(map(int, input().split())))
    charge.append(N)

    count = 0
    k = K
    for i in range(1, M+1):
        # i충전소에 도착했을 때 잔여량
        k -= charge[i] - charge[i-1]

        # 다음 충전소 까지의 거리
        next_charge = charge[i+1] - charge[i]      

        # 다음 충전소까지 완충해도 못가는 경우
        # 첫 충전소까지도 못 가는 경우
        # count를 0으로 초기화
        if next_charge > K or k < 0:
            count = 0
            break

        # 잔여량으로 다음 충전소까지 못 가는 경우
        # 충전을 하면 다음 충전소까지 갈 수 있는 경우
        # 충전 필요
        if next_charge > k and next_charge <= K:
            count += 1
            k = K
        
    print('#{}'.format(tc), count)        
