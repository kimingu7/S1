N = int(input())
class_N = [[0 for _ in range(5)] for _ in range(N)]
for i in range(N):
    class_N[i] = list(map(int, input().split()))
sameclass_list = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(5):
            if class_N[i][k] == class_N[j][k]:
                sameclass_list[i]+=1
president = sameclass_list.index(max(sameclass_list)) + 1
print(president)