N = int(input())
words = []
for i in range(N):
    word = input()
    words.append(word)
words = list(set(words))
words.sort()
words.sort(key=len)
print(*words,sep='\n')