t = int(input())

def boyermoore(b,a):
    m = len(b)
    n = len(a)
    i = 0
    cnt = 0
    while i <= n-m:
        j = m-1
        while j >= 0:
            if b[j] != a[i+j]:
                move = find(b,a[i+m-1])
                break
            j = j-1
        if j == -1:
            cnt+=1
            i+=m
        else :
            i+=move
    return cnt

def find(b, char):
    for i in range(len(b)-2,-1,-1):
        if b[i] == char:
            return len(b)-i-1
    return len(b)

for i in range(t):
    a, b = input().split()
    cnt = boyermoore(b,a)
    f_len = len(a)-(len(b)*cnt)+cnt
    print(f'#{i+1} {f_len}')

# 보이어-무어 알고리즘을 이용해 찾고자 했음
# 구현 자체는 인터넷을 참고했기에 어렵지 않았으나
# aaa에서 aa가 두번 확인되는 문제가 있었음
# 이를 해결하기 위해 동일한 문자열이 확인되면 강제로 인덱스를 target의 길이만큼 증가시켜서 확인함
# 최종길이는 a의 길이에서 b의 길이에 cnt값을 곱한 값을 빼고(이게 중복 문자열이 아닌 글자의 타이핑 수)
# cnt 값을 더해줌(이게 중복된 문자열의 타이핑 수)