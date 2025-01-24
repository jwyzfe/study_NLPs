'''
Vehicle
 ├── Car
 │     ├── get_info (부모 메서드 사용)
 │     └── ride_info (추가 메서드)
 └── Truck
       ├── get_info (오버라이드)
       └── more_info (추가 메서드)
'''

class Vehicle: #부모 클래스
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle): #car class가 vehicle class를 상속받음
    def get_info(self):
        return super().get_info() #super() : 코드 중복 방지

    def ride_info(self):
        return f"My car is a {self.brand} {self.model} ."


class Truck(Vehicle): #자식 클래스
    def get_info(self):
        return f"Truck Brand: {self.brand}, Truck Model: {self.model}"

    def more_info(self):
        return f"My truck is a {self.brand} {self.model}"



car = Car("Kia", "K3")
truck = Truck("Kia", "Bongo")


print(car.get_info())  
print(car.ride_info())  

print(truck.get_info())  
print(truck.more_info()) 