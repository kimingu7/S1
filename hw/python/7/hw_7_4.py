def collatz(n):
    for i in range(500):
        if n == 1:
            print(i)
            break
        elif n % 2 == 1:
            n = (n*3)+1
        elif n % 2 == 0:
            n = n//2
        if i == 499:
            print(-1)
collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1