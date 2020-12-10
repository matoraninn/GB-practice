close = "*"
confirm = 0
res = 0
while confirm != close:
    number = input(f"Введите числа или * для завершения: ")
    if close in number:
        numbers = number.replace(close, "")
        confirm = close

    num = [float(number) for number in number.split()]
    res += sum(num)
    print(f"Сумма равна: {res}")
