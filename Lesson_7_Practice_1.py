class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix
    def __str__(self):
        for row in self.my_matrix:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''
    def __add__(self, other):
        for i in range(len(self.my_matrix)):
            for j in range(len(other.my_matrix[i])):
                self.my_matrix[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix.__str__(self)


a = Matrix([[1, 3, 6], [-1, 8, 3], [6, 1, -6]])
b = Matrix([[-3, 8, 3], [-6, 8, 3], [6, 8, -6]])
print(a.__add__(b))