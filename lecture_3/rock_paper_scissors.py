first_player, second_player = input('Ввод: ').split(' ')
words: list = ['камень', 'ножницы', 'бумага']
if first_player and second_player in words:
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