n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x : (x[1],x[0]))
count = 1
room = meeting[0]
for i in range(1, n):
    if meeting[i][0] >= room[1]:
        room = meeting[i]
        count += 1
print(count)

# key=lambda를 통해 meeting 배열을 종료시간을 우선으로, 시작시간을 차선으로 하여 정렬
# 이후 첫번째 미팅을 room이라 둠
# room의 종료시간이 meeting 배열의 시작시간보다 빠를 때, room을 meeting[i]로 교체