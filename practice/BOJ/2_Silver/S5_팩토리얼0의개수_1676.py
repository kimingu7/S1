n = int(input())

def factorial(n):
    if n > 1 :
        return n * factorial(n-1)
    else :
        return 1
n_f = factorial(n)
n_f = list(str(n_f))
count_0 = 0
for i in range(len(n_f)-1,-1,-1):
    if n_f[i] == '0':
        count_0+=1
    else :
        break
print(count_0)