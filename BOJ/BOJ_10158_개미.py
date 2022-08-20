w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = t - (w - p)
if (a // w) % 2:
    p = a % w
else:
    p = w - (a % w)

b = t - (h - q)
if (b // h) % 2:
    q = b % h
else:
    q = h - (b % h)
print(p, q)