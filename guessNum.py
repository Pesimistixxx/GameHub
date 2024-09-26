def guessNum():
    from random import randint
    import datetime
    def gameProccess(randomInt):
        num = input()
        if num.isdigit():
            if int(num) > randomInt:
                print("Меньше")
            elif int(num) < randomInt:
                print("Больше")
            else:
                return True
    a = randint(0,100)
    cnt = 1
    print("Добро пожаловать в игру Больше/Меньше-------------------------------\n"
          "Суть игры угадать число, а консоль будет говорить больше или меньше\n"
          "-------------------------------------------------------------------\n"
          "Введите максимальное число, которое сможет выпасть")
    randmax = input()
    while randmax.isdigit() == False or int(randmax) <= 0:
        print("Неверный ввод")
        randmax = input()
    print("Попытайтесь угадать загаданное число-------------------------------")
    randomInt = randint(0,int(randmax))
    start = datetime.datetime.now()
    while gameProccess(randomInt) != True:
        cnt += 1
    finish = datetime.datetime.now()
    time = str(finish - start)
    print("Вы угадали загаданное число", randomInt, "за" , cnt , "ходов", time, "времени")
    print("Выберите следующюю игру или напишите exit для выхода")
    return 0