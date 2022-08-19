# 4873_반복문자지우기
# 2022-08-18

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    
    length = 0
    for _ in word:
        length += 1

    stack = [word[0]]
    for i in range(1,length):
        if stack:
            if word[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])
        
    answer = 0
    for _ in stack:
        answer += 1
        
    print('#{}'.format(tc), answer)