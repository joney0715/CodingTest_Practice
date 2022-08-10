# 1208_Flatten
# 2022-08-09

def min_max(box):
    idx_max = idx_min = 0
    for i in range(100):
        if box[i] > box[idx_max]:
            idx_max = i
        if box[i] < box[idx_min]:
            idx_min = i
    return idx_max, idx_min

T = 10

for tc in range(1, T+1):
    dump = int(input())
    box = list(map(int, input().split()))
    for _ in range(dump):
        
        # 최대값과 최소값 구하기
        idx_max, idx_min = min_max(box)
        
        box[idx_max] -= 1
        box[idx_min] += 1

        if box[idx_max] == box[idx_min] or abs(box[idx_max] - box[idx_min]) == 1:
            break

    idx_max, idx_min = min_max(box)
    print('#{} {}'.format(tc, box[idx_max] - box[idx_min]))
        

            