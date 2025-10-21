import time
print("МПТ")
print("Ваша цель: проникнуть в здание, найти ваш второй телефон и выбраться!")
print("Осторожно: повсюду преподаватели и охранники!")
time.sleep(3)
inventory = []   #это список, в который будут добавляться вещи!
locations = {    #это слловарь с названием локации и ее описания!
    "entrance": "Вы стоите перед входом воротами техникума. Ворота закрыты, зачем туда идти? ",
    "corridor": "Тихий корридор. Кажется, идет пара.",
    "classroom": "Большая пустая комната с партами. Здесь темно и страшно. Где все?",
    "exit": "Вы на свободе! Ура!"
}
enemies = { #это словарь с названием врага и его описанием!
    "guard": "ОХРАННИК!!! Если поймает, придется писать объяснительную...",
    "literatur": "ОЙ ОЙ, это же Петкова! Может, попробовать ее впечатлить?",
    "physic": "ТРЕВОГА! СУДОПЛАТОВ...Кажется, он смотрит довольно угрожающе! Надо его впечатлить."
}
completed_tasks = set() #это множество для добавления выполненных действий!
codes = ("0000","1234") #это кортеж с кодами!
print("УРОВЕНЬ 1: ПРОНИКНОВЕНИЕ В ЗДАНИЕ")
time.sleep(2)
print("Вы пытаетесь попасть в учебное заведение без пропуска. Смело...")
time.sleep(1)
level1_completed = False
guard_defeated = False
while level1_completed == False:
    print(locations["entrance"])
    time.sleep(1)
    print("--- ВАШИ ДЕЙСТВИЯ ---")
    print("1 - Посмотреть на ворота")
    print("2 - Поискать что-то полезное вокруг")
    print("3 - Открыть инвентарь")
    print("4 - Попробовать войти")
    time.sleep(2)
    choice = input("Что выберете? (1/2/3/4): ")
    if choice == "1":
        print("Ворота закрыты. Это что, кодовый замок? Нужен пароль!")
        time.sleep(1)
    elif choice == "2":
        print("Вы нашли бумажку под камнем!")
        inventory.append("бумажка с кодом")
        print("Ваши вещи:", inventory)
        time.sleep(1)
    elif choice == "3":
        if inventory:
            print("Сейчас у вас:", inventory)
            if "бумажка с кодом" in inventory:
                print("На бумажке написано: Зачем вам код от входа...Ладно, код: 1234")
                time.sleep(1)
        else:
            print("У вас пока ничего нет")
            time.sleep(1)
    elif choice == "4":
        if "бумажка с кодом" in inventory:
            code = input("Введите код от замка: ")
            if code == "1234" or "0000":
                print("Замок открылся! Ворота скрипнули...")
                time.sleep(1)
                completed_tasks.add("открыл ворота")
                print("ВНЕЗАПНО! " + enemies["guard"])
                time.sleep(1)
                print("Охранник приближается к вам!")
                time.sleep(1.3)
                while guard_defeated == False:
                    print("--- СПАСАЙТЕСЬ ОТ ОХРАННИКА! ---")
                    print("1 - Спрятаться в кустах")
                    print("2 - Не двигаться") 
                    print("3 - Бросить камень для отвлечения")
                    time.sleep(1)
                    action = input("Что будете делать? (1/2/3): ")
                    if action == "1":
                        print("Вы спрятались в кустах! Охранник прошел мимо!")
                        completed_tasks.add("убежал от охранника")
                        time.sleep(2)
                        guard_defeated = True
                    elif action == "2":
                        print("Вы сказали: 'Я опоздал на пару!'")
                        time.sleep(1)
                        print("Охранник: 'Покажите студенческий!'")
                        time.sleep(0.5)
                        print("Ой...У вас нет студенческого! Вас поймали!")
                        time.sleep(1)
                        exit()
                    elif action == "3":
                        print("Вы бросили камень в сторону!")
                        time.sleep(1)
                        print("Охранник пошел проверять шум! Бегите!")
                        time.sleep(1)
                        completed_tasks.add("отвлек охранника")
                        guard_defeated = True
                    else:
                        print("Неправильный выбор!")
                print("НОВАЯ ОПАСНОСТЬ! " + enemies["physic"])
                time.sleep(1)
                print("Господин Судоплатов блокирует путь в коридор!")
                time.sleep(0.6)
                print("Он считает вас злостным прогульщиком...")
                time.sleep(1)
                physic_defeated = False
                while physic_defeated == False:
                    print("--- ВЫЗОВ БОГА ФИЗИКИ ---")
                    print("Он спрашивает: 'Что измеряется в Ньютонах?'")
                    print("1 - Сила")
                    print("2 - Скорость")
                    print("3 - Температура")
                    print("4 - Время")
                    time.sleep(1)
                    physics_answer = input("Ваш ответ? (1/2/3/4): ")
                    if physics_answer == "1":
                        print("ВЕРНО! Сила измеряется в Ньютонах!")
                        time.sleep(1)
                        print("Бог физики доволен и пропускает вас!")
                        time.sleep(1)
                        completed_tasks.add("победил бога физики")
                        physic_defeated = True
                        level1_completed = True
                    else:
                        print("НЕПРАВИЛЬНО! Кажется, придется писать объяснительную...")
                        time.sleep(1)
                        exit()
            else:
                print("Неверный код! Попробуйте еще раз!")
        else:
            print("У вас нет кода! Сначала найдите подсказку!")
    else:
        print("Такого действия нет! Выберите 1, 2, 3 или 4")
print("УРОВЕНЬ 2: ПОИСК ТЕЛЕФОНА И ПОБЕГ")
time.sleep(0.8)
print("Вы внутри здания! Вы же пришли сюда только за вторым телефоном, оставленным где-то в аудитории... Теперь нужно найти телефон и выбраться!")
time.sleep(1)
print(locations["corridor"])
print("Где хоть один отдыхающий на диванчике студент?")
time.sleep(2)
found_phone = False
found_key = False
level2_completed = False
in_classroom = False
while not level2_completed:
    if not in_classroom:
        print("--- ВАШИ ДЕЙСТВИЯ В КОРИДОРЕ ---")
        print("1 - Осмотреть коридор")
        print("2 - Пойти к аудитории литературы и русского языка")
        print("3 - Посмотреть инвентарь")
        time.sleep(0.5)
        choice = input("Ваш выбор? (1/2/3): ")
        if choice == "1":
            print("В коридоре много дверей. Из некоторых доносится шум.")
            time.sleep(1)
            print("Кажется, вы забыли забрать телефон после литературы!")
            time.sleep(1)
        elif choice == "2":
            print(locations["classroom"])
            time.sleep(0.6)
            in_classroom = True
        elif choice == "3":
            if inventory:
                print("Ваши вещи:", inventory)
            else:
                print("У вас пока ничего нет")
        else:
            print("Неправильный выбор!")
    else:
        print("--- ВАШИ ДЕЙСТВИЯ В АУДИТОРИИ ---")
        time.sleep(1)
        print("1 - Осмотреть аудиторию")
        if not found_phone:
            print("2 - Искать телефон")
        if not found_key:
            print("3 - Искать ключ")
        print("4 - Вернуться в коридор")
        print("5 - Посмотреть инвентарь")
        if found_phone and found_key:
            print("6 - Попробовать выйти")
        time.sleep(1)
        choice = input("Ваш выбор? (1/2/3/4/5/6): ")
        if choice == "1":
            print("Вы осматриваете аудиторию:")
            time.sleep(0.5)
            print("   - Парты стоят в беспорядке")
            time.sleep(0.5)
            print("   - На доске какие-то надписи...Ну и почерк!")
            time.sleep(0.5)
            print("   - В углу стоит шкаф с тетрадями")
            time.sleep(0.5)
            if not found_phone:
                print("   Возможно телефон где-то здесь...")
                time.sleep(0.5)
            if not found_key:
                print("   Нужно будет найти ключ от черного выхода...")
                time.sleep(0.5)
        elif choice == "2" and not found_phone:
            print("УРА! Вы нашли свой телефон в одном из ящиков!!")
            time.sleep(1)
            inventory.append("телефон")
            found_phone = True
            print("Теперь у вас:", inventory)
            time.sleep(1)
        elif choice == "3" and not found_key:
            print("ОТЛИЧНО! Вы нашли ключ на подоконнике!")
            time.sleep(0.5)
            inventory.append("ключ от выхода")
            found_key = True
            print("Теперь у вас:", inventory)
            time.sleep(1)
        elif choice == "4":
            print("Вы возвращаетесь в коридор")
            time.sleep(1)
            in_classroom = False
        elif choice == "5":
            if inventory:
                print("Ваши вещи:", inventory)
                time.sleep(1)
            else:
                print("У вас пока ничего нет")
        elif choice == "6" and found_phone and found_key:
            print("У вас есть все необходимое! Вы бежите к выходу...")
            time.sleep(1)
            print(enemies["literatur"])
            time.sleep(0.5)
            while literatur_defeated == False:
                print("ФИНАЛЬНАЯ ЗАДАЧА: Кто из перечисленных героев является главным идеологом нигилизма в романе И.С.Тургенева Отцы и дети?")
                print("1 - Николай Петрович Кирсанов")
                print("2 - Павел Петрович Кирсанов") 
                print("3 - Евгений Базаров")
                print("4 - Аркадий Кирсанов")
                time.sleep(2)
                answer = input("Ваш ответ? (1/2/3/4): ")
                if answer == "3":
                    print("ПРАВИЛЬНО! Вы что-то помните!!")
                    time.sleep(1)
                    print("Петкова позволяет вам выйти из здания через черный ход!")
                    time.sleep(1)
                    completed_tasks.add("поразил Петкову")
                    print(locations["exit"])
                    time.sleep(1)
                    print("ПОЗДРАВЛЯЕМ! ВЫ ВЫБРАЛИСЬ ИЗ ЗДАНИЯ!")
                    time.sleep(1)
                    level2_completed = True
                    literatur_defeated = True
                else:
                    print("НЕПРАВИЛЬНО! Придется писать объяснительную!")
                    time.sleep(1)
                    exit()
        else:
            print("Неправильный выбор или вы еще не все нашли!")
print("ВЫ ВЫИГРАЛИ! ИГРА ЗАКОНЧЕНА!")
time.sleep(1)
print("ВАША СТАТИСТИКА:")
time.sleep(1)
print("Выполнено заданий:", len(completed_tasks))
print("Собрано предметов:", len(inventory))
print("Встречено врагов:", len(enemies))
print("Посещено мест:", len(locations))
print("Знаете кодов:", len(codes))
print("Ваши выполненные дела:", completed_tasks)
print("Ваши предметы:", inventory)
print("Спасибо за игру!")


