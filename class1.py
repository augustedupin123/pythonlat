class Cars:

    # below are the class variables
    num_wheels = 4
    year_manufacture = 2020
    speed_rpm = 1800


    def __init__(self, number, fuel_type, capacity, torque):
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque
    def power_calc(self):
        return(self.torque*self.speed_rpm)
car1 = Cars("MV 311", "Petrol", "35 litres", 200)

# Attributes are the data stored inside the class.
# class attributes and instance attributes.




        