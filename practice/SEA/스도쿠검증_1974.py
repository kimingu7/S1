t = int(input())

for i in range(t):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_90 = [[0 for _ in range(9)] for _ in range(9)]
    for j in range(9):
        for k in range(9):
            sudoku_90[k][9-j-1] = sudoku[j][k]
    rst = 1
    dx = [-1,-1,-1,0,0,0,1,1,1]
    dy = [-1,0,1,-1,0,1,-1,0,1]
    for j in range(9):
        if sum(sudoku[j]) != 45:
            rst = 0
            break
        if sum(sudoku_90[j]) != 45:
            rst = 0
            break
    for x in range(0,9,3):
        for y in range(0,9,3):
            sum_sdc = 0
            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                sum_sdc += sudoku[nx+1][ny+1]
            if sum_sdc != 45:
                rst = 0
                break
    print(f'#{i+1} {rst}')

# 열순회 하기 귀찮아서 그냥 90도 돌리고 동시에 검사함
# 단순히 생각했을 때 행의 합이 45가 아니라면 스도쿠가 아니라는 결론
# 그런데 3x3에 대해서도 유효 검사도 해야했음
# 델타검색을 통해서 3x3의 합을 구함