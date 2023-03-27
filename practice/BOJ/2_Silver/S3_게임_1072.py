import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
z = (y*100)//x
if z >= 99:
    print(-1)
    sys.exit()
else :
    game = 0
    start = 1
    end = 1000000000
while start <= end:
    mid = (start+end)//2
    z_ = ((y+mid)*100)//(x+mid)
    if z_ > z:
        game = mid
        end = mid-1
    else:
        start = mid+1
print(game)