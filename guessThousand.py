def guessThousand():
    from random import randint
    import datetime
    def numValidation(num):
        if num.isdigit() == True:
            if int(num) >= 1000 and int(num) <= 9999:
                return True
        return False
    print("-----------------------------------------------------------------------------------\n"
          "Добро пожаловать в игру угадай число\n"
          "Суть игры угадать загаданное число\n"
          "Программа будет писать сколько чисел стоят на своем месте, а сколько есть в числе\n"
          "----------------------------------------------------------------------------------")
    cnt = 1
    a = randint(1000,9999)
    a = str(a)
    #print(a)
    start = datetime.datetime.now()
    num = input()
    while num != str(a):
        cnt += 1
        while numValidation(num) == False:
            print("Неправильный ввод")
            num = input()
        else:
            atnum = 0
            inum = 0
            acnt = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            numcnt = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            for i in range(4):
                if num[i] == a[i]:
                    atnum += 1
                acnt[int(a[i])] = acnt[int(a[i])] + 1
                numcnt[int(num[i])] = numcnt[int(num[i])] + 1
            for i in range(10):
                inum += min(acnt[i],numcnt[i])
            print("Чисел на нужном месте",atnum,"Чисел не на своем месте",inum-atnum)
        num = input()
    finish = datetime.datetime.now()
    time = str(finish - start)
    print("Победа за", cnt , "ходов", time, "времени")
    print("Выберите следующую игру или напишите exit для выхода")
    return 0