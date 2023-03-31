def bank(bi,tri):
    moneys = []
    for i in range(1,len(bi)):
        money = list(bi)
        if bi[i] == '0':
            money[i] = '1'
        else:
            money[i] = '0'
        moneys.append(int(''.join(money), 2))
    nums = ['0','1','2']
    for i in range(len(tri)):
        for num in nums:
            money = list(tri)
            if money[i] != num:
                money[i] = num
                money = int(''.join(money), 3)
                if money in moneys:
                    return money

T = int(input())
for tc in range(1, T+1):
    bi = input()
    tri = input()
    answer = bank(bi, tri)
    print(f'#{tc}',answer)