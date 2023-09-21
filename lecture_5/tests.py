a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]


def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] for i, val in enumerate(array)]


def test_mask_list():
    print('проверяем тест маск лист')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0], 'маск работает'


test_mask_list()
print('всё работает')
answer_1 = []
answer_1 = [val * b[i] for i, val in enumerate(a)]                      # вариант 1 - main
print(answer_1)


# answer_2 =  []
# for i, val in enumerate(a):                                  # вариант 2
#    answer_2.append(val * b[i])
#    print(answer_2)

# for i, val in enumerate
# print(f'index = {i}')
# print(f'valuse = {val}')