import sys
n, m = map(int,sys.stdin.readline().split())
wood = list(map(int,sys.stdin.readline().split()))
start = 1
end = max(wood)
while start <= end:
    mid = (start + end) // 2
    cut_wood = 0
    for i in range(n):
        if wood[i] > mid:
            cut_wood += wood[i] - mid
    if cut_wood >= m:
        start = mid + 1
    else :
        end = mid - 1
print(end)