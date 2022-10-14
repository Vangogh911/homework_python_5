# 2. Создайте программу для игры с конфетами человек против человека.
#
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random


def user_input():
    while True:
        player_answer = input("Сколько конфет забрать?: ")
        while not (player_answer.isdigit() and 0 < int(player_answer) < 29):
            print("Некорректный ввод. Введите число от 1 до 28?")
            player_answer = input("Сколько конфет забрать?: ")
        else:
            player_answer = int(player_answer)
            return player_answer


def bot(counter):
    if 29 < counter < 57:
        value = counter - 29
    else:
        value = 28
    return value


counter = 150

bot_on = False
play_with_bot = input("Играть с ботом? (y/n): ")
while play_with_bot not in "yn":
    print("Введите 'y' если да и 'n' если нет.")
    play_with_bot = input("Играть с ботом? (y/n): ")
else:
    if play_with_bot == "y":
        bot_on = True

turn = random.randint(0, 1)
win = False
while not win:
    if turn:
        print("Ход игрока №1")
        counter -= user_input()
        if counter <= 0:
            print("-" * 13)
            print("Конец игры")
            print("-" * 13)
            print("Победил игрок №1")
            win = True
        else:
            print(f"Осталось {counter} конфет")
        turn = False
    else:
        print("Ход игрока №2")
        if bot_on:
            counter -= bot(counter)
        else:
            counter -= user_input()
        if counter <= 0:
            print("-" * 13)
            print("Конец игры")
            print("-" * 13)
            print("Победил игрок №2")
            win = True
        else:
            print(f"Осталось {counter} конфет")
        turn = True
