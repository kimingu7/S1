def clockwise(ti,tj,hi,hj):
    global dist_cw
    dist_cw = 0
    while True:
        if ti == hi and tj == hj:
            return dist_cw
        if hi == 0 and hj < n:
            hj += 1
            dist_cw += 1
        elif hj == n and hi < m:
            hi += 1
            dist_cw += 1
        elif hi == m and hj > 0:
            hj -= 1
            dist_cw += 1
        elif hj == 0 and hi > 0:
            hi -= 1
            dist_cw += 1

def counter_clockwise(ti,tj,hi,hj):
    global dist_ccw
    dist_ccw = 0
    while True:
        if ti == hi and tj == hj:
            return dist_ccw
        if hi == 0 and hj > 0:
            hj-=1
            dist_ccw+=1
        elif hj == 0 and hi < m:
            hi+=1
            dist_ccw+=1
        elif hi == m and hj < n:
            hj+=1
            dist_ccw+=1
        elif hj == n and hi > 0:
            hi-=1
            dist_ccw+=1

n, m = map(int, input().split())
k = int(input())
shop = []
security = []
for i in range(k):
    dir, dist = map(int, input().split())
    if dir == 1:
        shop.append((0,dist))
    elif dir == 2:
        shop.append((m,dist))
    elif dir == 3:
        shop.append((dist,0))
    elif dir == 4:
        shop.append((dist,n))
x_dir, x_dist = map(int, input().split())
if x_dir == 1:
    security.append((0,x_dist))
elif x_dir == 2:
    security.append((m,x_dist))
elif x_dir == 3:
    security.append((x_dist, 0))
elif x_dir == 4:
    security.append((x_dist, n))
sum_dist = 0
while shop:
    ti, tj = shop.pop()
    hi, hj = security[0][0], security[0][1]
    clockwise(ti, tj, hi, hj)
    counter_clockwise(ti, tj, hi, hj)
    if dist_cw > dist_ccw:
        sum_dist+=dist_ccw
    else :
        sum_dist+=dist_cw

print(sum_dist)

# 시계방향과 반시계방향으로 직접 움직이며 거리 측정