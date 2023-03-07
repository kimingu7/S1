from itertools import combinations

while True:
    k, *arg = map(int, input().split())
    if k == 0:
        break
    lotto = [*arg]
    numbers = list(combinations(lotto, 6))
    for number in numbers:
        print(*number)
    print()