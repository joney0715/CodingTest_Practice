# 5356_의석이의 세로로 말해요
# 2022-08-16

T = int(input())

def word_len(word):
    cnt = 0
    for _ in word:
        cnt += 1
    return cnt

for tc in range(1, T+1):    
    words = [input() for _ in range(5)]

    max_len = 0
    for i in range(5):
        cnt = word_len(words[i])
        if max_len < cnt:
            max_len = cnt
             
    answer = ''
    for i in range(max_len):
        for j in range(5):
            if i < word_len(words[j]):
                answer += words[j][i]

    print('#{} {}'.format(tc, answer))

