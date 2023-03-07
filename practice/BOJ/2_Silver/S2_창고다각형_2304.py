n = int(input())

max_l = 0
max_h = 1
warehouse = 0
temp = 0
stack = []
for _ in range(n):
    l, h = map(int, input().split())
    stack.append([l,h])
    if max_l < l:
        max_l = l
    if max_h < h:
        max_h = h
        max_idx = l

pillar = [0 for _ in range(max_l + 1)]
for l, h in stack:
    pillar[l] = h
for i in range(max_idx + 1):
    if pillar[i] > temp:
        temp = pillar[i]
    warehouse += temp
temp = 0
for i in range(max_l, max_idx, -1):
    if pillar[i] > temp:
        temp = pillar[i]
    warehouse += temp
print(warehouse)

# 입력 값을 스택에 [l,h]의 리스트 형으로 저장
# 리스트에서 가장 큰 l를 max_l, 창고의 총 길이로 저장
# 리스트에서 가장 큰 h를 max_h로, 그 때의 l 값을 max_idx로 저장
# 기둥 중 가장 높은 위치인 max_idx를 기준으로
# 0부터 max_idx까지 커지는 값만 temp에 저장하고, temp만큼 warehouse에 더함
# max_idx부터 거꾸로 검사하며 커지는 값만 temp에 저장하고, temp만큼 warehouse에 더함