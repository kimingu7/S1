t = int(input())
for i in range(t):
    str_ = [list(input()) for _ in range(5)]
    max_str = 0
    for j in range(5):
        if max_str < len(str_[j]):
            max_str = len(str_[j])
    n_str = ''
    for j in range(max_str):
        for k in range(5):
            if j < len(str_[k]):
                n_str += str_[k][j]
    print(f'#{i+1} {n_str}')

# line 6 길이가 다른 str_의 각 행 중 가장 긴 값을 할당
# line 8 n_str : 출력을 위한 빈 문자열
# line 9-12 열 순회하며 n_str에 str_의 원소를 추가