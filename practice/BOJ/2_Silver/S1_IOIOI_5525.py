import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
answer = i = count = 0

while i < m-1:
    if s[i:i+3] == 'IOI':
        i+=2
        count+=1
        if count == n:
            answer+=1
            count-=1
    else :
        i +=1
        count = 0
print(answer)

# 주어진 문장 s에서 IOI...의 문자열이 몇개 존재하는지 찾는 문제
# 처음에는 찾고자하는 문자열을 직접 만들었으나 시간 초과 발생
# 따라서 슬라이싱을 통해 시간 절약을 하고자 함
# s[i:i+3]이 n번 'IOI'가 반복된다면 answer을 1 증가시킴
# 이 때 i를 2칸씩 증가시켜야 IOI를 확인 가능
# count가 n일 때 count를 1만 감소시키는 이유는 연속해서 있는 경우를 고려했기 때문
# 예) n = 2, s = IOIOIOI라면 i가 3일 때 한번, 5일 때 한번 확인 가능하기 때문