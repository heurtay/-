# Задача 1

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A):
#     pass
#
# class E(B, D):
#     pass
#
#
# print(issubclass(B, A))
# print(issubclass(C, A))
# print(issubclass(D, A))

# Задача 2

# class H:
#     pass
#
# class D(H):
#     pass
#
# class E(H):
#     pass
#
# class F(H):
#     pass
#
# class G(H):
#     pass
#
# class B(D, E):
#     pass
#
# class C(F, G):
#     pass
#
# class A(B, C):
#     pass


# print(issubclass(C, D))
# print(issubclass(C, E))
# print(issubclass(C, F))
# print(issubclass(C, G))

# Задача 3

def get_method_owner(cls, method):
    for base in cls.__mro__:
        if method in base.__dict__:
            return base
    return None


class A:
    pass


class B(A):
    pass


print(get_method_owner(B, 'm'))
Задача 1: Проверка наследования классов (A, B, C, D, E).

Задача 2: Проверка наследования в сложной иерархии классов (A, B, C, D, E, F, G, H).

Задача 3: Функция get_method_owner ищет класс, которому принадлежит метод.


