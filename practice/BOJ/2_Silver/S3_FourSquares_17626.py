n = int(input())
ns = [0,1]
for i in range(2, n+1):
    min_value = 1000000000
    j = 1
    while (j**2) <= i:
        min_value = min(min_value, ns[i - (j**2)])
        j += 1
    ns.append(min_value + 1)
print(ns[n])