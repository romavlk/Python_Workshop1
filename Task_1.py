# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

def getNumber(inputText):
    is_number = False
    while not is_number:
        try:
            number = int(input(f"{inputText}"))
            is_number = True
        except ValueError:
            print('Это НЕ ЧИСЛО!')
    return number


weekday = getNumber('Введите день недели (целое число от 1 до 7): ')
if (weekday == 6 or weekday == 7):
    print('Ура, это ВЫХОДНОЙ!')
elif (weekday >= 1 and weekday < 6):
    print('Это рабочий день недели')
else:
    print('Вы ввели неправильное число')