# Задача 1

# class UpperPrintString(str):
#     def __str__(self):
#         return self.upper()
#
#
# s = UpperPrintString('beegeek')
# print(list(s))

# Задача 2

# class LowerString(str):
#     def __new__(cls, obj=""):
#         if isinstance(obj, str):
#             return super().__new__(cls, obj.lower())
#         elif isinstance(obj, list):
#             return super().__new__(cls, str([x.lower() for x in obj]))
#         elif isinstance(obj, dict):
#             return super().__new__(cls, str({k.lower(): v for k, v in obj.items()}))
#
# s = LowerString('BeeGeek')
#
# print(s[0], s[3])

# Задача 3

# class FuzzyString(str):
#     def __eq__(self, other):
#         if isinstance(other, str):
#             return self.lower() == other.lower()
#         return NotImplemented
#
#     def __ne__(self, other):
#         if isinstance(other, str):
#             return self.lower() != other.lower()
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, str):
#             return self.lower() < other.lower()
#         return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, str):
#             return self.lower() <= other.lower()
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, str):
#             return self.lower() > other.lower()
#         return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, str):
#             return self.lower() >= other.lower()
#         return NotImplemented
#
#     def __contains__(self, item):
#         if isinstance(item, str):
#             return item.lower() in self.lower()
#         return NotImplemented
#
#
# s1 = FuzzyString('BeeGeek')
# s2 = FuzzyString('beegeek')
#
# print(s1 == s2)
# print(s1 in s2)
# print(s2 in s1)
# print(s2 not in s1)

#задача 4

# class TitledText(str):
#     def __new__(cls, content, text_title):
#         content = super().__new__(cls, content)
#         content._title = text_title
#         return content
#     def title(self):
#         return self._title
#
#
# titled1 = TitledText('Сreate a class Soda', 'Homework')
# titled2 = TitledText('Сreate a class Soda', 'Exam')
#
# print(titled1 == titled2)

# задача 5

# class SuperInt(int):
#     def __iter__(self):
#         for digit in str(abs(self)):
#             yield SuperInt(int(digit))
#
#     def repeat(self, n = 2):
#         if '-' in str(self):
#             return '-' + str(self)[1:] * n
#         return str(self) * n
#
#     def to_bin(self):
#         if '-' in str(self):
#             return '-' + bin(self)[3:]
#         return bin(self)[2:]
#
#     def next(self):
#         return self + 1
#
#     def prev(self):
#         return self - 1
#
#
# superint1 = SuperInt(1337)
# superint2 = SuperInt(-2077)
#
# print(*superint1)
# print(*superint2)

# задача 6

# class RoundedInt(int):
#     def __new__(cls, num, even=True):
#         if even:
#             if num % 2 != 0:
#                 num += 1
#         else:
#             if num % 2 == 0:
#                 num += 1
#
#         return super().__new__(cls, num)
#
#
# roundedint1 = RoundedInt(7)
# roundedint2 = RoundedInt(7, False)
#
# print(roundedint1 + roundedint2)
# print(roundedint1 + 1)
# print(roundedint2 + 1)
#
# print(type(roundedint1))
# print(type(roundedint2))






