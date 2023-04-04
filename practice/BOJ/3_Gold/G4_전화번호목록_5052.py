import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data =data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
	# 문자열 삽입
    def insert(self, string):
        current_node = self.head
		# 각각의 문자에 대해 자식 Node를 만들며 내려감
        for s in string:
            # 같은 문자가 없을 때 새로운 node를 생성
            if s not in current_node.children:
                current_node.children[s] = Node(s)
			# 같은 문자가 있으면 해당 노드로 이동
            current_node = current_node.children[s]
        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        current_node.data = string
	# 문자열 검색
    def search(self, string):
		# 가장 아래의 노드부터 탐색 시작
        current_node = self.head
        for s in string:
            current_node = current_node.children[s]
        # 자식 노드가 있다는 뜻은 다른 부분이 있다는 뜻이므로 False
        if current_node.children:
            return False
        else :
            return True

T = int(input())

for _ in range(T):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)
    flag = True
    nums.sort()
    for num in nums:
        if not trie.search(num):
            flag = False
            break
    if flag:
        print('YES')
    else :
        print('NO')

# Trie 구조를 통해 탐색을 진행
# flag가 False일 경우 NO, True일 경우 Yes 출력
