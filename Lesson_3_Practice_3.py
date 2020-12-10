x = float(input("Введите 1 аргумент: "))
y = float(input("Введите 2 аргумент: "))
z = float(input("Введите 3 аргумет: "))
def my_func():
    my_sum = [x, y, z]
    my_sum.remove(min(x, y, z))
    return my_sum
print(sum(my_func()))