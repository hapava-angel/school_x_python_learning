# new_name: str = input('type name: ')
# greet_massenge: str = 'hello bob'

# greet_massenge: str = 'hello bob'

# # greet_massenge: str = (
# #     greet_massenge [-3] + new_name

# # )

# greet_massenge: str = \
#     greet_massenge.replace('bob', f' new_name')

# print(greet_massenge)

# river: str = 'mmmmississippi'

# print(
#     'm' + river.lstrip('m')
# )

# words: str = '<!----- dsa dsa dsa-----!>'

# print(
#     words.strip('<!>-').split()
# )


# import string

# numbers: str = string.digits
# word: str = 'hell23o b24ob ho35w ar2e e9458ou'

# for number in numbers:
#     word = word.replace(number, '')
# _word: str = ''
# _sum: float = 0
# _prod: float = 1  #для переменных - пустые штуки
# _list: list = []
# _set: set = set([])
# _dict: dict = {}


words: str = 'Hello Bob, are you a bob? BOB!!!'
# words = words.lower().find('bob')
while True:
    bob_index = words.lower().find('bob')
    if bob_index == -1:
        break
    else:
        words = (
            words[:bob_index] + 'Gregpry' + words[bob_index+len('bob'):]
        )
        # words = words[:bob_index]
        # words = words.lower().replace('bob', 'gregory')
        # print(words)
print(words)
# print(
#     words
# )



# for ch in word:
#     if ch in numbers:
#         continue
#     else: 
#         _word += ch
# word = _word
# del _word
        
# print(
#     word.replace(numbers, '')
# )




_list: list = [1, 2, 3]
_str: str = '123'
_tuple: tuple = (1, 2, 3)


_list[-1] = 5
_str[-1] = 5 #нельзя менять
_tuple[-1] = 5 #тоже нельзя менять, но эо список из чисел, хранит инты
_tuple: tuple = (
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
)
_list[-1] = 5
_tuple [1][1] = 5

#3 -> 5
print(_list, _str, _tuple)