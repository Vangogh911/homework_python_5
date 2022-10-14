# 3. Создайте программу для игры в 'Крестики-нолики'.


def game_field(net):
    print("-" * 13)
    for i in range(3):
        print("|", net[i * 3], "|", net[1 + i * 3], "|", net[2 + i * 3], "|")
        print("-" * 13)


def user_input(x_o, net):
    end_turn = False
    while not end_turn:
        player_answer = input("Выберите клетку для " + x_o + ": ")
        while player_answer not in "123456789":
            print("Некорректный ввод. Введите число от 1 до 9?")
            player_answer = input("Выберите клетку для " + x_o + ": ")
        else:
            player_answer = int(player_answer)
        if str(net[player_answer - 1]) not in "XO":
            net[player_answer - 1] = x_o
            end_turn = True
        else:
            print("Эта клетка уже занята!")


def check_win(net):
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for cell in win_combo:
        if net[cell[0]] == net[cell[1]] == net[cell[2]]:
            return net[cell[0]]
    return False


field = list(range(1, 10))
counter = 0
win = False
while not win:
    game_field(field)
    if counter % 2 == 0:
        user_input("X", field)
    else:
        user_input("O", field)
    counter += 1
    if counter > 4:
        tmp = check_win(field)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
    if counter == 9:
        print("Ничья!")
        break
game_field(field)
