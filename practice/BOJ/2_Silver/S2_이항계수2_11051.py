from math import factorial

n, k = map(int, input().split())
bc = factorial(n) // (factorial(k) * factorial(n - k))
print(bc%10007)