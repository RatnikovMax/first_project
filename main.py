from random import randint
import datetime


def play_game(player_name):
    number = randint(1, 100)
    print(f'\n{player_name}, угадайте число от 1 до 100')

    attempts = 0
    start_time = datetime.datetime.now()

    while True:
        guess = int(input('Введите число: '))
        attempts += 1

        if guess < number:
            print('Ваше число меньше того, что загадано.')
        elif guess > number:
            print('Ваше число больше того, что загадано.')
        elif guess == number:
            end_time = datetime.datetime.now()
            game_duration = end_time - start_time
            print('Отличная интуиция! Вы угадали число :)\n')
            return number, attempts, game_duration


def save_game_info(player_name, number, attempts, game_duration, filename='game_stats.txt'):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Игрок: {player_name}\n")
        file.write(f"Загаданное число: {number}\n")
        file.write(f"Потребовалось попыток: {attempts}\n")
        file.write(f"Время игры: {game_duration}\n")
        file.write(f"Дата и время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("-" * 50 + "\n")


def main():
    """Основная функция программы"""
    print("=== ИГРА 'УГАДАЙ ЧИСЛО' ===")
    player_name = input("Введите ваше имя: ")

    while True:
        number, attempts, game_duration = play_game(player_name)

        save_game_info(player_name, number, attempts, game_duration)

        print(f"Статистика этой игры:")
        print(f"Загаданное число: {number}")
        print(f"Попыток: {attempts}")
        print(f"Время: {game_duration}")

        print("\nВыберите действие:")
        print("1. Продолжить игру")
        print("2. Выйти из игры")

        choice = input("Введите номер действия (1 или 2): ")

        if choice == '2':
            print(f"Спасибо за игру, {player_name}! До свидания!")
            break
        elif choice != '1':
            print("Неверный ввод. Игра завершается.")
            break

if __name__ == "__main__":
    main()