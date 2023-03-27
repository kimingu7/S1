t = int(input())
for i in range(t):
    str1 = list(set(input()))
    str2 = list(input())
    max_cnt = 0
    for j in range(len(str1)):
        cnt = 0
        for k in range(len(str2)):
            if str1[j] == str2[k]:
                cnt+=1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{i+1} {max_cnt}')

# str1에서 중복문자는 중요하지 않기 때문에 list(set())을 통해 중복은 정리함
# 그 이후엔 이중 for문을 통해 순회하며 카운트한 뒤 max_cnt 값과 비교