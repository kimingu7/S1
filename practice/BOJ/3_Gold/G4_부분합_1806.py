import sys

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

left = right = 0
sum_num = 0
min_length = sys.maxsize

while True:
    if sum_num >= s:
        min_length = min(min_length, right-left)
        sum_num -= num_list[left]
        left +=1
    elif right == n:
        break
    else :
        sum_num += num_list[right]
        right += 1

if min_length == sys.maxsize:
    answer = 0
else :
    answer = min_length
print(answer)

# 투 포인터를 활용해 구간합이 s보다 커질 때 가장 작은 길이를 구하는 문제
# 이 때 구간의 합이 s보다 작을 경우 right를 증가시키고,
# 구간의 합이 s보다 크거나 같을 때 최소 길이인지 확인하고, left를 증가시킴
# right가 끝에 도달할 때까지 진행함