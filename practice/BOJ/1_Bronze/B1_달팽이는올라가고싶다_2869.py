A, B, V = map(int, input().split())
date = ((V-A) / (A-B)) + 1
print(int(date) if date == int(date) else int(date)+1)