class Division:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def divide(x, y):
        try:
            return (x / y)
        except:
            return (f"Невозможно произвести деление на ноль")


z = Division(36, 7)
print(Division.divide(0, 0))
print(Division.divide(84, 0))
print(z.divide(68, 3))