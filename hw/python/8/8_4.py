class PublicTransport:
    num_of_passenger = 0
    def __init__(self, size) -> None:
        self.size = size
    def get_in(self):
        PublicTransport.num_of_passenger+=1
    def get_off(self):
        PublicTransport.num_of_passenger-=1

class Bus(PublicTransport):
    def __init__(self, size) -> None:
        super().__init__(size)
    def get_in(self):
        super().get_in()
        max_passenger = self.size
        print(f'현재 탑승 인원은 {self.num_of_passenger}명입니다')
        if PublicTransport.num_of_passenger >= max_passenger:
            PublicTransport.num_of_passenger -=1
            print('더 이상 탑승할 수 없습니다')

bus = Bus(5)
for i in range(5):
    bus.get_in()