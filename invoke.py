def invoke():
    print("Добро пожаловать в игру Invoke\n"
          "Суть игры как можно быстрее набрать последовательность из 10 заклинаний\n"
          "Список заклинаний------------------------------------------------------\n"
          "|Cold Snap : QQQ  |"
          "Ghost Walk : QQW\n"
          "|Ice Wall : QQE   |"
          "EMP : WWW\n"
          "|Tornado : WWQ    |"
          "Alacrity : WWE\n"
          "|Sun Strike : EEE |"
          "Forge Spirit : EEQ\n"
          "|Meteor : EEW     |"
          "Deaf. Blast : QWE\n"
          "------------------------------------------------------------------------")
    from random import randint
    import datetime
    spells = {"Cold Snap" : "QQQ",
               "Ghost Walk" : "QQW",
               "Ice Wall" : "QQE",
               "EMP" : "WWW",
               "Tornado" : "WWQ",
               "Alacrity" : "WWE",
               "Sun Strike" : "EEE",
               "Forge Spirit" : "EEQ",
               "Meteor" : "EEW",
               "Deaf. Blast" : "QWE"}
    spelltoint = ["Cold Snap", "Ghost Walk", "Ice Wall", "EMP", "Tornado", "Alacrity", "Sun Strike", "Forge Spirit", "Meteor", "Deaf. Blast"]
    cnt = 0
    print("Напишите \"GO\" если готовы")
    p = input()
    while p != "GO":
        p = input()
    start = datetime.datetime.now()
    while cnt != 10:
        randomint = randint(0,9)
        print(spelltoint[randomint])
        inp = input()
        while inp != spells[spelltoint[randomint]]:
            print("НЕПРАВИЛЬНО")
            inp = input()
        cnt += 1
    finish = datetime.datetime.now()
    time = str(finish - start)
    print("Вы прошли игру за", time, "времени")
    print("Выберите следующую игру или напишите exit для выхода")
    return 0