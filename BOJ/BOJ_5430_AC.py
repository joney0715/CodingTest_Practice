T = int(input())

for _ in range(T):
    F = input()
    N = int(input())
    numbers = input()
    numbers = numbers[1:-1].split(',')
    
    if not N:
        numbers = []

    R = 0
    for f in F:
        if f == 'R':
            R += 1
        else:
            if not len(numbers):
                print('error')
                break
            
            else:
                if not R % 2:
                    numbers.pop(0)
                else:
                    numbers.pop()
    else:
        if R % 2:
            numbers.reverse()
            print('['+','.join(numbers)+']')
        else:
            print('['+','.join(numbers)+']')

'''
T = int(input())

for _ in range(T):
    F = input()
    N = int(input())
    numbers = input()
    numbers = numbers[1:-1].split(',')
    
    if not N:
        numbers = []
    R = 0
    for f in F:
        if f == 'R':
            R += 1
        else:
            if not len(numbers):
                break
            
            else:
                if R % 2:
                    numbers.pop()
                else:
                    numbers.pop(0)

    if len(numbers):
        if R % 2:
            numbers.reverse()
            print('['+','.join(numbers)+']')
        else:
            print('['+','.join(numbers)+']')
    else:
        print('error')
'''
'''
위 코드가 안되는 반례
1
D
1
[1]
답: []
출력: error

경계값을 조심하자
'''