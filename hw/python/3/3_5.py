saltwater = [[0 for _ in range(2)] for _ in range(5)]
for i in range(5):
    try :
        saltwater[i] = list(map(int, input().split()))
    except ValueError:
        break
sum_salt = sum_water = 0
for i in range(5):
    sum_salt = sum_salt + (saltwater[i][0] * saltwater[i][1]) / 100
    sum_water = sum_water + saltwater[i][1]
avg_saltwater = (sum_salt / sum_water) * 100
print(f'{avg_saltwater:.2f}, {sum_water}')