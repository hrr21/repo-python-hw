class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(i, end="  ")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
m_2 = Matrix([[31, 22], [37, 43], [51, 86]])

print(m_1.__add__(m_2))
