from game19 import game19
from guessNum import guessNum
from guessThousand import guessThousand

print("Добро прожаловать в GameHub в свободное время я буду стараться добавлять игры в которые можно играть в консоли\n"
      "Список игр ---------------------------------------------------------------------------------------------------\n"
      "1 - Игра 19 Количество игроков : 1 Время игры : 30 - 60 минут\n"
      "2 - Игра Больше/Меньше Количество игроков : 1 Время игры : около 1 минуты\n"
      "3 - Игра Угадай число Количество игроков : 1 Время игры: около 2 минут\n"
      "--------------------------------------------------------------------------------------------------------------\n"
      "Введите номер игры")
cmd = input()
while cmd != "exit":
    if cmd == "1":
        game19()
    elif cmd == "2":
        guessNum()
    elif cmd == "3":
        guessThousand()
    elif cmd != "exit":
        print("Неправильный ввод")
    cmd = input()