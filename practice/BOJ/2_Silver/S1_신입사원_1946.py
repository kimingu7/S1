import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    applicants.sort()
    cnt = 0
    print(n-cnt)