import sys

t = int(sys.stdin.readline())

wave = [0 for _ in range(101)]
wave[1] = wave[2] = wave[3] = 1
for i in range(3,101):
    wave[i] = wave[i-2] + wave[i-3]

for i in range(t):
    n = int(input())
    print(wave[n])