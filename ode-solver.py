from matplotlib import pyplot as plt
from colorama import Fore, Style
from sys import exit
from re import search

print(Fore.MAGENTA + "_" * 58)
print("{:<}".format("|"), "{:^54}".format("Решение обыкновенного дифференциального уравнения"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("третьего порядка методом Эйлера"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("ay'''(t) + by''(t) + cy'(t) + dy(t) = f(t)"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^55}".format("y(0) = y\u2080, y'(0) = y'\u2080, y''(0) = y''\u2080"), "{:>}".format("|"))
print("_" * 58)

LOWER_LIMIT = float(input(Style.NORMAL + "\nВведите нижний предел интегрирования: "))
UPPER_LIMIT = float(input("Введите верхний предел интегрирования: "))

while not UPPER_LIMIT > LOWER_LIMIT:
    try:
        raise ValueError
    except ValueError as error:
        print(Fore.RED + "Верхний предел интегрирования должен быть больше, чем нижний предел интегрирования")
        UPPER_LIMIT = float(input(Style.NORMAL + "Введите верхний предел интегрирования: "))

LIMIT_DIFF = UPPER_LIMIT - LOWER_LIMIT

step = float(input(Style.NORMAL + "Введите шаг интегрирования: "))

while not 0 < step <= LIMIT_DIFF:
    try:
        raise ValueError
    except ValueError:
        print(Fore.RED + f"Шаг интегрирования должен быть в интервале (0:{LIMIT_DIFF}]")
        step = float(input(Style.NORMAL + "Введите шаг интегрирования: "))

step_count =  LIMIT_DIFF // step

try:
    x_0 = float(input(Style.NORMAL + "Введите значение y(0): "))
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
t = [LOWER_LIMIT]
step_number = LOWER_LIMIT
i = 0


def diff_equation(y, y1, y2, t):
    return 1 / (2*t+2) - y - y1 - y2


def Euler(step_count, i, t, step_number, sol_x, sol_y, sol_z):
    try:
        while i < step_count:
            step_number += step
            t.append(step_number)
            sol_x.append(sol_x[i] + step * sol_y[i])
            sol_y.append(sol_y[i] + step * sol_z[i])
            sol_z.append(sol_z[i] + step * diff_equation(sol_x[i], sol_y[i], sol_z[i], t[i]))
            i += 1
            if i == step_count and step_number < UPPER_LIMIT:
                t.append(float(UPPER_LIMIT))
                sol_x.append(sol_x[i] + step * sol_y[i])
                sol_y.append(sol_y[i] + step * sol_z[i])
                sol_z.append(sol_z[i] + step * diff_equation(sol_x[i], sol_y[i], sol_z[i], t[i]))
    except ZeroDivisionError:
        print(Fore.RED + "В процессе вычисления возникла угроза деления на ноль!")
        exit(-1)
    return sol_x, sol_y, sol_z, t


Euler(step_count, i, t, step_number, sol_x, sol_y, sol_z)

print('\n{:<22}'.format("t"), '{:<22}'.format("y"), '{:<22}'.format("y'"), '{:<22}'.format("y''"))
print('_' * 90)

for line in range(len(t)):
    print('{:<22}'.format(t[line]),
          '{:<22}'.format(sol_x[line]), '{:<22}'.format(sol_y[line]), '{:<22}'.format(sol_z[line]))


plt.title('Графики функции y и её производных')
plt.plot(t, sol_x)
plt.plot(t, sol_y)
plt.plot(t, sol_z)
plt.legend(("y", "y'", "y''"))
plt.show()