#Driver's code
class Person:
    age_2023 = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def get_age(cls, name, year):
        age_2023 = 2023-year+1
        return cls(name, age_2023)

    def check_age(self):
        if self.age > 19:
            return True
        else :
            return False
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
