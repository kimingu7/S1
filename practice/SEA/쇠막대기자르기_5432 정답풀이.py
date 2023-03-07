t = int(input())
for i in range(t):
    tc = list(input())
    cnt = 0
    stick = 0
    j = 0
    while j < len(tc):
        if tc[j] == '(' and tc[j+1] == ')': # ()가 연속해서 있다면 밑에 있는 stick의 개수만큼 cnt 증가
            cnt+=stick
            j+=2 # 그 후 j+=2 해줌. Why? 이미 j+1까지 봤기 때문
        elif tc[j] == '(': # (는 있는데 다음 칸이 )가 아니라면 막대기를 의미하므로 stick에 추가
            stick+=1
            j+=1
        else : # 아닐 경우는 사실 )밖에 없음. stick을 1 감소시켜주고 cnt는 1 증가시켜줌
            cnt+=1
            stick-=1
            j+=1
    print(f'#{i+1} {cnt}')