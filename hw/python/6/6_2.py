grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
grain_lst.sort(key=lambda x:x[1])
print(grain_lst[-1][0])