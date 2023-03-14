n = int(input())
m = int(input())
min_count = abs(100 - n)

if m:
    buttons = set(input().split())
else:
    buttons = set()

for number in range(1000001):
    for N in str(number):
        if N in buttons:
            break
    else :
        min_count = min(min_count, abs(number - n) + len(str(number)))

print(min_count)

# 리모컨이 고장났으면 새거 좀 사라
# 1000000까지 모든 수에 대해서 체크함(500000의 2배)
# 해당 번호가 눌러서 만들 수 없을 때 break
# 번호를 눌러서 만든 경우 번호를 누른 횟수에 타겟까지의 차이를 구함