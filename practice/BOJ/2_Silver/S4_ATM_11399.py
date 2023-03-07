n = int(input())
p = list(map(int, input().split()))
p.sort()
sum_p = 0
for i in range(n+1):
    sum_p = sum_p + (sum(p[:i]))
print(sum_p)