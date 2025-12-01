import random
import os

def create_statistika():
    if not os.path.exists("statistika"):
        os.makedirs("statistika")

def save_statistika(size, winner, moves):
    with open("statistika/games.txt", "a",encoding='cp1251') as file:
        file.write("Размер поля: "+str(size)+", Победитель игры: "+winner+", Действий было сделано: "+str(moves)+"\n")

def skolko_size():
    while True:
        try:
            size = int(input("Введите размер поля от 3 до 9): "))
            if size >= 3 and size <= 9:
                return size
            print("Введите размер, соответствующий требованиям!!")
        except:
            print("Введите целое натуральное число!!")

def print_pole(pole):
    size = len(pole)
    print("   ", end="")
    for stolb in range(size):
        print(stolb + 1, end=" ")
    print()
    for ryad in range(size):
        print(ryad + 1, end="  ")
        for stolb in range(size):
            print(pole[ryad][stolb], end=" ")
        print()
    print()

def proverka_na_pobedu(pole):
    size = len(pole)
    for ryad in range(size):
        perv_kletka = pole[ryad][0]
        if perv_kletka == '.':
            continue
        vse_sovp = True
        for stolb in range(size):
            if pole[ryad][stolb] != perv_kletka:
                vse_sovp = False
                break        
        if vse_sovp:
            return perv_kletka
    
    for stolb in range(size):
        perv_kletka = pole[0][stolb]
        if perv_kletka == '.':
            continue
        vse_sovp = True
        for ryad in range(size):
            if pole[ryad][stolb] != perv_kletka:
                vse_sovp = False
                break       
        if vse_sovp:
            return perv_kletka
        
    perv_kletka = pole[0][0]
    if perv_kletka != '.':
        vse_sovp = True
        for i in range(size):
            if pole[i][i] != perv_kletka:
                vse_sovp = False
                break      
        if vse_sovp:
            return perv_kletka
        
    perv_kletka = pole[0][size-1]
    if perv_kletka != '.':
        vse_sovp = True
        for i in range(size):
            if pole[i][size-1-i] != perv_kletka:
                vse_sovp = False
                break
        if vse_sovp:
            return perv_kletka
        
    vse_full = True
    for ryad in pole:
        for kletka in ryad:
            if kletka == '.':
                vse_full = False
                break
        if not vse_full:
            break
            
    if vse_full:
        return "Ничья"
    
    return None

def move_igroka(pole, player):
    size = len(pole)
    while True:
        try:
            move = input("Ход игрока "+player+". Введите координату вашего хода (например: 1 2): ")
            ryad, stolb = map(int, move.split())
            if ryad >= 1 and ryad <= size and stolb >= 1 and stolb <= size and pole[ryad-1][stolb-1] == '.':
                return ryad-1, stolb-1
            print("Неверный ход, проверьте на соответсвие условиям!!")
        except:
            print("Неверный ввод, проверьте на соотвествие условиям!!")

def move_robot(pole):
    size = len(pole)
    svobod_kletki = []
    for ryad in range(size):
        for stolb in range(size):
            if pole[ryad][stolb] == '.':
                svobod_kletki.append((ryad, stolb))
    random_kletka = random.choice(svobod_kletki)
    return random_kletka

def choose_rezim():
    while True:
        rezim = input("Выберите режим игры (1 - PVP, 2 - PVE): ")
        if rezim in ["1", "2"]:
            return int(rezim)
        print("Введите 1 или 2!!")

def play():
    create_statistika()  
    while True:
        size = skolko_size()
        rezim = choose_rezim()
        tek_player = random.choice(["X", "O"])
        moves = 0
        
        pole = []
        for i in range(size):
            ryad = []
            for j in range(size):
                ryad.append(".")
            pole.append(ryad)
        
        print("Первым ходит: "+tek_player)
        
        while True:
            print_pole(pole)
            if rezim == 1 or (rezim == 2 and tek_player == 'X'):
                ryad, stolb = move_igroka(pole, tek_player)
            else:
                ryad, stolb = move_robot(pole)
                print("Робот совершил действие "+tek_player+" на позиции: "+str(ryad+1)+" "+str(stolb+1))
            
            pole[ryad][stolb] = tek_player
            moves += 1
            
            result = proverka_na_pobedu(pole)
            if result:
                print_pole(pole)
                if result == "Ничья":
                    print("Ничья!!")
                else:
                    print(result+" побеждает!")
                save_statistika(size, result, moves)
                break
            
            if tek_player == 'X':
                tek_player = 'O'
            else:
                tek_player = 'X'

        while True:
            again = input("Хотите сыграть еще? (да/нет): ").lower()
            if again == 'да':
                break
            elif again == 'нет':
                return
            else:
                print("Введите да или нет!!")

play()
