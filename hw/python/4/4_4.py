word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')
ascii1 = ascii2 = 0

for i in word1:
    ascii1 = ascii1 + ord(i)
for i in word2:
    ascii2 = ascii2 + ord(i)

if ascii1 > ascii2:
    print(word1)
else :
    print(word2)