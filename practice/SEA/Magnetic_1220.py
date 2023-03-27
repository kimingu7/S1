for tc in range(1,11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    sum_count = 0
    for j in range(n):
        count = 0
        stack.clear()
        for i in range(n):
            if not stack:
                if table[i][j] == 1:
                    stack.append(1)
            if stack:
                if table[i][j] == 2:
                    stack.pop()
                    count+=1
        sum_count += count

    print(f'#{tc}',sum_count)

# stack 활용하면 됨