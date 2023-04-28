import heapq
import sys

input = sys.stdin.readline

N = int(input())
min_heap = []
max_heap = []

for i in range(N):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)
    print(-max_heap[0])

# heapq를 활용해서 min_heap과 max_heap 두 개를 만들고,
# 최소 힙의 최대값이 최대 힙의 최대값(-1을 곱해서 들어갔기에 실제로는 최소값)보다 크다면
# 두 값을 교환해 중간값인 -max_heap[0]을 출력함