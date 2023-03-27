class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0
    def __init__(self, name, breed) -> None:
        self.name = name
        self.breed = breed
        Doggy.birth_of_dogs+=1
        Doggy.num_of_dogs+=1
    def bark(self):
        print(f'{self.name}는 짖었습니다. 멍!멍!')
    def death(self):
        Doggy.num_of_dogs-=1
    @classmethod
    def get_status(cls):
        print(f'태어난 개는 {cls.birth_of_dogs}마리입니다.\n'
            f'살아있는 개는 {cls.num_of_dogs}마리입니다.')

jindo = Doggy('jindo', 'jindotgae')
jindo.bark()
doji = Doggy('doji', 'shiba')
doji.bark()
doji.death()
Doggy.get_status()