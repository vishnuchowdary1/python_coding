class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    color = 'white'

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('volvo', 180, 12)
car = Car('audi', 240, 18)

print(bus.color, bus.name, bus.max_speed, bus.mileage)
print(car.color, car.name, car.max_speed, car.mileage)