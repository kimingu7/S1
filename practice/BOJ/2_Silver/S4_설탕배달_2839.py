n = int(input())

if n == 4 or n == 7:
    k = -1
elif n % 5 == 0:
    k = n//5
elif n % 5 == 1:
    k = (n//5) + 1
elif n % 5 == 2:
    k = (n//5) + 2
elif n % 5 == 3:
    k = (n//5) + 1
elif n % 5 == 4:
    k = (n//5) + 2
elif n % 3 == 0:
    k = n//3
print(k)