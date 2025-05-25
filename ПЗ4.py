# Задание 1
# def print_file_content(filename):
#     try:
#         with open(filename, mode='r', encoding='utf-8') as file:
#             print(file.readline())
#     except FileNotFoundError:
#         print(f"Файл не найден")
#
#
# with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
#     file.write('Сражения и путешествия берут своё')
#
# print_file_content('Precepts_of_Zote.txt')

# Задание 2

# def non_closed_files(files):
#     open_files = []
#     for file in files:
#         if not file.closed:
#             open_files.append(file)
#     return open_files
#
#
# with (
#     open('file1.txt', 'w', encoding='utf-8') as file1,
#     open('file2.txt', 'w', encoding='utf-8') as file2,
#     open('file3.txt', 'w', encoding='utf-8') as file3
# ):
#     file1.write('i am the first file')
#     file2.write('i am the second file')
#     file3.write('i am the third file')
#
# file1 = open('file1.txt', encoding='utf-8')
# file3 = open('file3.txt', encoding='utf-8')
#
#
# for file in non_closed_files([file1, file2, file3]):
#     print(file.read())

# Задание 3

# def log_for(logfile, date_str):
#     with open(f"log_for_{date_str}.txt", mode='w', encoding='utf-8') as log_file:
#         with open(logfile, mode='r', encoding='utf-8') as file:
#             for line in file:
#                 date_part, message_part = line[:10], line[11:]
#                 if date_part == date_str:
#                     log_file.write(message_part)
#
#
# with open('log.txt', 'w', encoding='utf-8') as file:
#     print('2022-01-01 INFO: User logged in', file=file)
#     print('2022-01-01 ERROR: Invalid input data', file=file)
#     print('2022-01-02 INFO: User logged out', file=file)
#     print('2022-01-03 INFO: User registered', file=file)
#
# log_for('log.txt', '2022-01-01')
#
# with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
#     print(file.read())

