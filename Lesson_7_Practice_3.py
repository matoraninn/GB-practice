class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return self.quantity + other.quantity
    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return sub if sub > 0 else "Ошибка"
    def __truediv__(self, other):
        return self.quantity // other.quantity
    def __mul__(self, other):
        return self.quantity * other.quantity
    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_a = Cell(36)
cell_b = Cell(68)
print(cell_a + cell_b)
print(cell_a - cell_b)
print(cell_a / cell_b)
print(cell_a * cell_b)
print(cell_a.make_order(8))