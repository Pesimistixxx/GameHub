def game19():
    def inputCheck(cmd):
        if len(cmd.split()) == 2:
            if cmd.split()[0].isdigit() and cmd.split()[-1].isdigit():
                if int(cmd.split()[0]) > 0 and int(cmd.split()[0]) <= rowcnt:
                    if int(cmd.split()[1]) > 0 and int(cmd.split()[1]) <= 9:
                        return True
        return False

    def addElements(field):
        newField = []
        newLine = []
        for i in range(len(field)):
            for elem in field[i]:
                newLine.append(elem)
                if len(newLine) == 9:
                    newField.append(newLine)
                    newLine = []
        for i in range(len(field)):
            for elem in field[i]:
                if elem != 0:
                    newLine.append(elem)
                    if len(newLine) == 9:
                        newField.append(newLine)
                        newLine = []
        if len(newLine) != 0:
            newField.append(newLine)
        return newField

    def calculateCnt(field):
        deskCnt = 0
        for i in range(len(field)):
            deskCnt += len(field[i])
        return deskCnt

    def checkAllVariations(field):
        ans = []
        deskCnt = calculateCnt(field)
        for i in range(deskCnt):
            if field[i // 9][i % 9] != 0:
                if i != deskCnt - 1:
                    m = i + 1
                    while m != (deskCnt - 1) and field[m // 9][m % 9] == 0:
                        m += 1
                    if field[m // 9][m % 9] != 0:
                        if field[m // 9][m % 9] == field[i // 9][i % 9] or (
                                field[m // 9][m % 9] + field[i // 9][i % 9]) == 10:
                            ans.append([(i // 9) + 1, (i % 9) + 1, (m // 9) + 1, (m % 9) + 1])
                if i != 0:
                    m = i - 1
                    while m != 0 and field[m // 9][m % 9] == 0:
                        m -= 1
                    if field[m // 9][m % 9] != 0:
                        if field[m // 9][m % 9] == field[i // 9][i % 9] or (
                                field[m // 9][m % 9] + field[i // 9][i % 9]) == 10:
                            ans.append([(i // 9) + 1, (i % 9) + 1, (m // 9) + 1, (m % 9) + 1])
                if i >= 9:
                    m = i - 9
                    while m >= 9 and field[m // 9][m % 9] == 0:
                        m -= 9
                    if field[m // 9][m % 9] != 0:
                        if field[m // 9][m % 9] == field[i // 9][i % 9] or (
                                field[m // 9][m % 9] + field[i // 9][i % 9]) == 10:
                            ans.append([(i // 9) + 1, (i % 9) + 1, (m // 9) + 1, (m % 9) + 1])
                if i <= (deskCnt - 10):
                    m = i + 9
                    while m <= (deskCnt - 10) and field[m // 9][m % 9] == 0:
                        m += 9
                    if field[m // 9][m % 9] != 0:
                        if field[m // 9][m % 9] == field[i // 9][i % 9] or (
                                field[m // 9][m % 9] + field[i // 9][i % 9]) == 10:
                            ans.append([(i // 9) + 1, (i % 9) + 1, (m // 9) + 1, (m % 9) + 1])

        return ans

    a = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 1, 2, 1, 3, 1, 4, 1], [5, 1, 6, 1, 7, 1, 8, 1, 9]]
    cmd = ""
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    u = 0
    print("------------------------------------------------------\n"
          "Добро пожаловать в игру 19\n"
          "Ты можешь соединять либо одинаковые цифры, либо цифры, дающие в сумме 10\n"
          "Соединять можно ближайщие по вертикали или горизонтали цифры\n"
          "Отсчёт координат начинается с левого верхнего угла\n"
          "Например 3 1 это число 5\n"
          "------------------------------------------------------\n"
          "Команды и их значение\n"
          "Add - добавить ряд оставщихся чисел\n"
          "Hint - подсказка\n"
          "Exit - завершить игру\n"
          "------------------------------------------------------")
    while cmd != "Exit" and len(a) != 0:
        # print(checkAllVariations(a))
        rowcnt = len(a)
        for i in range(rowcnt):
            print(a[i])
        columncnt = []
        for i in range(rowcnt):
            if len(a[i]) == 0:
                a.remove(a[i])
        rowcnt = len(a)
        for i in range(rowcnt):
            lcnt = 0
            for elem in a[i]:
                if elem != 0:
                    lcnt += 1
            columncnt.append(lcnt)
        print("Введите координаты первого числа или команду")
        cmd = input()
        if cmd == "Add":
            a = addElements(a)
        elif cmd == "Hint":
            hints = checkAllVariations(a)
            if len(hints) == 0:
                print("Возможных ходов нет, используйте команду Add")
            else:
                print(hints[0])
        else:
            if inputCheck(cmd):
                x1 = int(cmd[0])
                y1 = int(cmd[-1])
                print("Введите координаты второго числа")
                cmd = input()
                while inputCheck(cmd) == False:
                    print("Неверный Ввод Второго Числа")
                    cmd = input()
                    inputCheck(cmd)
                x2 = int(cmd[0])
                y2 = int(cmd[-1])
                if [x1, y1, x2, y2] in checkAllVariations(a):
                    a[x1 - 1][y1 - 1] = 0
                    a[x2 - 1][y2 - 1] = 0
            else:
                print("Неверный Ввод")
    print("Выберите следующую игру или напишите exit для выхода")
    return 0