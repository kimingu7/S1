import sys
from collections import Counter

n, m, b = map(int,sys.stdin.readline().split())
gnd = []
for i in range(n):
    gnd += list(map(int,sys.stdin.readline().split()))
h = 0
t = 10000000000
min_h = min(gnd)
max_h = max(gnd)
sum_gnd = sum(gnd)
gnd_ = dict(Counter(gnd))
for i in range(min_h, max_h+1):
    if sum_gnd + b >= i*n*m:
        cur_time = 0
        for key in gnd_:
            if key > i:
                cur_time += (key-i) * gnd_[key] * 2
            elif key < i:
                cur_time += (i-key) * gnd_[key]
        if cur_time <= t:
            t = cur_time
            h = i
print(t, h)