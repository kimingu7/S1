k = int(input())
width = []
height = []
field = []
for i in range(6):
    dir, dist = map(int, input().split())
    if dir == 1 or dir == 2:
        width.append(dist)
        field.append(dist)
    else :
        height.append(dist)
        field.append(dist)

big_area = max(width) * max(height)
maxh = field.index(max(height))
maxw = field.index(max(width))
small_height = abs(field[maxh-1] - field[(maxh-5 if maxh == 5 else maxh+1)])
small_width = abs(field[maxw-1] - field[(maxw-5 if maxw == 5 else maxw+1)])
small_area = small_height * small_width
area = big_area - small_area
melon = area * k
print(melon)

# 큰 사각형에서 작은 사각형을 빼는 문제
# 작은 사각형의 가로 세로를 파악하는 것이 중요