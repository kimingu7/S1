t = int(input())
for i in range(t):
    n = int(input())
    print(f'#{i+1}')
    doc = []
    for j in range(n):
        c, k = input().split()
        k = int(k)
        for l in range(k):
            doc.append(c)
    for j in range(len(doc)):
        if j > 0 and j%10 == 0:
            print()
            print(doc[j],end='')
        else :
            print(doc[j],end='')
    print('')

# 압축을 푸는건 어려운게 아니었지만 10번 출력마다 줄을 바꾸는게 어려웠음
# index가 10의 배수일 때마다 print()를 사용해 줄을 바꿔주도록 함
# 이 때 print()만 사용하는 실수를 했는데
# 9글자만 출력되기 때문에 반드시 줄바꿈 이후에도 문자를 출력해줄 것