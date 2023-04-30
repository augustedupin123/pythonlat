class Cars:

    speed_rpm = 1800
    
    def __init__(self, number, fuel_type, capacity, torque):
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque
        pass
    def power_calc(self):
        return (self.torque * self.speed_rpm)/9550
    

    #defining a class method to alter speed value:

    @classmethod

    def set_speed(cls, speed):
        cls.speed_rpm = speed

car1 = Cars("RJ06 1719", "Petrol", "35 litres", 200)
print(car1.power_calc())
#calling the classmethod

Cars.set_speed(2100)
print(car1.power_calc())


