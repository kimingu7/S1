import sys
n = int(sys.stdin.readline())
list_n = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_m = list(map(int,sys.stdin.readline().split()))

for num in list_m:
    print(1) if num in list_n else print(0)