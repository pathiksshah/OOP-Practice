class Vehicle():
    #Class attribute
    color = "White"

    def __init__(self, name, max_speed,mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def __init__(self,name,max_speed,mileage, capacity):
        Vehicle.__init__(self,name,max_speed,mileage, capacity)
    def fare(self):
        return super().fare()*1.10
    def __str__(self):
        return "I'm a Bus"
School_bus = Bus("School Volvo", 70, 12, 50)
print("Total Bus fare is:", School_bus.fare())

print(School_bus)

# use Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))