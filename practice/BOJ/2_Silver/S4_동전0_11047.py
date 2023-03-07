n, k = map(int, input().split())
A = [0 for _ in range(n)]
for i in range(n):
    A[i] = int(input())
A.sort(reverse=True)
coin = 0
for i in range(n):
    coin+=(k//A[i])
    k = k % A[i]
print(coin)