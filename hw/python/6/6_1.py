def de_identify(id):
    id = id[:6]+'*******'
    return id
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))