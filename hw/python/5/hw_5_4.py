n = int(input())

def fn_d(n):
    d = n + sum([int(i) for i in str(n)])
    return d

def is_selfnumber(n):
    selfnumber = []
    for i in range(1000):
        selfnumber.append(fn_d(i))
    for i in range(len(selfnumber)):
        if selfnumber[i] == n:
            print('selfnumber가 아님')
            break
        elif i == len(selfnumber)-1:
            print('selfnumber')
is_selfnumber(n)