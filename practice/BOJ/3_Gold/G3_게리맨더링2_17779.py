n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
population = 0
answer = 10**9
for i in range(n):
    for j in range(n):
        population+=city[i][j]

def election(r,c,d1,d2):
    global population, answer
    city1 = city2 = city3 = city4 = 0
    c1 = c + 1
    for i in range(r+d1):
        if i >= r:
            c1-=1
        city1 += sum(city[i][:c1])
    c2 = c + 1
    for i in range(r+d2+1):
        if i > r:
            c2 += 1
        city2 += sum(city[i][c2:])
    c3 = c - d1
    for i in range(r+d1, n):
        city3 += sum(city[i][:c3])
        if i < r+d1+d2:
            c3 += 1
    c4 = (c+d2) - n
    for i in range(r+d2+1, n):
        city4 += sum(city[i][c4:])
        if i <= r+d1+d2:
            c4 -= 1
    city5 = population - (city1 + city2 + city3 + city4)
    answer = min(answer, (max(city1, city2, city3, city4, city5) - min(city1, city2, city3, city4, city5)))

def check(r, c, d1, d2):
    if 0 <= r+d1 < n and 0 <= r+d2-1 < n and 0 <= c-d1+d2-1 < n:
        if 0 <= c-d1 and c+d2 < n and r+d1+d2 < n:
            election(r,c,d1,d2)

for r in range(n-2):
    for c in range(1, n-1):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                check(r,c,d1,d2)
print(answer)