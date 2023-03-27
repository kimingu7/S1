x, y = map(int, input().split())
rev_x = int(str(x)[::-1])
rev_y = int(str(y)[::-1])
rev_xy = rev_x + rev_y
xy = int(str(rev_xy)[::-1])
print(xy)