import sys, math
N = sys.stdin.readline()
data = list(map(int,sys.stdin.readline().split()))
cnt = 0

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for n in data:
    if n == 1:
        pass
    elif isPrime(n) == True:
        cnt+=1
print(cnt)