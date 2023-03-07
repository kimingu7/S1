octave = list(map(int,input().split()))

if octave[0] == 1:
    for i in range(len(octave)):
        if octave[i] != i+1:
            print('mixed')
            break
        elif i == len(octave) - 1:
            print('ascending')
elif octave[0] == 8:
    for i in range(len(octave)):
        if octave[i] != 8-i:
            print('mixed')
            break
        elif i == len(octave) -1:
            print('descending')
else :
    print('mixed')