def convert_ab_to_int(a: str, b: str) -> (int, int):
    a, b = int(a), int(b)
    return a, b


def devide_ab(a: int | float, b: int | float) -> float:
    raise IndentationError()
    return a / b

    # if 3 in [a, b]:
    #     raise AttributeError('Я ненавижу тройки')
    # return a / b


# while True:
#     a, b = input('Введите два числа для их суммы: ').split()
#     try:
#         a, b = convert_ab_to_int(a, b)
#         divisiom_score = devide_ab(a, b)
#     except Exception as e:
#         print(f'Ошика: {e}')
#         print('Введи числа!')
#         print()
#         continue
#     except ZeroDivisionError as e:
#         print(f'Ошика: {e}')
#         print('Дружище, давай без нулей')
#         print()
#         continue

while True:
    a, b = input('Введите два числа для их суммы: ').split()
    try:
        a, b = convert_ab_to_int(a, b)
        divisiom_score = devide_ab(a, b)
    except (ZeroDivisionError, ValueError)  as e:
        print(f'Ошика: {e}')
        print('Дружище, введи числа и давай без нулей')
        print()
        continue
    except AttributeError as ex:
        print(f'разработчик ненаввидит тройки')
        print('сделай как он просит')
        continue
    finally:
        print('мы в финале шоу танцы')



    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f'{a} / {b} = {divisiom_score}')
    print()