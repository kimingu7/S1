t = int(input())
for i in range(t):
    n = int(input())
    cor = [0 for _ in range(201)]
    for j in range(n):
        a, b = map(int, input().split())
        if a < b :
            for k in range((a+1)//2,((b+1)//2)+1):
                cor[k]+=1
        else :
            for k in range((b+1)//2,((a+1)//2)+1):
                cor[k]+=1
    print(f'#{i+1} {max(cor)}')

# 가장 많이 겹치는 부분만큼 시간이 걸린다고 생각함
# 방 개수와 같은 cor 배열을 만듬(번호는 1~400이기에 크기는 401)
# 방 번호의 범위와 일치하는 index의 cor를 1씩 증가시킨 뒤 max 값을 구하고자 함
# 그러나 방 번호의 범위가 겹치지 않아도 복도는 공유하는 경우가 있었음
# 예시) 1~15와 16~30으로 갈 경우 방 번호는 겹치지 않아도 방 앞 복도는 공유함
# 따라서 방 두개를 묶어서 복도 하나로 생각하기로 했음