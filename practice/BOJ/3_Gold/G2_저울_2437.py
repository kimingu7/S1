N = int(input())
pendulum = list(map(int, input().split()))
pendulum.sort() // 정렬
weights = 1
for i in pendulum: 
    if weights < i: // 누적합이 새로운 추의 무게보다 작다면 그 사이의 무게들을 만들지 못함
        break
    weights += i
print(weights)