# 1216_회문2
# 2022-08-16
import sys

sys.stdin = open('input.txt', 'r')

T = 10

for _ in range(1, T+1):
    tc = int(sys.stdin.readline())
    mapping = [sys.stdin.readline() for _ in range(100)]

    answer = 1
    for i in range(2,100):
        for y1 in range(100):
            for x1 in range(100-i+1):
                if mapping[y1][x1:x1 + i] == mapping[y1][x1:x1 + i][::-1]:
                    answer = i

        for x2 in range(100):
            for y2 in range(100-i+1):
                temp = ''
                for k in range(i):
                    temp += mapping[y2+k][x2]
                if temp == temp[::-1]:
                    answer = i
                    break
    print('#{}'.format(tc), answer)