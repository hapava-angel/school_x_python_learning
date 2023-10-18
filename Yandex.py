# N = int(input())
# print('Купи слона!\n'*N)    если нужно разделить повторяющиеся строки

# N = int(input())
# a = input()
# print(f'Я больше никогда не буду писать: "{a}"!\n' * N)

# N = int(input())
# M = int(input())
# a = N * M // 2
# print(a)

# name = input()
# number = int(input())
# group = number / 100
# bed = number // 10 % 10
# n_list = number % 10
# print('Чек')
# print(f"Группа № {group}.")
# print(f"{n_list}. {name}.")
# print(f"Шкафчик: {number}.")
# print(f"Кроватка: {bed}.")


# a = int(input())
# a1 = a // 100 % 10
# a2 = a // 1000
# a3 = a // 10 % 10
# a4 = a % 10
# print(a1, a2, a4, a3, sep='')

# a = int(input())
# b = int(input())
# c = (a % 10 + b % 10) % 10
# d = (a // 10 + b // 10) % 10
# e = (a // 100 + b // 100) % 10
# print(e, d, c, sep='')

# a = int(input())
# b = int(input())
# c = b // a
# d = b % a
# print(c, d)

# a = int(input())
# b = int(input())
# c = int(input())
# d = a + c + 1
# print(d)

# N = int(input())
# M = int(input())
# T = int(input())
# if T >= 1440:
#     N1 = T // 60  # Кол-во часов без остатка
#     a = N + N1 # Часы с доставкой
#     while a >= 24:
#         a -= 24
#     if a == 24:
#         a = 00
#     M1 = T % 60 #Остаток минут
#     b = M + M1 # Минуты на данный момент + остаток минут
#     while b >= 60:
#         b -= 60
#         a += 1
# else:
#     N1 = T // 60  # Кол-во часов без остатка
#     a = N + N1  # Часы с доставкой
#     while a >= 24:
#         a -= 24
#         if a == 24:
#             a = 00
#     M1 = T % 60 #Остаток минут
#     b = M + M1 # Минуты на данный момент + остаток минут
#     while b >= 60:
#         b -= 60
#         a += 1
# print(f"{a:0>2}:{b:0>2} ") 

# N = int(input())
# M = int(input())
# T = int(input())
# a = (N + M // 60) % 24
# b = N  % 60
# print(f"{a:0>2}:{b:0>2} ") 

# N1 = T // 60
# N2 = N + N1
# while N2 < 24:
#         N2 = N + N1
#         if N2 > 24
# M1 = T % 60
# print(f"{N2:0>2}:{M1:0>2} ")  #- для выравнивания строк удобно, особенно в работе со временем


# A = int(input())
# B = int(input())
# C = int(input())
# d = (B - A) / C
# print(d)

# a = int(input())
# b = input()
# b1 = int(b, 2)
# c = a + b1
# print(c)

# a = input()
# b = int(input())
# a1 = int(a, 2)
# c = b - a1
# print(c)

# name = input()
# price = int(input())
# mass = int(input())
# money = int(input())
# a = price * mass
# b = money - a
# d = 'Чек'
# c = f"{mass}кг * {price}руб/кг"
# print(f"{d:^35}".replace(' ', '='))   
# print(f"Товар: {name:>28}")
# print(f"Цена: {c:>29}")
# print(f"Итого: {a:>25}руб")
# print(f"Внесено: {money:>23}руб")
# print(f"Сдача: {b:>25}руб")
# print("="*35)

N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
result = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j == N and i * K1 + j * K2 == N * M:
            result.append([i, j])
 
print(*result[0])