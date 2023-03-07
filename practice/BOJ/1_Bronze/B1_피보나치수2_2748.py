n = int(input())

fibonaci = [0,1]
for i in range(2,n+1):
    fibonaci.append(fibonaci[i-2]+fibonaci[i-1])
print(fibonaci[-1])