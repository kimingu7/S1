import sys
from collections import deque

n = int(sys.stdin.readline().strip())
card = deque()
for i in range(n):
    card.append(i+1)
for i in range(n-1):
    del card[0]
    card.rotate(-1)
print(*card)