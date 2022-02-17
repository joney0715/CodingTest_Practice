N= int(input("input paid money  :")) #손님이 낸 금액

coins = [500, 100, 500, 10] #거스름돈으로 내줄 동전 종류
count = 0 # 동전 수

for coin in coins:
    count += N // coin # 큰 동전부터 카운트
    N %= coin

print(count)