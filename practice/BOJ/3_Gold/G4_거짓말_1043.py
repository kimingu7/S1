n, m = map(int, input().split())
truth = set(input().split()[1:])
parties = []
for i in range(m):
    parties.append(set(input().split()[1:]))

for i in range(m):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

cnt = 0
for party in parties:
    if party & truth:
        continue
    else :
        cnt+=1

print(cnt)

# 분리 집합을 활용해 푸는 문제
# truth의 원소 중 하나와 같은 party에 속한 원소 또한 truth에 추가해줘야함
# union 함수를 이용해 해당 