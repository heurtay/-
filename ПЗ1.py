# Задание 1

class Item:
    def __init__(self, name, price, quantity):
        self.name = name.capitalize()
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)


course = Item('pygen', 3900, 2)

print(course.name)
print(course.price)
print(course.quantity)
print(course.total)

#Задание 2

# class Logger:
#     def __setattr__(self, attr, value):
#         print(f'Изменение значения атрибута {attr} на {value}')
#         self.__dict__[attr] = value
#
#     def __delattr__(self, attr):
#         print(f"Удаление атрибута  {attr}")
#         del self.__dict__[attr]
#
# obj = Logger()
#
# obj.name = 'pygen'
# obj.rating = '5*'
# obj.ceo = 'Timur'
# del obj.rating
# obj.rating = '6*'

# Задание 3

# class Ord:
#     def __getattribute__(self, item):
#         return ord(item)
#
# obj = Ord()
#
# print(obj.в)
# print(obj.г)