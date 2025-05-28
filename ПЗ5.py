# Задание 1

# def is_context_manager(obj):
#     return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')
#
# print(is_context_manager(open('output.txt', mode='w')))

# Задание 2

# class SuppressAll:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return True
#
#
# print('start')
#
# with SuppressAll():
#     print('Python generation!')
#     raise ValueError
#
# print('end')

# Задание 3

# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print(f'Приветствую, {self.name}!')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'До встречи, {self.name}!')
#
# with Greeter('Михаил Г.') as greeter:
#     print(
#         '\nКак бессонница в час ночной\n'
#         'Меняет, нелюдимая, облик твой,\n'
#         'Чьих невольница ты идей?\n'
#         'Зачем тебе охотиться на людей?\n'
#     )

# Задание 4

# class Closer:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self):
#             return self.obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             self.obj.close()
#         except AttributeError:
#             print('Незакрываемый объект')
#
#
# with Closer(5) as i:
#     i += 1
#
# print(i)

#Задание 5

class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def __enter__(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            self.lines = file.readline().split('\n')
            Задание 1: Функция is_context_manager проверяет, является ли объект контекстным менеджером.

Задание 2: Класс SuppressAll подавляет все исключения внутри блока with.

Задание 3: Класс Greeter выводит приветствие и прощание в контекстном менеджере.

Задание 4: Класс Closer автоматически закрывает объект, если у него есть метод close.

Задание 5: Класс ReadableTextFile читает файл и разбивает его на строки.
