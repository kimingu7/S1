m, n = map(int, input().split())
lst = [0 for _ in range(n-m+1)]
for i in range(n-m+1):
    lst[i] = m+i
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for i in range(len(lst)):
    if isPrime(lst[i]) == True and lst[i] != 1:
        print(lst[i])