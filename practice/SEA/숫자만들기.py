T = int(input())

def dfs(idx, result):
    global max_ans
    global min_ans
    if idx == n-1:
        if max_ans <= result:
            max_ans = result
        if min_ans >= result:
            min_ans = result
        return
    for i in range(4):
        if operator[i] > 0:
            operator[i]-=1
            if i == 0:
                n_result = result + number[idx+1]
            elif i == 1:
                n_result = result - number[idx+1]
            elif i == 2:
                n_result = result * number[idx+1]
            elif i == 3:
                n_result = int(result / number[idx+1])
            dfs(idx+1, n_result)
            operator[i]+=1

for tc in range(1,T+1):
    n = int(input())
    operator = list(map(int, input().split()))
    number = list(map(int, input().split()))
    min_ans = 10 ** 9
    max_ans = -1 * (10 ** 9)
    dfs(0, number[0])
    answer = max_ans - min_ans
    print(f'#{tc}', answer)

# itertools의 permutations를 활용해 풀려했으나 시간이 많이 걸림
# 따라서 dfs를 통해 풀고자 함
# operator[i]가 0보다 클 때 (사용할 수 있는 연산자의 개수가 남아있을 때)
# i에 따라 n_result 값을 계산하고, dfs로 확인