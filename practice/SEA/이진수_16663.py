T = int(input())
hex_dic = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
for tc in range(1, T+1):
    n, hex = input().split()
    result = ''
    for h in hex[::-1]:
        if h in hex_dic:
            h = hex_dic[h]
        h = int(h)
        for _ in range(4):
            result = str(h%2) + result
            h//=2
    print(f'#{tc}', result)

# 딕셔너리를 활용해 16진수를 이진수로 바꿈