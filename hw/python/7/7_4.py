def fee(min, km): 
    if min % 10 == 0:
        if min % 30 == 0:
            fee_min = ((min//10) * 1200) + ((min//30) * 525)
        else :
            fee_min = ((min//10) * 1200) + (((min//30)+1) * 525)
    else :
        fee_min = (((min//10)+1) * 1200) + (((min//30)+1) * 525)
    if km > 100:
        fee_km = (170 * 100) + (85 * (km-100))
    else :
        fee_km = km * 170
    print(fee_min + fee_km)

fee(600, 50)
fee(600, 110)