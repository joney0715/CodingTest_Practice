w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

d_p = [1, -1, -1, -1]
d_q = [1, 1, -1, 1]

d = 0
while t > 0:
    if (p+d_p[d] > w and q+d_q[d] > h) or (p+d_p[d] < 0 and q+d_q[d] < 0):
        d = (d+2) % 4
        p += d_p[d]
        q += d_q[d]
    elif (p+d_p[d] > w and q+d_q[d] < 0) or (p+d_p[d] < 0 and q+d_q[d] > h):
        d = (d+2) % 4
        p += d_p[d]
        q += d_q[d]
    elif p+d_p[d] < 0 or p+d_p[d] > w or q+d_q[d] < 0 or q+d_q[d] > h:
        d = (d+1) % 4
        p += d_p[d]
        q += d_q[d]
    else:
        p += d_p[d]
        q += d_q[d]
    t -= 1

print(p, q)