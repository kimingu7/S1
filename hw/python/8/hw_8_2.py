class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def get_area(self):
        area = abs(p1.x-p2.x)*abs(p1.y-p2.y)
        return area
    def get_perimeter(self):
        perimeter = (abs(p1.x-p2.x)+abs(p1.y-p2.y))*2
        return perimeter
    def is_square(self):
        if abs(p1.x-p2.x) == abs(p1.y-p2.y):
            return True
        else :
            return False

# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True