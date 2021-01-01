class Error:
    def __init__(self, *args):
        self.my_list = []
    def my_input(self):
        while True:
            try:
                val = int(input("Введите данные дял заполнения списка: "))
                self.my_list.append(val)
                print(f"Список: {self.my_list} \n ")
            except:
                print(f"Введен недопустимое формат данных")
                stop = input(f"Породолжить? cont/stop ")

                if stop == "cont":
                    print(try_except.my_input())
                elif stop == "stop":
                    return f"THE END"
                else:
                    return f"THE END"


try_except = Error(1)
print(try_except.my_input())
