t = int(input())
def result(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else :
        return result(n-1) + result(n-2) + result(n-3)
for i in range(t):
    n = int(input())
    print(result(n))