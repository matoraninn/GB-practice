def my_div(*args):
    try:
        n1 = float(input("Введите делимое: "))
        n2 = float(input("Введите делитель: "))
        div_res = n1 / n2
    except ValueError:
        return 'Неверное значение'
    except ZeroDivisionError:
        return "Ошибка. Нельзя разделить на 0"

    return div_res
print(f'Результат — {my_div()}')