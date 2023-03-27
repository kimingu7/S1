for t in range(10):
    i = int(input())
    canvas = [[0 for _ in range(100)] for _ in range(100)]
    for j in range(100):
        canvas[j] = list(map(int, input().split()))
    sum_canvas = []
    for x in range(100):
        sum_x = 0
        for y in range(100):
            sum_x+=canvas[x][y]
        sum_canvas.append(sum_x)
    for y in range(100):
        sum_y = 0
        for x in range(100):
            sum_y+=canvas[x][y]
        sum_canvas.append(sum_y)
    sum_xy = 0
    sum_xy2 = 0
    for x in range(100):
        sum_xy+=canvas[x][x]
        sum_xy2+=canvas[99-x][x]
    sum_canvas.append(sum_xy)
    sum_canvas.append(sum_xy2)
    print(f'#{i} {max(sum_canvas)}')