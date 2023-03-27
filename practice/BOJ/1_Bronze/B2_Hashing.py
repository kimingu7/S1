import sys

L = int(input())
char = sys.stdin.readline()
score = 0
for i in range(L):
    score = score + ((ord(char[i]) - 96) * (31 ** i))
print(score % 1234567891)