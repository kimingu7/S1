n, ha = map(int, input().split())

start = 1
end = n * 1000000 * 1000000
dungeon = [list(map(int, input().split())) for _ in range(n)]

def dragon(ha, hm):
    hc = hm
    for i in range(n):
        t = dungeon[i][0]
        a = dungeon[i][1]
        h = dungeon[i][2]
        if t == 1:
            if not h%ha :
                times = h//ha
            else:
                times = h//ha+1
            hc -= a * (times-1)
        else:
            ha += a
            hc += h
            if hc > hm:
                hc = hm
        if hc <= 0:
            return False
    return True
answer = 0
while start <= end:
    hm = (start+end)//2
    if dragon(ha, hm):
        end = hm - 1
        answer = hm
    else :
        start = hm + 1
print(answer)