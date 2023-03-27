# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

n_s = s[3:-3]
n_s = n_s.lower()
n_s = n_s.capitalize()
print(n_s)