tc = list(input())
cnt = 0 
stick = 0
j = 0
while j < len(tc):
    if tc[j] == '(' and tc[j+1] == ')':
        cnt+=stick
        j+=2
    elif tc[j] == '(':
        stick+=1
        j+=1
    else :
        cnt+=1
        stick-=1
        j+=1
print(cnt)