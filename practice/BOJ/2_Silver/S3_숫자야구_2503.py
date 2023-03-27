from itertools import permutations

n = int(input())
numbers = [1,2,3,4,5,6,7,8,9]
num_list = list(permutations(numbers,3))

for _ in range(n):
    answer, strike, ball = map(int, input().split())
    answer = list(str(answer))
    removed = 0
    for i in range(len(num_list)):
        strikes = balls = 0
        i -= removed

        for j in range(3):
            answer[j] = int(answer[j])
            if answer[j] in num_list[i]:
                if j == num_list[i].index(answer[j]):
                    strikes+=1
                else :
                    balls+=1

        if strikes != strike or balls != ball:
            num_list.remove(num_list[i])
            removed+=1

print(len(num_list))

# permutations를 활용해 영수가 생각할 수 있는 답을 담은 num_list를 생성
# 이 때 주어진 정보들을 활용해 num_list의 모든 숫자들에 대해서
# answer의 strike와 ball 정보와 num_list의 strike와 ball의 정보가 일치하는 숫자만 num_list에 남겨둠
# 최종적으로 num_list의 길이를 출력함 (num_list의 원소가 아님)