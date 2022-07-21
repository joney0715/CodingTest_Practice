
#N = int(input())
n = 1001
LH = [0] * n
# for i in range(N):
#     l, h = map(int, input().split())
#     LH[l] = h
LH[2] = 4
LH[11] = 4
LH[15] = 8
LH[4] = 6
LH[5] = 3
LH[8] = 10
LH[13] = 6

H_max = max(LH)
id_max = 0
for idx in range(n):
    if LH[idx] == H_max:
        id_max = idx
        break
   
answer = H_max
h_r = 0
for i in range(n-1, id_max, -1):
    if LH[i] > h_r:
        h_r = LH[i]
    answer += h_r

h_l = 0
for j in range(0, id_max):
    if LH[j] > h_l:
        h_l = LH[j]
    answer += h_l

print(answer)








