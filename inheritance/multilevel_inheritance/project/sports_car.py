from project.car import Car

class SportsCar(Car):
    def race(self):
        return "racing..."

ferrari = SportsCar()
print(ferrari.move())
print(ferrari.drive())
print(ferrari.race())
