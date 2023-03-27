def inorder(a):
    if a <= n:
        inorder(a*2)
        print(sentence[a], end='')
        inorder(a*2+1)

for tc in range(1,11):
    n = int(input())
    sentence = [0 for _ in range(n+1)]
    for i in range(n):
        node = list(input().split())
        sentence[i+1] = node[1]
    print(f'#{tc}', end=' ')
    inorder(1)
    print()

# 중위 순회를 통해 문제를 출력
# 자식 노드에 대한 정보는 딱히 사용하지 않아도 됨
# 노드에 따른 sentence 배열만 올바르게 만들어주면 중위순회를 통해 출력가능