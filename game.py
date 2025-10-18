"""
игра с угадыванием числа.

число загадывает компьютер в
выбранном пользователем диапазоне.

поддерживает команды для просмотра истории угаданных
чисел и смены диапазона в процессе игры.
"""
import random
import time

history = list()


def show_commands():
    """выводит список доступных команд."""
    print("""
0  — показать команды
-1 — сменить максимальное число (применится в новой игре)
-2 — показать список угаданных чисел
""")


def check_max(prompt_text):
    """проверяет значение.

    максимальное число во избежание ошибок
    должно быть больше нуля.
    """
    while True:
        try:
            maximal = int(input(prompt_text))
            if maximal > 0:
                return maximal
            else:
                print('число должно быть больше нуля')
        except ValueError:
            print('ошибка ввода, введите целое число')
        except KeyboardInterrupt:
            print('игра прервана пользователем, ввод пропущен')
            continue


old_attempts = 0
counter = 0
total_att = 0
attempts = 1
print('-' * 40)
print('"0" для вывода доступных команд')
print('-' * 40)
maximal = check_max('введите максимальное число: ')
old_max = maximal
print('-' * 40, '\n')
print(f' ~~ диапазон чисел: 1 - {maximal} ~~ ')
time.sleep(0.7)
print('игра начинается!')
time.sleep(0.3)
print()
while True:
    number = random.randint(1, maximal)
    while True:
        try:
            prompt = int(input('введите число: '))
            if prompt == 0:
                show_commands()
                continue
            if prompt == -1:
                print()
                print('выбрана смена максимального числа. ', end='')
                print('будет применено в новой игре')
                maximal = check_max('введите новое число: ')
                print(f'новый диапазон чисел: 1 - {maximal}')
                print()
                print(f' ~~ актуальный диапазон: 1 - {old_max} ~~ ')
                old_max = maximal
                continue
            if prompt == -2:
                print()
                print(f'список угаданных чисел: {history} \n')
                time.sleep(0.5)
                continue
            if prompt < number:
                print('загаданное число больше')
                time.sleep(0.15)
                attempts += 1
            elif prompt > number:
                print('загаданное число меньше')
                time.sleep(0.15)
                attempts += 1
            elif prompt == number:
                print()
                print('-' * 40)
                print(f'вы угадали! загаданное число: {number}')
                print(f'попыток: {attempts}')
                time.sleep(0.5)
                total_att += attempts
                counter += 1
                history.append(number)
                average_atts = round(total_att / counter, 3)
                print(f'среднее количество попыток: {average_atts}')
                print('-' * 40)
                time.sleep(0.3)
                if old_attempts > 0:
                    if old_attempts > attempts:
                        less_diff = old_attempts - attempts
                        print(f'быстрее на {less_diff} попыток по \
сравнению с предыдущим результатом!')
                    elif old_attempts < attempts:
                        more_diff = attempts - old_attempts
                        print(f'позднее на {more_diff} попыток по \
сравнению с предыдущим результатом!')
                    elif old_attempts == attempts:
                        print('столько же попыток, сколько и в прошлый раз!')
                    print('-' * 40)

                old_attempts = attempts
                attempts = 1
                print()
                print(f' ~~ диапазон чисел: 1 - {maximal} ~~ ')
                break
        except ValueError:
            print()
            print('ошибка ввода, введите целое число')
            show_commands()
            continue
        except KeyboardInterrupt:
            print('игра прервана пользователем, ввод пропущен')
            show_commands()
            continue
        except Exception as error:
            print(f'неизвестная ошибка: {error}')
            continue
