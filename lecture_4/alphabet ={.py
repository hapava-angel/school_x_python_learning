# from typing import TypeAlias

# IntOrNoneType = int | None

# ComplicatedDict: TypeAlias = dict[int | str | None]

# alphabet: dict[int|str|None|float, str|list|set |int |float |dict] ={ ...}   #все нужные типа
    
    
# print(
#     alphabet.get(4).get(3)get('A')
# O_letter = alphabet.get('O', None)
# if not bool(O_letter):                                                                 #if not O_letter:
#     print('NO O')                                                                      #LBYL - if переменная существует
# for key, value in alphabet.items(): #.key.values()                                     #EAFP - try catch    #get вытасуивает переменную из dictionary, если не найдет - то выведет None
#     if value in 'AY':
#         print(f'Ключ: {key} Значение: {value}')

