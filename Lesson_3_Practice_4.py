x = float(input("Введите действительное положительное число: "))
y = float(input("Введиет целое отрицательное число: "))
def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(x, y))