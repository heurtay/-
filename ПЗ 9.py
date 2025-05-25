from abc import ABC, abstractmethod
# задача 1

# class Middle(ABC):
#     def __init__(self, user_votes, expert_votes):
#         self.user_votes = user_votes
#         self.expert_votes = expert_votes
#
#     def get_correct_user_votes(self):
#         """Возвращает нормализованный список пользовательских оценок
#         без слишком низких и слишком высоких значений"""
#         return [vote for vote in self.user_votes if 10 < vote < 90]
#
#     def get_correct_expert_votes(self):
#         """Возвращает нормализованный список оценок критиков
#         без слишком низких и слишком высоких значений"""
#         return [vote for vote in self.expert_votes if 5 < vote < 95]
#
#     @abstractmethod
#     def get_average(self, users=True):
#         pass
#
# class Average(Middle):
#     def get_average(self, users=True):
#         """Возвращает среднее арифметическое пользовательских оценок или
#         оценок критиков в зависимости от значения параметра users"""
#         if users:
#             votes = self.get_correct_user_votes()
#         else:
#             votes = self.get_correct_expert_votes()
#
#         return sum(votes) / len(votes)
#
# class Median(Middle):
#     def get_average(self, users=True):
#         """Возвращает медиану пользовательских оценок или
#         оценок критиков в зависимости от значения параметра users"""
#         if users:
#             votes = sorted(self.get_correct_user_votes())
#         else:
#             votes = sorted(self.get_correct_expert_votes())
#
#         return votes[len(votes) // 2]
#
# class Harmonic(Middle):
#     def get_average(self, users=True):
#         """Возвращает среднее гармоническое пользовательских оценок или
#         оценок критиков в зависимости от значения параметра users"""
#         if users:
#             votes = self.get_correct_user_votes()
#         else:
#             votes = self.get_correct_expert_votes()
#
#         return len(votes) / sum(map(lambda vote: 1 / vote, votes))
#
#
# user_votes = [99, 90, 71, 1, 1, 100, 56, 60, 80]
# expert_votes = [87, 90, 67, 70, 81, 85, 97, 79, 71]
# harmonic = Harmonic(user_votes, expert_votes)
#
# print(harmonic.get_correct_user_votes())
# print(harmonic.get_correct_expert_votes())
# print(round(harmonic.get_average(), 2))
# print(round(harmonic.get_average(False), 2))

# Задача 2

# class ChessPiece(ABC):
#     def __init__(self, horizontal, vertical):
#         self.horizontal = horizontal
#         self.vertical = vertical
#
#     @abstractmethod
#     def can_move(self, hor, ver):
#         pass
#
#
# class King(ChessPiece):
#     def can_move(self, hor, ver):
#         dx = abs(ord(hor) - ord(self.horizontal))
#         dy = abs(ver - self.vertical)
#         return dx <= 1 and dy <= 1 and (dx + dy != 0)
#
# class Knight(ChessPiece):
#     def can_move(self, hor, ver):
#         dx = abs(ord(hor) - ord(self.horizontal))
#         dy = abs(ver - self.vertical)
#         return (dx, dy) in [(2, 1), (1, 2)]
#
#
# king = King('b', 2)
#
# print(king.can_move('c', 3))
# print(king.can_move('a', 1))
# print(king.can_move('f', 7))

# задача 3

# class Validator(ABC):
#     def __set_name__(self, owner, name):
#         self.private_name = '_' + name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if not hasattr(instance, self.private_name):
#             raise AttributeError('Атрибут не найден')
#         return getattr(instance, self.private_name)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.private_name, value)
#
#     @abstractmethod
#     def validate(self, value):
#         pass
#
#
# class Number(Validator):
#     def __init__(self, minvalue=None, maxvalue=None):
#         self.minvalue = minvalue
#         self.maxvalue = maxvalue
#
#     def validate(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError('Устанавливаемое значение должно быть числом')
#         if self.minvalue is not None and value < self.minvalue:
#             raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
#         if self.maxvalue is not None and value > self.maxvalue:
#             raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
#
#
# class String(Validator):
#     def __init__(self, minsize=None, maxsize=None, predicate=None):
#         self.minsize = minsize
#         self.maxsize = maxsize
#         self.predicate = predicate
#
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Устанавливаемое значение должно быть строкой')
#         if self.minsize is not None and len(value) < self.minsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
#         if self.maxsize is not None and len(value) > self.maxsize:
#             raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
#         if self.predicate is not None and not self.predicate(value):
#             raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
#
#
# class Student:
#     age = Number(18, 99)
#
# try:
#     student = Student()
#     student.age = 101
# except ValueError as error:
#     print(error)





