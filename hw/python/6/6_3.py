def count_vowels(char):
    count = 0
    for i in char:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+=1
    print(count)

count_vowels('apple')
count_vowels('banana')