T = int(input())

for _ in range(T):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]
    A.sort()
    B.sort()

    while len(A) and len(B):
        a = A.pop()
        b = B.pop()

        if a == b:
            if not len(A) and not len(B):
                print('D')
                break
            elif not len(A) and len(B):
                print('B')
                break
            elif len(A) and not len(B):
                print('A')
                break
            else:
                pass
        else:
            if a > b:
                print('A')
                break
            elif a < b:
                print('B')
                break
                    


