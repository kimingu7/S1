T = int(input())

def bst(i):
    global number
    if i <= n:
        bst(i*2)
        tree[i] = number
        number +=1
        bst(i*2+1)

for tc in range(1,T+1):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    number = 1
    bst(1)
    answer1 = tree[1]
    answer2 = tree[n//2]

    print(f'#{tc}', answer1, answer2)

# bst(이진 탐색 트리)를 만들어 1번 노드의 값과, n//2번 노드의 값을 출력하는 문제
# number는 노드의 번호
# line 6 왼쪽 노드는 부모 노드의 번호의 두 배
# line 9 오른쪽 노드는 부모 노드의 번호의 두 배 + 1
# answer1은 1번 노드의 값
# answer2는 n//2번 노드의 값