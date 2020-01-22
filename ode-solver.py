from matplotlib import pyplot as plt
from re import search

print("_" * 58)
print("{:<}".format("|"), "{:^54}".format("Решение обыкновенного дифференциального уравнения"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("третьего порядка методом Эйлера"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("ay'''(t) + by''(t) + cy'(t) + dy(t) = f(t)"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("y(0) = y\u2080, y'(0) = y'\u2080, y''(0) = y''\u2080"), "{:>}".format("|"))
print("_" * 58)

PATTERN = '\d*\.?\d+[Ee]?[+-]?\d*'


def input_lower_limit(lower_limit:str) -> float:
    if search(PATTERN, lower_limit):
        lower_limit = float(lower_limit)
    else:
        while not search(PATTERN, lower_limit):
            lower_limit = input("Значение должно быть числовым. Введите ещё раз: ")
        lower_limit = float(lower_limit)
    return lower_limit


def input_upper_limit(upper_limit:str) -> float:
    if search(PATTERN, upper_limit):
        upper_limit = float(upper_limit)
    else:
        while not search(PATTERN, upper_limit):
            upper_limit = input("Значение должно быть числовым. Введите ещё раз: ")
        upper_limit = float(LOWER_LIMIT)
    return upper_limit


LOWER_LIMIT = input_lower_limit(input("\nВведите нижний предел интегрирования: "))
UPPER_LIMIT = input_upper_limit(input("Введите верхний предел интегрирования: "))

while not UPPER_LIMIT > LOWER_LIMIT:
    try:
        raise ValueError
    except ValueError as error:
        UPPER_LIMIT = input_upper_limit(input("Число должно быть больше, чем нижний предел интегрирования. "
                                              "Введите ещё раз: "))

LIMIT_DIFF = UPPER_LIMIT - LOWER_LIMIT


def input_step(step:str) -> float:
    if search(PATTERN, step):
        step = float(step)
    else:
        while not search(PATTERN, step):
            step = input("Значение должно быть числовым. Введите ещё раз: ")
        step = float(step)
    return step


step = input_step(input("Введите шаг интегрирования: "))

while not 0 < step <= LIMIT_DIFF:
    try:
        raise ValueError
    except ValueError:
        step = input_step(input(f"Шаг интегрирования должен быть в интервале (0:{LIMIT_DIFF}]. Введите ещё раз: "))

step_count =  LIMIT_DIFF // step

x_0 = float(input("Введите значение y(0): "))
y_0 = float(input("Введите значение y'(0): "))
z_0 = float(input("Введите значение y''(0): "))
sol_x, sol_y, sol_z = [x_0], [y_0], [z_0]
t = [LOWER_LIMIT]
step_number = LOWER_LIMIT
i = 0


def diff_equation(y, y1, y2, t) -> float:
    return 1 / (2*t+2) - y - y1 - y2


def Euler(step_count, i, t, step_number, sol_x, sol_y, sol_z) -> float:
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
        print("В процессе вычисления возникла угроза деления на ноль!")
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