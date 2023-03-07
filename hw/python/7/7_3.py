class Calculator:
    def add(self, a, b):
        print(a+b)
    def substract(self, a, b):
        print(a-b)
    def multiply(self, a, b):
        print(a*b)
    def divide(self, a, b):
        try:
            print(a/b)
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다')
num = Calculator()
num.add(1,2)
num.substract(2,1)
num.multiply(3,4)
num.divide(4,0)