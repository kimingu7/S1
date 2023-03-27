h, w = map(int, input().split())
block = list(map(int, input().split()))
raindrop = 0
temp = 0
max_h = 0
for i in range(w):
    if max_h < block[i]:
        max_h = block[i]
        max_idx = i

for i in range(max_idx):
    if block[i] > temp:
        temp = block[i]
    raindrop+=(temp - block[i])
temp = 0
for i in range(w-1,max_idx,-1):
    if block[i] > temp:
        temp = block[i]
    raindrop+=(temp - block[i])
if raindrop == max_h:
    ans = 0
else :
    ans = raindrop
print(ans)

# 창고다각형과 같은 방식으로 풀면 됨
# 주의할 점은 temp에 block[i]를 뺀만큼만 더해야한다는 것