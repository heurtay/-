# Задание 1

# class BasicPlan:
#     can_stream = True
#     can_download = True
#     has_SD = True
#     has_HD = False
#     has_UHD = False
#     num_of_devices = 1
#     price = '8.99$'
#
# class SilverPlan(BasicPlan):
#     has_HD = True
#     num_of_devices = 2
#     price = '12.99$'
#
# class GoldPlan(BasicPlan):
#     has_HD = True
#     has_UHD = True
#     num_of_devices = 4
#     price = '15.99$'
#
#
# print(GoldPlan.can_stream)
# print(GoldPlan.can_download)
# print(GoldPlan.has_SD)
# print(GoldPlan.has_HD)
# print(GoldPlan.has_UHD)
# print(GoldPlan.num_of_devices)
# print(GoldPlan.price)

# Задание 2
#
from datetime import date
#
# class WeatherWarning:
#     def rain(self):
#         print("Ожидаются сильные дожди и ливни с грозой")
#
#     def snow(self):
#         print("Ожидается снег и усиление ветра")
#
#     def low_temperature(self):
#         print("Ожидается сильное понижение температуры")
#
# class WeatherWarningWithDate(WeatherWarning):
#     def rain(self, dt: date):
#         print(dt.strftime('%d.%m.%Y'))
#         super().rain()
#
#     def snow(self, dt: date):
#         print(dt.strftime('%d.%m.%Y'))
#         super().snow()
#
#     def low_temperature(self, dt: date):
#         print(dt.strftime('%d.%m.%Y'))
#         super().low_temperature()
#
#
# weatherwarning = WeatherWarningWithDate()
# dt = date(2022, 12, 12)
#
# weatherwarning.rain(dt)
# weatherwarning.snow(dt)
# weatherwarning.low_temperature(dt)


# Задание 3

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         super().__init__(side, side, side)
#
#
# triangle1 = Triangle(3, 4, 5)
# triangle2 = EquilateralTriangle(3)
#
# print(triangle1.perimeter())
# print(triangle2.perimeter())


# Задание 4

# class Counter:
#     def __init__(self, start=0):
#         self.value = start
#
#     def inc(self, inc=1):
#         self.value += inc
#
#     def dec(self, dec=1):
#         self.value = max(self.value - dec, 0)
#
# class DoubledCounter(Counter):
#     def __init__(self, start=0):
#         super().__init__(start)
#
#     def inc(self, inc=1):
#         super().inc(inc * 2)
#
#     def dec(self, dec=1):
#         super().dec(dec * 2)
#
#
# counter = DoubledCounter(20)
#
# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(10)
# print(counter.value)
Задание 1: Создали разные тарифные планы (Gold, Silver) на основе базового (Basic), переопределяя только отличающиеся характеристики.
 * Задание 2: Расширили предупреждения о погоде, добавив дату к существующим сообщениям с помощью super().
 * Задание 3: Создали равносторонний треугольник, используя логику базового класса Triangle для инициализации сторон через super().__init__().
 * Задание 4: Изменили поведение счетчика так, чтобы он удваивал приращение/уменьшение, переопределив методы inc() и dec().

