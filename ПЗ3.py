# Задание 1
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __iter__(self):
#         yield self.x
#         yield self.y
#         yield self.z
        
#     def __repr__(self):
#         return f'Point({self.x, self.y, self.z})'

# points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
# print(points)

# Задание 2

# class DevelopmentTeam:
#     def __init__(self):
#         self.juniors = []
#         self.seniors = []
        
#     def add_junior(self, *args):
#         self.juniors.extend((name, 'junior') for name in args)

#     def add_senior(self, *args):
#         self.seniors.extend((name, 'senior') for name in args)
        
#     def __iter__(self):
#         return iter(self.juniors + self.seniors)
    

# beegeek = DevelopmentTeam()

# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# print(*beegeek, sep='\n')

# Задание 3

# class  AttrsIterator:
#     def __init__(self, obj):
#         self._attrs = list(obj.__dict__.items())
#         self._index = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self._index >= len(self._attrs):
#             raise StopIteration
#         attr = self._attrs[self._index]
#         self._index += 1
#         return attr
    
    
    
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
        
# user = User('Debbie', 'Harry', 77)
# attrsiterator = AttrsIterator(user)

# print(*attrsiterator)

# задание 4

import random

class RandomLooper:
    def __init__(self, *args):
        self._items = []
        for item in args:
            self._items.extend(item)
        random.shuffle(self._items)
        self._index = 0        

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item
        

randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))
Задание 1: Класс Point представляет точку в 3D-пространстве и поддерживает итерацию.

Задание 2: Класс DevelopmentTeam управляет списками junior и senior разработчиков.

Задание 3: Класс AttrsIterator позволяет итерировать по атрибутам объекта.

Задание 4: Класс RandomLooper перемешивает элементы итерируемых объектов.
