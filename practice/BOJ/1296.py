name = list(input())
N = int(input())
team_list = []
percent = []
L = O = V = E = 0
for i in range(N):
    team_name = list(input())
    team_list.append(team_name)
for i in range(len(name)):
    if name[i] == 'L':
        L+=1
    elif name[i] == 'O':
        O+=1
    elif name[i] == 'V':
        V+=1
    elif name[i] == 'E':
        E+=1
for i in range(N):
    L_ = L
    O_ = O
    V_ = V
    E_ = E
    for j in range(len(team_list[i])):
        if team_list[i][j] == 'L':
            L_+=1
        elif name[i] == 'O':
            O_+=1
        elif name[i] == 'V':
            V_+=1
        elif name[i] == 'E':
            E_+=1
    percent.append((L_+O_) * (L_+V_) * (L_+E_) * (O_+V_) * (O_+E_) * (V_+E_))
print(*team_list[percent.index(max(percent))],sep='')