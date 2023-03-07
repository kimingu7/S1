T = int(input())
As = list(map(int,input().split()))
As.sort()
N = As[0] * As[-1]
print(N)