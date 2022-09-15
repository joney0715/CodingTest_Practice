import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def postorder(node):
    
    if int(node) <= N:
        if len(N_list[node]) > 2:
            postorder(int(N_list[node][2]))
        if len(N_list[node]) > 2:
            postorder(int(N_list[node][3]))
        
        stack.append(N_list[node][1])
        
        if len(stack) >= 3 and not str(stack[-1]).isdigit():
            cal = stack.pop()
            if cal == '-':
                a = stack.pop()
                b = stack.pop()
                ans = int(b) - int(a)
                stack.append(ans)
            if cal == '+':
                a = stack.pop()
                b = stack.pop()
                ans = int(b) + int(a)
                stack.append(ans)
            if cal == '/':
                a = stack.pop()
                b = stack.pop()
                ans = int(b) // int(a)
                stack.append(ans)
            if cal == '*':
                a = stack.pop()
                b = stack.pop()
                ans = int(b) * int(a)
                stack.append(ans)


T = 10
for tc in range(1, T+1):
    N = int(input())

    N_list = [0] * (N+1)
    for i in range(N):
        n_list = list(input().split())
        N_list[int(n_list[0])] = n_list
    
    stack = []
   
    postorder(1)

    print('#{}'.format(tc), stack[-1])
