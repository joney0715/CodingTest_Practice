def coordinate(d,p):
    if d == 1:
        return p,hight
    elif d == 2:
        return p,0
    elif d ==3:
        return 0,hight-p
    else:
        return width,hight-p

width, hight = map(int, input().split())
store = int(input())
stores = []
for _ in range(store):
    d, p = map(int, input().split())
    stores.append(coordinate(d,p))

position = tuple(map(int, input().split()))
position = coordinate(position[0], position[1])

answer = 0
for store in stores:
    x = abs(position[0] - store[0])
    y = abs(position[1] - store[1])

    if x == width:
        a = min(position[1]+width+store[1], 2*hight-(position[1]+store[1])+width)
        answer += a
    elif y == hight:
        a = min(position[0]+hight+store[0], 2*width-(position[0]+store[0])+hight)
        answer += a
    else:
        a = x+y
        answer += a

print(answer)