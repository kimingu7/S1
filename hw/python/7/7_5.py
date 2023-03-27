import random
class ClassHelper:
    def __init__(self, lst) -> None:
        self.lst = lst
        print(lst)
    def pick(self, a):
        rndlst = random.sample(self.lst, a)
        return rndlst
    def match_pair(self):
        rndlst1 = random.sample(self.lst, 2)
        self.lst.remove(rndlst1[0])
        self.lst.remove(rndlst1[1])
        return rndlst1, self.lst

ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())