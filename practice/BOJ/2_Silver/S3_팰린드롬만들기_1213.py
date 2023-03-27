from collections import Counter
hansoo = list(input())
hansoo.sort()
cnt_hansoo = Counter(hansoo)
center = ''
odd_cnt = 0
for i in cnt_hansoo:
    if cnt_hansoo[i] % 2 != 0:
        odd_cnt+=1
        center+=i
        hansoo.remove(i)
    if odd_cnt > 1:
        break

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else :
    palindrom =''
    for i in range(0, len(hansoo), 2):
        palindrom += hansoo[i]
    print(palindrom + center + palindrom[::-1])

# 팰린드롬이란 회문을 의미함
# 팰린드롬을 만들기 위해서는
# 6글자일 때 0-2 index까지 출력하고, 3-5 index까지는 [::-1]을 통해 거꾸로 출력해주면 됨
# 7글자일 때는 가운데를 고려해 [::-1] 전에 가운데에 와야할 문자를 출력
# 또한 홀수 개가 존재하는 문자가 가운데에 와야하므로 홀수 개인 문자가 여러 개일 경우 팰린드롬이 불가능함