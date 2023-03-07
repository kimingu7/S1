t = int(input())
for i in range(t):
    tc = list(input())
    lazer = [] 
    steel = []
    steel_start = [] 
    cnt = 0
    for j in range(len(tc)):
        if tc[j] == ')':  
            if tc[j-1] == '(': 
                lazer.append(j)
            else :
                for k in range(j,-1,-1): 
                    if tc[k] == '(' and k+1 not in lazer and k not in steel_start:
                        steel.append([k,j])             
                        steel_start.append(k)
                        break
    for j in range(len(lazer)):
        for k in range(len(steel)):
            if steel[k][0] < lazer[j] < steel[k][1]:
                cnt+=1
    print(f'#{i+1} {cnt+len(steel)}')

# line 4 lazer : 레이저 좌표를 담을 빈 리스트
# line 5 steel : 막대기 범위를 담을 빈 리스트
# line 6 steel_start : 막대기의 시작점을 담을 빈 리스트
# line 9-10 )가 있을 때 한칸 앞이 (라면 lazer에 j를 추가
# line 13-18 아닐 경우 가장 가까운 ( 중 lazer에도 없으며
# 이미 다른 막대의 시작점이 아닌 (의 index인 k와 )의 index의 j를 추가하고, 시작점을 k에 추가
# line 20 lazer가 steel 사이에 있으면 cnt+=1
# line 22 cnt에 막대기 개수를 더해 최종값 출력
# 시간초과가 뜬 이유?
# append만 3번을 사용했다 append는 원래 시간이 많이 걸림
# )를 찾기 위해 j만큼 전진한 뒤 다시 후진하면서 (를 찾는 과정에서 시간이 많이 걸림