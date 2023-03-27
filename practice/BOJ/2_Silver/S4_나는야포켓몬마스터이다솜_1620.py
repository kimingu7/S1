import sys
n, m = map(int,sys.stdin.readline().split())
pokemon = {}
for i in range(1,n+1):
    name = input().rstrip()
    pokemon[i] = name
    pokemon[name] = i
for i in range(m):
    command = input().rstrip()
    if command.isdigit():
        print(pokemon[int(command)])
    else :
        print(pokemon[command])
