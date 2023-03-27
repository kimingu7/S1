import sys

k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(sys.stdin.readline()))
start, end = 1, max(line) 

while start <= end: 
    mid = (start + end) // 2
    lines = 0 
    for i in line:
        lines += i // mid       
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)