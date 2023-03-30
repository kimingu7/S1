T = int(input())

for tc in range(1,T+1):
    number, count = input().split()
    count = int(count)
    nums = set([number])
    money = set()
    for _ in range(count):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(number)):
                for j in range(i+1, len(number)):
                    n[i], n[j] = n[j], n[i]
                    money.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
    answer = max(money)
    print(f'#{tc}',answer)
    
# count 횟수만큼 교환을 진행해서 그 경우를 money에 저장 (모든 경우의 수가 저장됨)
# money의 최대값이 정답이 됨
# 이 때, 모든 경우의 수를 구하기 때문에 메모리가 매우 커짐
# set을 활용하여 교환해 나온 숫자 중 중복되는 경우를 제거함