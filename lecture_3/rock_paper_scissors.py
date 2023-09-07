first_player: str = ('камень', 'ножницы','бумага')       #спросить, можно ли первые две строчки объеденить, и зачем тогда нужон был этот ваш регистр
second_player: str = ('камень', 'ножницы','бумага')
first_player, second_player = input('Ввод: ').split(' ')
if first_player == second_player:
     print ('ничья')
elif first_player == 'ножницы':
    if second_player == 'бумага':
        print('Первый игрок победил')
    else:
        print('Второй игрок победил')
elif first_player == 'камень':
    if second_player == 'ножницы':
         print('Первый игрок выиграл')
    else:
         print('Второй игрок выиграл')
elif first_player == 'бумага':
    if second_player == 'камень':
         print('Первый игрок победил')
    else:
        print('Второй игрок выиграл')


# first_player: str 
# second_player: str
# first_player, second_player = input('Ввод: ').lower().split(' ')
# if first_player == second_player:
#      print ('ничья')
# elif first_player == 'ножницы':
#     if second_player == 'бумага':
#         print('Первый игрок победил')
#     elif second_player =='камень':
#         print('Второй игрок победил')
# elif first_player == 'камень':
#     if second_player == 'ножницы':
#          print('Первый игрок выиграл')
#     elif second_player =='бумага':
#          print('Второй игрок выиграл')
# elif first_player == 'бумага':
#     if second_player == 'камень':
#          print('Первый игрок победил')
#     elif second_player =='ножницы':
#         print('Второй игрок выиграл')

