
N = int(input())

words = []
for _ in range(N):
    word  = input()
    l = len(word)
    words.append((l,word))
words = set(words)
words = sorted(words, key = lambda words : (words[0], words[1]))

for word in words:
    print(word[1])

