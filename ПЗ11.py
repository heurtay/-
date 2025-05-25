# Задание 1

# class USADate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
        
#     def format(self):
#         return f'{self.month:02}-{self.day:02}-{self.year}'
    
#     def iso_format(self):
#         return f'{self.year}-{self.month:02}-{self.day:02}'
    
# class ItalianDate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
        
#     def format(self):
#         return f'{self.month:02}/{self.day:02}/{self.year}'
    
#     def iso_format(self):
#         return f'{self.year}-{self.month:02}-{self.day:02}'\


# usadate = USADate(2023, 4, 6)

# print(usadate.format())
# print(usadate.iso_format())

# italiandate = ItalianDate(2023, 4, 6)

# print(italiandate.format())
# print(italiandate.iso_format())

# Задание 2

# class MinStat:
#     def __init__(self, iterable=None):
#         self.iterable = iterable if iterable is not None else []
        
#     def add(self, n):
#         self.iterable.append(n)
        
#     def result(self):
#         if len(self.iterable) == 0:
#             return None
#         return min(self.iterable)
    
#     def clear(self):
#         self.iterable = []
        
# class MaxStat:
#     def __init__(self, iterable=None):
#         self.iterable = iterable if iterable is not None else []
        
#     def add(self, n):
#         self.iterable.append(n)
        
#     def result(self):
#         if len(self.iterable) == 0:
#             return None
#         return max(self.iterable)
    
#     def clear(self):
#         self.iterable = []
        
# class AverageStat:
#     def __init__(self, iterable=None):
#         self.iterable = iterable if iterable is not None else []
        
#     def add(self, n):
#         self.iterable.append(n)
        
#     def result(self):
#         if len(self.iterable) == 0:
#             return None
#         return sum(self.iterable) / len(self.iterable)
    
#     def clear(self):
#         self.iterable = []
        

# minstat = MinStat([1, 2, 4])
# maxstat = MaxStat([1, 2, 4])
# averagestat = AverageStat([1, 2, 4])

# minstat.add(5)
# maxstat.add(5)
# averagestat.add(5)

# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())


# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()

# for i in range(1, 6):
#     minstat.add(i)
#     maxstat.add(i)
#     averagestat.add(i)

# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())


# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()

# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())

# Задание 3

class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.lines = []
        self.current_line = ''
        
    def add(self, text):
        for word in text.split():
            if not self.current_line:
                self.current_line = word
            elif len(self.current_line) + 1 + len(word) <= self.length:
                self.current_line += ' ' + word
            else:
                self.lines.append(self.current_line)
                self.current_line = word
                
    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
        for line in self.lines:
            print(line)
        self.lines.clear()
        self.current_line = ''
        
class RightParagraph:
    def __init__(self, length):
        self.length = length
        self.lines = []
        self.current_line = ''
        
    def add(self, text):
        for word in text.split():
            if not self.current_line:
                self.current_line = word
            elif len(self.current_line) + 1 + len(word) <= self.length:
                self.current_line += ' ' + word
            else:
                self.lines.append(self.current_line)
                self.current_line = word
                
    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
        for line in self.lines:
            print(line.rjust(self.length))
        self.lines.clear()
        self.current_line = ''


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()


rightparagraph = RightParagraph(10)

rightparagraph.add('death')
rightparagraph.add('can have me')
rightparagraph.add('when it earns me')
rightparagraph.end()
