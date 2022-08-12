# 4839_이진탐색
# 2022-08-11

T = int(input())

def binary_search(start, end, p, i):
    if start > end:
        return i
    i += 1
    c = (start+end)//2
    if c == p:
        return i
    elif c > p:
        return binary_search(start, c, p, i)
    else:
        return binary_search(c, end, p, i)

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    a = binary_search(1, P, Pa, 0)
    b = binary_search(1, P, Pb, 0)

    if a < b:
        print('#{} A'.format(tc))
    elif b < a:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))

    


