def dfs(i, j):
    global cnt
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    if i < 0 or n <= i or j < 0 or n <= j:
        return False
    if villa[i][j] == 1:
        cnt+=1
        villa[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            dfs(ni,nj)
        return True
    return False


n = int(input())
villa = [list(map(int,input())) for _ in range(n)]
state = []
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            state.append(cnt)
            dfs(i, j)
            cnt = 0
state.sort()
print(len(state))
for i in range(len(state)):
    print(state[i])

# 연결요소의 개수와 유사한 문제
# 연결요소의 개수뿐만 아니라 각 연결요소의 크기 또한 알아내야한다
# dfs를 진행하며 각 연결요소의 크기를 알기 위한 변수 cnt 정의
# 탐색이 끝날 때마다 누적된 cnt를 state 배열에 append시키고, cnt는 0으로 초기화
# 빌라의 총 개수는 state의 길이와 같으며, 크기 순으로 정렬해서 출력