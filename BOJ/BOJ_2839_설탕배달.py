N = int(input())

count = 0
if N % 5 == 0:
    count += N // 5
    print(count)
else:
    while True:
        N -= 3
        count += 1
        if not N % 5:
            count += N // 5
            print(count)
            break
        elif not N:
            print(count)
            break
        elif N < 0:
            print(-1)
            break