def stat():
    global min_stat
    stat = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                stat+=s[i][j]
            elif not visited[i] and not visited[j]:
                stat-=s[i][j]
    min_stat = min(min_stat,abs(stat))
    return

def team(man, num):
    if num > n//2:
        return
    if man == n-1:
        if num == n//2:
            stat()
        return
    team(man+1,num)
    visited[man] = 1

    team(man+1,num+1)
    visited[man] = 0

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_stat = 1000
team(0,0)
print(min_stat)