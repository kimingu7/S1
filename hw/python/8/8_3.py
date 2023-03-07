class PublicTransport:
    num_of_passenger = 0
    all_of_passenger = 0
    def __init__(self, name, fare) -> None:
        self.name = name
        self.fare = fare
    def get_in(self):
        PublicTransport.num_of_passenger+=1
        PublicTransport.all_of_passenger+=1
    def get_off(self):
        PublicTransport.num_of_passenger-=1
    @classmethod
    def passenger(cls, name):
        cls.name = name
        print (f'현재 {cls.name} 탑승자는 {cls.num_of_passenger}명입니다.')
    def profit(self):
        profit = PublicTransport.all_of_passenger * self.fare
        print(f'요금 총합은 {profit}입니다')

class Bus(PublicTransport):
    num_of_bus_passenger = 0
    all_of_bus_passenger = 0
    def __init__(self, name, fare) -> None:
        super().__init__(name, fare)
    def get_in(self):
        Bus.num_of_bus_passenger+=1
        Bus.all_of_bus_passenger+=1
    def get_off(self):
        Bus.num_of_bus_passenger-=1
    @classmethod
    def passenger(cls, name):
        cls.name = name
        print (f'현재 {cls.name} 탑승자는 {cls.num_of_bus_passenger}명입니다.')
    def profit(self):
        profit = Bus.all_of_bus_passenger * self.fare
        print(f'요금 총합은 {profit}입니다')
        
class Subway(PublicTransport):
    num_of_subway_passenger = 0
    all_of_subway_passenger = 0
    def __init__(self, name, fare) -> None:
        super().__init__(name, fare)
    def get_in(self):
        Subway.num_of_subway_passenger+=1
        Subway.all_of_subway_passenger+=1
    def get_off(self):
        Subway.num_of_subway_passenger-=1
    @classmethod
    def passenger(cls, name):
        cls.name = name
        print (f'현재 {cls.name} 탑승자는 {cls.num_of_subway_passenger}명입니다.')
    def profit(self):
        profit = Subway.all_of_subway_passenger * self.fare
        print(f'요금 총합은 {profit}입니다')

bus = Bus('bus', 1000)
subway = Subway('subway', 1500)
train = PublicTransport('train', 5000)

bus.get_in()
bus.get_in()
bus.passenger('버스')
bus.profit()

subway.get_in()
subway.get_in()
subway.get_in()
subway.get_off()
subway.get_off()
subway.passenger('지하철')
subway.profit()

train.get_in()
train.get_in()
train.get_in()
train.get_in()
train.get_off()
train.passenger('기차')
train.profit()