#1
def distance(x1=0, y1=0, x2=0, y2=0):
    line = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return line

x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))


res = distance(x2 = x2, y2 = y2, x1 = x1, y1 = y1)
print(res)
#2
def power(a, n):

    num = 1

    for i in range(abs(n)):
        num *= a
    if n >= 0:
        return num
    else:
        return 1 / num

print(power(float(input('Введите число: ')), int(input('Введите степень: '))))
#3
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input('Введите число: '))))
#4
def is_year_leap():
    y = int(input('Введите год: '))
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return 'TRUE'
    else:
        return ('FALSE')

print(is_year_leap())
#5
import math

def square(a):
    P = a * a * a * a
    print('Периметр квадрата', P)
    S = a * a
    print('Площадь квадрата', S)
    B = a * math.sqrt(2)
    print('Диагональ квадрата', B)


print(square(int(input('Введите сторону квадрата: '))))
#6
def season(a):
    if a > 12:
        print('Месяцы от 1 до 12')
    else:
        if a >= 3 and a <= 5:
            print('С 3 по 5 месяц Весна')
        elif a >= 6 and a <= 8:
            print('С 6 по 8 месяц лето')
        elif a >= 9 and a <= 11:
            print('С 9 по 11 месяц осень')
        else:
            print('С 12 по 2 месяц зима')


print(season(int(input('Введите номер месяца: '))))
#7
def credit(a, y):
    sum = a
    for i in range(y):
        sum = sum + (sum * 0.1)
    return sum

a = int(input("Введите сумму вклада: "))
y = int(input("Введите срок вклада в годах: "))

print("Сумма на счету пользователя через", y, "лет:", credit(a, y), "рублей")
#8
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input('Введите число от 0 до 1000: '))
sum = is_prime(num)

if sum:
    print(num, ' простое число')
else:
    print(num, 'не простое число')
#9
def date(day, month, year):
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
            elif day > 28:
                return False
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30:
                    return False
            else:
                if day > 31:
                    return False
    return True

day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))

if date(day, month, year):
    print('Введенная дата является действительной')
else:
    print('Введенная дата не является действительной')
