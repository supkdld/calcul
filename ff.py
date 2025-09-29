print( "Добро пожаловать в калькулятор!")
print("Выберите операторы, с которыми будете работать:")
print("Арифметические операторы (Сложение: +,Вычитание: -, Умножение: *, Деление: /, Целочисленное деление //, Остаток от деления %, Возведение в степень **)")
print("Операторы сравнения (Равно ==, Не равно !=, Больше >, Меньше <, Больше или равно >=, Меньше или равно <=)")
print("Логические операторы (И - and, ИЛИ - or, НЕ - not)")
print("Операторы принадлежности (В - in, Не в - not in)")
print("Операторы тождественности (Является - is, Не является - is not)")
operat=int(input( "Арифмет. - 1, Сравн. - 2, Лог. - 3, Принад. - 4, Тожд. - 5: "))
if operat == 1:
    znak = input("Выберите желаемую операцию: ")
    a= int(input("Введите первое число: "))
    b= int(input("Введите второе число: "))
    if znak =="+":
        print(a,"+", b, "=", a+b)
    elif znak =="-":
        print(a,"-", b, "=", a-b)
    elif znak =="*":
        print(a,"*", b, "=", a*b)
    elif znak =="/":
        if b==0:
            print("На ноль делить нельзя")
        else:
            print(a,"/", b, "=", a/b)
    elif znak =="//":
        if b==0:
            print("На ноль делить нельзя")
        else:
            print(a,"//", b, "=", a//b)
    elif znak =="%":
        if b==0:
            print("На ноль делить нельзя")
        else:
            print(a,"%", b, "=", a%b)
    elif znak =="**":
        print(a,"**", b, "=", a**b)
    else:
        print("Проверьте правильность написания операции!")
elif operat == 2:
    znak = input("Выберите желаемую операцию: ")
    a= int(input("Введите первое число: "))
    b= int(input("Введите второе число: "))
    if znak == "==":
        if a==b:
            print("True")
        else:
            print("False")
    elif znak == "!=":
        if a!=b:
            print("True")
        else:
            print("False")
    elif znak == ">":
        if a>b:
            print("True")
        else:
            print("False")
    elif znak == "<":
        if a<b:
            print("True")
        else:
            print("False")
    elif znak == ">=":
        if a>=b:
            print("True")
        else:
            print("False")
    elif znak == "<=":
        if a<=b:
            print("True")
        else:
            print("False")
    else:
        print("Проверьте правильность написания операции!")
elif operat == 3:
    znak = input("Выберите желаемую операцию: ")
    if znak == "not":
        a = input("Введите число 0/1 или значение True/False: ")
        if a in ("True", "1"):
            a = True
        elif a in ("False", "0"):
            a = False
        else:
            print("Проверьте правильность написания значения!")
        print("not", a, "is: ", not a)
    elif znak =="and" or "or":
        a=input("Введите первое число 0/1 или значение True/False: ")
        b=input("Введите второе число 0/1 или значение True/False: ")
        if a in ("True", "1"):
            a= True
        elif a in ("False","0"):
            a=False
        else:
             print("Проверьте правильность написания значения!")
        if b in ("True", "1"):
            b= True
        elif b in ("False","0"):
            b=False
        else:
             print("Проверьте правильность написания значения!")
        if znak=="and":
            print(a ,"and", b, "is", a and b)
        elif znak=="or":
            print(a ,"or", b ,"is", a or b)
    else:
        print("Проверьте правильность написания операции!")
elif operat == 4:
    znak = input("Выберите желаемую операцию: ")
    a=(input("Введите первое большое число: "))
    b=(input("Введите второе число: "))
    if znak=="in":
        if b in a:
            print("True")
        else:
            print("False")
    if znak=="not in":
        if b  not in a:
            print("True")
        else:
            print("False")
    else:
        print("Проверьте правильность написания операции!")
elif operat==5:
    a= int(input("Введите первое число: "))
    b= int(input("Введите второе число: "))
    znak = input("Выберите желаемую операцию: ")
    print(f"a = '{a}' (тип: {type(a)}, id: {id(a)})")
    print(f"b = '{b}' (тип: {type(b)}, id: {id(b)})")
    if znak =="is":
        cc=a is b
        print(f"a is b = {cc}")
    elif znak=="is not":
        cc=a is not b
        print(f"a is not b = {cc}")
    else:
       print("Проверьте правильность написания операции!")

        
