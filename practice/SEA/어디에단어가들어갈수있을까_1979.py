t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    count_k = 0
    for a in range(n):
        count = 0
        for b in range(n):
            if puzzle[a][b] == 1:
                count+=1
            elif puzzle[a][b] == 0:
                if count == k:
                    count_k+=1
                    count = 0
                else :
                    count = 0
        if count == k:
            count_k+=1
    for a in range(n):
        count = 0
        for b in range(n):
            if puzzle[b][a] == 1:
                count+=1
            elif puzzle[b][a] == 0:
                if count == k:
                    count_k+=1
                    count = 0
                else :
                    count = 0
        if count == k:
            count_k+=1
    print(f'#{i+1} {count_k}')

# 행 순회 열 순회 한번씩 해야함
# 1이 연속될 때 count한 뒤 0이면 count 중지한 후 count 값이 k와 같으면 count_k에 1 더함