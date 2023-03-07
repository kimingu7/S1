t = int(input())
for i in range(t):
    n = int(input())
    factors = [0] * 5
    while n > 1:
        if n % 2 == 0:
            factors[0]+=1
            n = n//2
        elif n % 3 == 0:
            factors[1]+=1
            n = n//3
        elif n % 5 == 0:
            factors[2]+=1
            n = n//5
        elif n % 7 == 0:
            factors[3]+=1
            n = n//7
        elif n % 11 == 0:
            factors[4]+=1
            n = n//11
    print(f'#{i + 1} {" ".join(map(str, factors))}')

# 문제에서 2 3 5 7 11로 하라해서 그거만 줌
# 2로 나눠지면 factors[0]에 1 3으로 나눠지면 [1]에 1 ... 11로 나눠지면 [4]에 1을 더함
# 최종으로 join을 이용해서 출력