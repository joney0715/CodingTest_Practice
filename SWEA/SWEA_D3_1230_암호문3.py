import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def I(i, n_list):
    # 인덱스 주의
    idx = int(M_list[i+1])
    f = n_list[0:idx]
    b = n_list[idx:len(N_list)]

    insert_num = []
    for ii in range(int(M_list[i+2])):
        insert_num.append(int(M_list[i+3+ii]))

    f.extend(insert_num)
    f.extend(b)
    return f

def D(i, n_list):
    # 인덱스 주의
    idx = int(M_list[i + 1]) + int(M_list[i + 2])

    f = n_list[0:idx]
    b = n_list[idx:len(N_list)]

    for _ in range(int(M_list[i + 2])):
        f.pop()

    f.extend(b)
    return f

def A(i, n_list):
    result = n_list[:]
    for a in range(int(M_list[i + 1])):
        result.append(int(M_list[i + 2 + a]))

    return  result

for tc in range(1, 2):
    N = int(input())
    N_list = list(map(int, input().split()))

    M = int(input())
    M_list = list(input().split())

    # print(N_list)
    for m in range(len(M_list)):
        if M_list[m].isdigit():
            continue
        elif M_list[m] == 'I':
            N_list = I(m, N_list)
        elif M_list[m] == 'A':
            N_list = A(m, N_list)
        elif M_list[m] == 'D':
            N_list = D(m, N_list)
        # print(N_list)

    print('#'+str(tc), *N_list[:10])
