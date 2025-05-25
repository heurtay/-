# Задание 1

# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class WaterVehicle(Vehicle):
#     pass

# class AirVehicle(Vehicle):
#     pass

# class Car(LandVehicle):
#     pass

# class Motorcycle(LandVehicle):
#     pass

# class Bicycle(LandVehicle):
#     pass

# class Propeller(AirVehicle):
#     pass

# class Jet(AirVehicle):
#     pass


# print(issubclass(LandVehicle, Vehicle))
# print(issubclass(WaterVehicle, Vehicle))
# print(issubclass(AirVehicle, Vehicle))
# print(issubclass(Car, LandVehicle))
# print(issubclass(Motorcycle, LandVehicle))
# print(issubclass(Bicycle, LandVehicle))


# Задание 2

# class Shape:
#     pass

# class Polygon(Shape):
#     pass

# class Circle(Shape):
#     pass

# class Quadrilateral(Polygon):
#     pass

# class Triangle(Polygon):
#     pass

# class Parallelogram(Quadrilateral):
#     pass

# class IsoscelesTriangle(Triangle):
#     pass

# class EquilateralTriangle(Triangle):
#     pass

# class Rectangle(Parallelogram):
#     pass

# class Square(Rectangle):
#     pass


# print(issubclass(Circle, Shape))
# print(issubclass(Polygon, Shape))
# print(issubclass(Triangle, Polygon))
# print(issubclass(IsoscelesTriangle, Triangle))
# print(issubclass(EquilateralTriangle, Triangle))

# Задание 3

# class Animal:
#     def sleep(self):
#         pass
    
#     def eat(self):
#         pass
    
# class Fish(Animal):
#     def swim(self):
#         pass
    
# class Bird(Animal):
#     def lay_eggs(self):
#         pass
    
# class FlyingBird(Bird):
#     def fly(self):
#         pass
    
    
# print(issubclass(Fish, Animal))
# print(issubclass(Bird, Animal))
# print(issubclass(FlyingBird, Animal))
# print(issubclass(FlyingBird, Bird))

# Задание 4

# class User:
#     def __init__(self, name):
#         self.name = name
        
#     def skip_ads(self):
#         return False
    
# class PremiumUser(User):
#     def skip_ads(self):
#         return True
    
    
# print(issubclass(PremiumUser, User))

# user = User('Arthur')
# premium_user = PremiumUser('Arthur')

# print(user.skip_ads())
# print(premium_user.skip_ads())

# Задание 5

# class Validator:
#     def __init__(self, obj):
#         self.obj = obj
    
#     def is_valid(self):
#         pass
    

# class NumberValidator(Validator):
#     def is_valid(self):
#         return isinstance(self.obj, (int, float))


# print(issubclass(NumberValidator, Validator))

# validator1 = NumberValidator('beegeek')
# validator2 = NumberValidator(1)
# validator3 = NumberValidator(1.1)

# print(validator1.is_valid())
# print(validator2.is_valid())
# print(validator3.is_valid())

# validator1 = Validator('beegeek')
# validator2 = Validator(1)
# validator3 = Validator(1.1)

# print(validator1.is_valid())
# print(validator2.is_valid())
# print(validator3.is_valid())

# Задание 6

# class Counter:
#     def __init__(self, start=0):
#         self.value = start
        
#     def inc(self, inc=1):
#         self.value += inc
    
#     def dec(self, dec=1):
#         self.value -= dec
#         if self.value < 0:
#             self.value = 0
            
# class NonDecCounter(Counter):
#     def dec(self, dec=1):
#         pass
    
# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         super().__init__(start)
#         self.limit = limit
        
#     def inc(self, inc=1):
#         self.value = min(self.value + inc, self.limit)
        

# print(issubclass(NonDecCounter, Counter))
# print(issubclass(LimitedCounter, Counter))

# counter = Counter()

# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(3)
# print(counter.value)
# counter.dec(10)
# print(counter.value)

# counter = NonDecCounter(10)

# print(counter.value)
# counter.inc()
# counter.inc(10)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(50)
# print(counter.value)

# counter = LimitedCounter()

# print(counter.value)
# counter.inc()
# counter.inc(4)
# print(counter.value)
# counter.dec()
# counter.dec(2)
# print(counter.value)
# counter.inc(20)
# print(counter.value)

