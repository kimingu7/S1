import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    applicants.sort()
    cnt = 1
    success = applicants[0][1]
    for i in range(1,n):
        if applicants[i][1] < success:
            cnt+=1
            success = applicants[i][1]
    print(cnt)