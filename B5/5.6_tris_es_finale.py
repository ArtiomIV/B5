import random
field = [[" "] * 3 for i in range(3)]

def game_board(field):
    print("   | 0 | 1 | 2 |")
    print( "-----------------" )
    for i in range(3):
        row_str = " | " + " | ". join(field[i]) + " | "
        print( f"{i} {row_str}" )
        print( "-----------------" )
    return field

def ask_name():
    user = input( "Введите имя первого игрока: " )
    user_1 = input( "Введите имя второго игрока: " )
    random_value = random.choice("x" "o")
    print(random_value)
    dict_ = {}
    if random_value == "x":
        dict_[user], dict_[user_1] = "x", "o"
        print( f"Игроку {user} присвоен знак 'x' \nигроку {user_1} присвоен занк 'o'" )
    else:
        dict_[user], dict_[user_1] = "o", "x"
        print( f"Игроку {user} присвоен знак 'o' \nигроку {user_1} присвоен занк 'x'" )
    return dict_

def ask():
    while True:
        coords = input( " Ваш ход (x, y): ").split()
        if len(coords) != 2:
            print( "Введите 2 числа" )
            continue
        x, y = coords
        
        if not x.isdigit() or not y.isdigit():
            print( "Введите числа!" )
            continue

        x, y = int(x), int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("Позиция занята")
        else:
            print("Координаты вне диапазона")


def check_win(check_list):
    win_coord = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 1), (1, 1), (2, 1))
    )
    name_list = []
    for key, value in check_list.items():
        if check_list[key] == "x":
            name_list.insert(0, key)
        elif check_list[key] == "o":
            name_list.insert(1, key)
    user_1 = name_list[0]
    user_2 = name_list[1]
    for coord in win_coord:
        list_ = []
        for c in coord:
            a, b = c
            list_.append(field[a][b])
            if list_ == ["x", "x", "x"]:
                print(f"Выиграл игрок >>{user_1}<<")
                return True
            elif list_ == ["o", "o", "o"]:
                print(f"Выиграл игрок >>{user_2}<<")
                return True
    return False

check_list = ask_name()

num = 0
while True:
    num += 1

    print( f"Номер хода {num}" )
    game_board(field)

    if num % 2 == 0:
        print( "Ходит x" )
        x, y = ask()
        field[x][y] = "x"
    else:
        print( "Ходит o" )
        x, y = ask()
        field[x][y] = "o"
    
    game_board(field)

    if check_win(check_list):
        print("Игра окончена")
        break
    
    elif num == 9:
        print("Ничья")
        break
