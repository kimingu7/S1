def abc(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (abc(a,b//2,c)**2)%c
    else:
        return ((abc(a,b//2,c)**2)*a)%c

a, b, c = map(int, input().split())
print(abc(a, b, c))

# 분할정복을 사용해 문제를 풀어야함
# b의 값이 1보다 클 때 b를 계속 2로 나눠 계산 과정을 줄임
# 안그러면 시간초과 뜸
# 거듭제곱을 분할정복에 싸서드셔보세요