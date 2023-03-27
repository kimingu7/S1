n, r, c = map(int, input().split())
rst = 0

while n >= 1:
    mid = (2**(n-1)) - 1
    if r <= mid and c <= mid:
        n-=1
        continue
    elif r <= mid and c > mid:
        c -= mid+1
        rst+=(mid+1)*(mid+1)
    elif r > mid and c <= mid:
        r -= mid+1
        rst+=(mid+1)*(mid+1)*2
    elif r > mid and c > mid:
        c -= mid+1
        r -= mid+1
        rst+=(mid+1)*(mid+1)*3
    n-=1

print(rst)

# 분할탐색을 활용해 r행 c열이 몇번째로 방문되는지 찾는 문제
# 중심인 mid를 찾아 r과 c를 중심 기준으로 어디에 위치하는지 판별
# 판별 뒤에 경우에 따라 r과 c를 변경해주며 위치에 따라 rst를 누적
# 4등분한 배열의 크기 n이 1까지 갈 때까지 반복