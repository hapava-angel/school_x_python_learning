def elements(n: list) -> str | int | list:
    mass = []
    for i in range(1, len(n)):
        if n[i] - n[i-1] > 1:
            mass.append(i)    
    if len(mass) == 0:
            return "Не найден"
    else:
         return mass


user = input('Введите числа: ').split(' ')
user_mass = []
for a in user:
    user_mass.append(int(a))

answer = elements(user_mass)
print(answer)


