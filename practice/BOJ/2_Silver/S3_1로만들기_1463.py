n = int(input())
m = [0 for _ in range(n+1)]

for i in range(2, n+1):
    m[i] = m[i-1]+1
    if i%3 == 0:
        m[i] = min(m[i], m[i//3]+1)
    if i%2 == 0:
        m[i] = min(m[i], m[i//2]+1)
print(m[n])