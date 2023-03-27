from collections import deque

def check_right(gear_num, dir):
    if gear_num > 4 or gear[gear_num-1][2] == gear[gear_num][6]:
        return
    if gear[gear_num-1][2] != gear[gear_num][6]:
        check_right(gear_num+1, -dir)
        gear[gear_num].rotate(dir)

def check_left(gear_num, dir):
    if gear_num < 0 or gear[gear_num][2] == gear[gear_num+1][6]:
        return
    if gear[gear_num][2] != gear[gear_num+1][6]:
        check_left(gear_num-1, -dir)
        gear[gear_num].rotate(dir)

gear = {}
for i in range(1,5):
    gear[i] = deque(list(map(int, input())))

k = int(input())
for _ in range(k):
    gear_num, dir = map(int, input().split())
    check_right(gear_num+1,-dir)
    check_left(gear_num-1,-dir)
    gear[gear_num].rotate(dir)

score = 0
for i in range(1,5):
    if gear[i][0] == 1:
        score+=2**(1-i)

print(score)

# 처음엔 모든 경우의 수에 따라 직접 기어를 움직이는 코드를 모두 작성
# 대신 함수를 작성하고 재귀를 이용해 기어를 움직임
# 왼쪽과 오른쪽을 확인해 돌려야한다면 돌림
# 왼쪽, 혹은 오른쪽의 기어가 돌아가지 않았다면 그 다음 기어는 돌릴 필요가 없음