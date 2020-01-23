from matplotlib import pyplot as plt
from re import search
from sys import exit

print("_" * 58)
print("{:<}".format("|"), "{:^54}".format("Решение обыкновенного дифференциального уравнения"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("третьего порядка методом Эйлера"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("ay'''(t) + by''(t) + cy'(t) + dy(t) = f(t)"), "{:>}".format("|"))
print("{:<}".format("|"), "{:^54}".format("y(0) = y\u2080, y'(0) = y'\u2080, y''(0) = y''\u2080"), "{:>}".format("|"))
print("_" * 58)

PATTERN = '\d*\.?\d+[Ee]?[+-]?\d*'


def input_var(var:str) -> float:
    if search(PATTERN, var):
        var = float(var)
    else:
        while not search(PATTERN, var):
            var = input("Значение должно быть числовым. Введите ещё раз: ")
        var = float(var)
    return var


LOWER_LIMIT = input_var(input("\nВведите нижний предел интегрирования: "))
UPPER_LIMIT = input_var(input("Введите верхний предел интегрирования: "))

while not UPPER_LIMIT > LOWER_LIMIT:
    UPPER_LIMIT = input_var(input("Число должно быть больше, чем нижний предел интегрирования. Введите ещё раз: "))
LIMIT_DIFF = UPPER_LIMIT - LOWER_LIMIT

step = input_var(input("Введите шаг интегрирования: "))
while not 0 < step <= LIMIT_DIFF:
    step = input_var(input(f"Число должно быть в интервале: {0, LIMIT_DIFF}. Введите ещё раз: "))

step_count =  LIMIT_DIFF // step
x_0 = input_var(input("Введите значение y(0): "))
y_0 = input_var(input("Введите значение y'(0): "))
z_0 = input_var(input("Введите значение y''(0): "))
sol_x, sol_y, sol_z = [x_0], [y_0], [z_0]
t = [LOWER_LIMIT]
step_number = LOWER_LIMIT
i = 0


def diff_equation(y:float, y1:float, y2:float, t:float) -> float:
    return 1 / (2*t+2) - y - y1 - y2

def Euler(step:float, step_count:int, i:float, step_number:float, t:list, sol_x:list, sol_y:list, sol_z:list):
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


Euler(step, step_count, i, step_number, t, sol_x, sol_y, sol_z)

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