# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# day = int(input('Введите цифру с 1 до 7 соответствующую дню недели. Для выяснения выходной это или будний день '))
# if 0 < day < 6:
#     print('День будний, работаем')
# elif 5 < day < 8:
#     print('День выходной, скоро на работу')
# else:
#     print('Нет таких данных')

# 2.Напишите программу для. проверки истинности утверждения ¬(нет)(X ⋁(или) Y ⋁ Z) = ¬X ⋀(и) ¬Y ⋀ ¬Z для всех значений предикат.

# x,y,z = int(input('Введите х: ')), int(input('Введите y: ')), int(input('Введите y: '))
# left = not (x or y or z)
# right = not x and not y and not z
# result = left == right
# if result == True:
#     print(f'Утверждение истинно')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34; y=-30 -> 3

# a = int(input('Введите координату Х: '))
# b = int(input('Введите координату Y: '))
# if not a == 0 and not b == 0:
#     if a > 0 < b:
#         print('Координаты находятся в первой четверти')
#     elif a < 0 < b:
#         print('Координаты находятся во второй четверти ')
#     elif a < 0 > b:
#         print('Координаты находятся в третей четверти')
#     elif a > 0 > b:
#         print('Координаты находятся в четвертой четверти')
# else:
#     print(f"Координату с 0 вводить нельзя")

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# number_quarter = int(input('Введите номер четверти из оси координат '))
# if number_quarter == 1:
#     print('Координаты точек x и y находятся в диапазоне от 0 и до 100')
# if number_quarter == 2:
#     print('Координаты точки x находятся от 0 до -100. Координата y от 0 до 100')
# if number_quarter == 3:
#     print('Координаты точек x и y находятся в диапазоне от 0 и до -100')
# if number_quarter == 4:
#     print('Координаты точки x находятся от 0 до 100. Координата y от 0 до -100')
# else:
#     print('такого диапазона не существует')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в
# 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти растояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# x1 = int(input('Введите координат х для первой точки'))
# y1 = int(input('Введите координат y для первой точки'))
# x2 = int(input('Введите координат х для второй точки'))
# y2 = int(input('Введите координат y для второй точки'))
# res = (((x2-x1) **2 + (y2-y1) ** 2) ** 0.5)
# print(f'Расстояние между точками {round(res,3)}')