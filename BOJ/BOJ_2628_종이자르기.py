
W, H = map(int, input().split())
N = int(input())

cut_w = [0,W]
cut_h = [0,H]
for _ in range(N):
    d, p = map(int, input().split())
    if d == 1:
        cut_w.append((p))
    else:
        cut_h.append((p))

# W, H = 10, 8
# N = 3
# cut_w = [0, 10, 4]
# cut_h = [0, 8, 3, 2]

cut_w.sort()
cut_h.sort()

S = []
for i in range(1,len(cut_w)):
    for j in range(1, len(cut_h)):
        s = (cut_w[i] - cut_w[i-1]) * (cut_h[j] - cut_h[j-1])
        S.append(s)

print(max(S))