def expression(i):
    if i:
        expression(left[i])
        expression(right[i])
        if tree[i] == '+':
            tree[i] = int(tree[left[i]]) + int(tree[right[i]])
        elif tree[i] == '-':
            tree[i] = int(tree[left[i]]) - int(tree[right[i]])
        elif tree[i] == '*':
            tree[i] = int(tree[left[i]]) * int(tree[right[i]])
        elif tree[i] == '/':
            tree[i] = int(tree[left[i]]) // int(tree[right[i]])
    return

for tc in range(1,11):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    left = [0 for _ in range(n+1)]
    right = [0 for _ in range(n+1)]
    for i in range(n):
        node = list(input().split())
        tree[int(node[0])] = node[1]
        if len(node) == 4:
            left[int(node[0])] = int(node[2])
            right[int(node[0])] = int(node[3])
    expression(1)
    answer = tree[1]
    print(f'#{tc}', answer)

# tree, left, right 3개의 배열을 만듬
# len(node)가 4라는 뜻은 자식 노드의 정보가 있다는 뜻이므로 자식 노드의 정보를 left와 right 배열에 저장
# tree의 n번째 index [int(node(0))]에 node[1]를 입력(node[1]은 연산자 또는 숫자이기 때문에 input()으로 입력받음)
# expression 함수에서 left[i]와 right[i]를 실행시켜 노드의 관계 확인
# tree[i]가 연산자일 때, tree[left[i]]와 tree[right[i]]는 tree[i]의 자식 노드
# 자식 노드들의 값을 연산해서 tree[i]에 저장
# tree의 1번 노드의 값이 정답