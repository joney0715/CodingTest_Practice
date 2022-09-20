import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    num_b = list(input().rstrip())
    num_th = list(input().rstrip())

    flag = 0
    for i in range(len(num_b)):
        num_b_c = num_b[:]
        num_b_c[i] = str(1 - int(num_b_c[i]))
        for j in range(len(num_th)):
            for k in range(1,3):
                num_th_c = num_th[:]
                num_th_c[j] = str((int(num_th_c[j]) + k)%3) 
                num_th_c = num_th_c[::-1]

                num_b_c = ''.join(num_b_c)
                num_1 = int(num_b_c, 2)

                num_2 = 0
                for p in range(len(num_th_c)):
                    num_2 += int(num_th_c[p]) * 3**p

                if num_1 == num_2:
                    flag = 1
                    answer = num_1
                    break
        
            if flag:
                break
        if flag:
            break
        
    print('#{}'.format(tc),answer)

