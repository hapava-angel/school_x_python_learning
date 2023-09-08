from import_this import (
    generate_race_data,
    RaceInfo,
    )
 

def sort_racers(RACE_DATA: dict) -> dict:
    order_rd: dict = {}
    for value in RACE_DATA.values():
        finishplace: int  = ["FinishedPlace"]
        order_rd[finishplace] = value
    return order_rd


def print_first_racer(order_rd: dict) -> str:
    congrat: str =  f'Выиграл - {order_rd[1]["RacerName"]}!!!!!!!!!!!!!!!!!!!! Поздравляем!!'
    print(congrat + '\n' + '-' * len(congrat))


def print_top3_racers(order_rd: dict) -> str:
    print('Первые три места:\n')
    for m in range(1, 4):
        value: dict = order_rd[m]
        print(f'Гонщик на {m} месте\n' +
              f'\t Имя: {value ["RacerName"]} \n' +
              f'\t Команда: {value ["RacerTeam"]} \n' +
              f'\t Время: {value ["FinishedTimeSeconds"] // 3600}:'+
              f'{value ["FinishedTimeSeconds"] // 60}:' +
              f'{value ["FinishedTimeSeconds"] % 60} (H:M:S)'
              )


if __name__ == '__main__':
    race_data: RaceInfo = generate_race_data(10)
    print_first_racer(race_data)
    print_top3_racers(race_data)
