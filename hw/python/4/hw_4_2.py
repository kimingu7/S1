words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for i in range(len(words)-1):
    if words[i][-1] != words[i+1][0]:
        print(i)
for i in range(len(words)):
    for n in range(i+1,len(words)):
        if words[i] == words[n]:
            print(n)