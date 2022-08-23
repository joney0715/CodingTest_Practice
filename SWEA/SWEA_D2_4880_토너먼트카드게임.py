
def divide(start, end):
    if start == end:
        return start

    middle = (start + end) // 2

    i = divide(start, middle)
    j = divide(middle+1, end)

    return win(i, j)

def win(i, j):
    if N_list[i] == N_list[j]:
        return i
    elif N_list[i] - N_list[j] == 1 or N_list[i] - N_list[j] == -2:
        return i
    elif N_list[j] - N_list[i] == 1 or N_list[j] - N_list[i] == -2:
        return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    N_list = list(map(int, input().split()))

    winner = divide(0, N-1)
    print('#{}'.format(tc), winner+1)


