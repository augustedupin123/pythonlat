"Encapsulation - building data into functions that operate on that data into a single unit"
"data and code safe from external interference"

"Abstraction - hides unnecessary details- ensures simplocity - details of the program hidden, reduce the program complexity"
"Inheritance - new class can inherit methods and attributes from existing classes"
"polymorphism - "

"class car -> each car with proprties (variables) - vehicle type, fuel type, fuel capacity, torque is an objects of the car class and each variable like vehicle type, fuel type, fuel capacity are called instance variables, and each individual object is called an instance"
"car : Skoda, no., type, capacity, torque -> instance variables, value of these instance variables are attributes, cost of the car, power of the car - methods"

"Instance method, class method, static method, special method"


class Cars:
    def __init__(self, number, fuel_type, capacity, torque):
        self.number = number
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.torque = torque

        pass
car_1 = Cars("RJ06 1719", "Petrol", "35 litres", 200)
print(car_1.number)



class Alcohol:
    year_of_brew = 1990
    storage = "chill"

    def __init__(self, ingredient, hardness):
        self.ingredient = ingredient
        self.hardness = hardness
    def function1(self):
        # above is an instance method, taking an instance as input.
        print("the ingredient is:", self.ingredient)
        print("the hardness is:", self.hardness)
        pass

beer = Alcohol("Rye", "light")
print(beer.function1())
print(beer.ingredient)
print(Alcohol.year_of_brew)









