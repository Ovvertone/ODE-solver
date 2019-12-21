# расписать всё в классах
from matplotlib import pyplot as plt
from colorama import Fore, Style
from sys import exit


LOWER_LIMIT = 0
UPPER_LIMIT = 10
STEP_MAX = 1

print(Fore.MAGENTA + "_" * 58)
print("{:<}".format("|"), "{:^54}".format("Решение обыкновенного дифференциального уравнения"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("третьего порядка методом Эйлера"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("ay'''(t) + by''(t) + cy'(t) + dy(t) = f(t)"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^55}".format("y(0) = y\u2080, y'(0) = y'\u2080, y''(0) = y''\u2080"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("t \u220A [0;10]"), "{:>}".format("|"))
print("_" * 58)
a = 1

class IntegrationStepError(Exception):  # заменить на built-in exception мб

    def __init__(self, msg):
        self.msg = Fore.RED + msg


step = float(input(Style.NORMAL + "\nВведите шаг интегрирования: ")) # решить проблему с точностью

while not LOWER_LIMIT < step <= STEP_MAX:  # закончить с проверкой ТИПА!!!!!!!!!!!
    try:
        raise IntegrationStepError("IntegrationStepError: integration step should be in the range (0:1]"
                                   "\nВведите корректное значение")
    except IntegrationStepError as error:
        print(error.msg)
        step = float(input(Style.NORMAL + "Введите шаг интегрирования: "))

step_count =  UPPER_LIMIT // step

try:
    x_0 = float(input("Введите значение y(0): "))
    if type(x_0) == str:
        raise ValueError
except ValueError:
    print(Fore.RED + "Введите числовое значение")
    exit(-1)

try:
    y_0 = float(input(Style.NORMAL + "Введите значение y'(0): "))
    if type(y_0) == str:
        raise ValueError
except ValueError:
    print(Fore.RED + "Введите числовое значение")
    exit(-1)

try:
    z_0 = float(input( Style.NORMAL + "Введите значение y''(0): "))
    if type(z_0) == str:
        raise ValueError
except ValueError:
    print(Fore.RED + "Введите числовое значение")
    exit(-1)

sol_x, sol_y, sol_z = [x_0], [y_0], [z_0]
t = [0]
step_number = 0
i = 0


def diff_equation(y, y1, y2, t):  # обобщить ф-ию к любому виду
    return 1 / (2*t+2) - y - y1 - y2


print('\n{:<22}'.format("t"), '{:<22}'.format("y"), '{:<22}'.format("y'"), '{:<22}'.format("y''"))
print('_' * 90)


def Euler(step_count, i, t, step_number, sol_x, sol_y, sol_z):  # создать общую ф-ию с данной в кач-ве шага
    while i < step_count:                                          # которая на вход получает ф-ию общего диффура
        step_number += step
        i += 1
        t.append(step_number)
        sol_x.append(sol_x[i - 1] + step * sol_y[i-1])
        sol_y.append(sol_y[i - 1] + step * sol_z[i-1])
        sol_z.append(sol_z[i - 1] + step * diff_equation(sol_x[i - 1], sol_y[i - 1], sol_z[i - 1], t[i - 1]))
        if i == step_count and step_number < UPPER_LIMIT:
            t.append(float(UPPER_LIMIT))
            sol_x.append(sol_x[i] + step * sol_y[i])
            sol_y.append(sol_y[i] + step * sol_z[i])
            sol_z.append(sol_z[i] + step * diff_equation(sol_x[i], sol_y[i], sol_z[i], t[i]))
    return sol_x, sol_y, sol_z, t


Euler(step_count, i, t, step_number, sol_x, sol_y, sol_z)

for line in range(len(t)):
    print('{:<22}'.format(t[line]),
          '{:<22}'.format(sol_x[line]), '{:<22}'.format(sol_y[line]), '{:<22}'.format(sol_z[line]))


plt.title('Графики функции y и её производных')

plt.plot(t, sol_x)
plt.plot(t, sol_y)
plt.plot(t, sol_z)

plt.legend(("y", "y'", "y''"))

plt.show()
