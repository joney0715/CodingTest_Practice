# 4873_반복문자지우기
# 2022-08-18

T = int(input())

for tc in range(1, T+1):
    word = input()
    
    t = 0
    while True:
        cnt = 0
        for _ in word:
            cnt += 1

        word = list(word)

        for i in range(1,cnt):
            if word[i-1] == word[i]:
                word[i-1] = ''
                word[i] = ''
        word = ''.join(word)

        if t == cnt:
            break
        t = cnt
        
    print('#{}'.format(tc), cnt)