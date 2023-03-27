from collections import deque
for _ in range(10):
    tc = int(input())
    pw = deque(list(map(int, input().split())))
    while pw[-1] != 0:
        for i in range(1,6):
            p = pw.popleft()
            if p-i <= 0:
                pw.append(0)
                break
            else :
                pw.append(p-i)
    print(f'#{tc}', *pw)

# pw의 마지막이 0이 아닐 경우 while문 실행
# 사이클은 무조건 1,2,3,4,5의 순서대로 감소하기 때문에 for문 사용
# p-i가 0 이하일 때, pw에 0을 append시키고 break
# 아닐 경우 pw에 p-i를 append
# pw를 출력