import sys
n = int(sys.stdin.readline())
num_n = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num_m = list(map(int,sys.stdin.readline().split()))

count_m = [0 for _ in range(m)]

for i in range(m):
    count = 0
    for j in range(n):
        if num_m[i] == num_n[j]:
            count+=1
    count_m[i] = count
print(*count_m)