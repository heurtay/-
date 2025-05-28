#Задание 1
# def hash_function(obj):
#     str_obj = str(obj)
#     temp1 = 0
#     temp2 = 0
#     for i in range(len(str_obj)//2):
#         gender = ord(str_obj[i]) * ord(str_obj[-i - 1])
#         temp1 += gender
#     if len(str_obj) % 2 != 0:
#         temp1 += ord(str_obj[len(str_obj) // 2])

#     for j in range(len(str_obj)):
#         temp2 += ((-1) ** j) * ord(str_obj[j]) * (j + 1)

#     return (temp1 * temp2) % 123456791

# print(hash_function('python'))
# print(hash_function(12345))
# print(hash_function(None))

# Задание 2

# def limited_hash(left, right, hash_function=hash):
#     def inner(obj):
#         raw_hash = hash_function(obj)
#         size_hash = right - left + 1
#         if left <= raw_hash <= right:
#             return raw_hash
#         return left + (raw_hash - left) % size_hash
#     return inner


# hash_function = limited_hash(10, 15)

# print(hash_function(16))
# print(hash_function(17))
# print(hash_function(21))
# print(hash_function(22))
# print(hash_function(23))


# Задание 3

# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#     @property
#     def x(self):
#         return self._x

#     @property
#     def y(self):
#         return self._y
#     @property
#     def color(self):
#         return self._color

#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self.x == other.x and self.y == other.y and self.color == other.color
#         return NotImplemented

#     def __hash__(self):
#         return hash((self.x, self.y, self.color))

#     def __repr__(self):
#         return f"ColoredPoint({self.x}, {self.y}, {repr(self.color)}"

# point = ColoredPoint(1, 2, 'white')

# try:
#     point.color = 'black'
# except AttributeError as e:
#     print('Error')
Задание 1: hash_function(obj)
Преобразует объект в строку, затем вычисляет хеш по сложной формуле из двух частей, зависящих от символов строки.
Задание 2: limited_hash(left, right, hash_function=hash)
Создаёт новую хеш-функцию, которая "заворачивает" результаты исходной хеш-функции в заданный диапазон [left, right].
Задание 3: Класс ColoredPoint
Описывает точку с координатами (x, y) и цветом. Координаты и цвет доступны только для чтения. Класс умеет сравнивать точки (__eq__), быть ключом в хеш-таблицах (__hash__) и имеет удобное текстовое представление (__repr__)



