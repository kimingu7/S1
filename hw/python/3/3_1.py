fruits = 'apple,rottenBanana,apple,RoTTenorange,Orange'
fruit_list = fruits.split(',')
for i in range(len(fruit_list)):
    fruit_list[i] = fruit_list[i].lower()
    fruit_list[i] = fruit_list[i].replace('rotten','')
print(fruit_list)