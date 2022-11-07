import random


def new_game():
    global choose
    value = False
    while not value:
        print("Выберите вариант игры:", '\n',
              "1. С другим игроком", '\n',
              "2. С компьтером", '\n')
        try:
            choose = int(input())
            if choose == 1 or choose == 2:
                result_()
                value = True
            else:
                print("Вы сделали оишбку при выборе варианта игры!")
        except (TypeError, ValueError, IndexError):
            print("Вы ввели неверное значение!")
            continue
# функция выбора варианта игры


def hod_igroka():
    global logo
    global choose
    global a
    # переменные которые будем использовать при отработке функции из основного тела кода
    value = False
    while not value:
        hod = input('Введите номер строки, а затем номер столбца через пробел:')
        try:
            hod = list(map(int, hod.split()))
            i = hod[0] + 1
            j = hod[1] + 1
            value = True
        except (TypeError, ValueError, IndexError):
            print("Вы ввели неверное значение!"
    # цикл отрабатывает вводимые значения, при неправильном вводе обрабатыввается одна из ошибок
    if  (i and j) >= 1 and (i and j) <= 4:
        if logo[i][j] == '_':
            if a % 2 == 0:
                logo[i][j] = 'x'
                result_()
            elif choose == 1 and a % 2 != 0:
                logo[i][j] = 'o'
                result_()
        else:
            print('Данная ячейка уже занята, попробуйте еще раз!')
            povtor_igrok()
    else:
        print('Введены неверные значения, попробуйте еще раз!')
        povtor_igrok()
    # Условие ставит нужный нам символ в ячейку, либо возвращает в начало работы функции
# функция для запроса данных от пользователя и проверки на соответствие условиям задачи


def hod_computer():
    global logo
    i = random.randint(1, 3)
    j = random.randint(1, 3)
    if logo[i][j] == '_':
        logo[i][j] = 'o'
        result_()
    else:
        povtor_computer()
# функция для ответа компьютера (тут гораздо меньше проверок и условий)


def proverka():
    global a
    global choose
    for i in range(1, 4):
        if logo[i] == [i - 1, 'x', 'x', 'x']:
            print('Выиграл игрок 1!')
            a = 10
        elif logo[i] == [i - 1, 'o', 'o', 'o']:
            if choose == 2:
                print('Компьютер выиграл!')
            elif choose == 1:
                print("Выиграл игрок 2!")
            a = 10
        elif logo[1][i] == 'x' and logo[2][i] == 'x' and logo[3][i] == 'x':
            print('Выиграл игрок 1!')
            a = 10
        elif logo[1][i] == 'o' and logo[2][i] == 'o' and logo[3][i] == 'o':
            if choose == 2:
                print('Компьютер выиграл!')
            elif choose == 1:
                print("Выиграл игрок 2!")
            a = 10
    if logo[1][1] == 'x' and logo[2][2] == 'x' and logo[3][3] == 'x':
        print('Выиграл игрок 1!')
        a = 10
    elif logo[1][3] == 'x' and logo[2][2] == 'x' and logo[3][1] == 'x':
        print('Выиграл игрок 1!')
        a = 10
    elif logo[1][1] == 'o' and logo[2][2] == 'o' and logo[3][3] == 'o':
        if choose == 2:
            print('Компьютер выиграл!')
        elif choose == 1:
            print("Выиграл игрок 2!")
        a = 10
    elif logo[1][3] == 'o' and logo[2][2] == 'o' and logo[3][1] == 'o':
        if choose == 2:
            print('Компьютер выиграл!')
        elif choose == 1:
            print("Выиграл игрок 2!")
        a = 10
# функция проверки выигрыша (проверка проводится по критериям в зависимости от того, что выбрал пользователь)


def povtor_igrok():
    hod_igroka()
# функция используется для повторного использования при неверном вводе данных


def povtor_computer():
    hod_computer()
# функция для правильной отработки выбора компьютера


def result_():
    global logo
    for i in range(0, 4):
        print(*logo[i], end='\n')
# печать нашей таблицы (начальной и измененной в дальнейшем)


choose = 0
# переменная заводится для отработки выбора пользователя и используется в функциях:
# выбор варианта игры; проверки выигрыша, и запрос данных для выполнения хода
a = 0
# переменная заводится для отработки подсчета общего количества ходов
logo = [
    [" ", 0, 1, 2],
    [0, '_', '_', '_'],
    [1, '_', '_', '_'],
    [2, '_', '_', '_']
]
# создаем таблицу для игры
new_game()

while a < 9:
    hod_igroka()
    a += 1
    proverka()
    if a == 9 or a == 10:
        break
    if choose == 1:
        hod_igroka()
    elif choose == 2:
        hod_computer()
    a += 1
    proverka()
# цикл отрабатывает заполнение всего поля игры, либо прерывается при выигрыше кого-либо
if a == 9:
    print('Ничья')
# условие верно при заполнении всего поля игры
print('конец игры')
