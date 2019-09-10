import random


class Matrix:
    roundTo = 12

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for i in range(rows)]

    def __getitem__(self, keys):
        i, j = keys
        return self.data[i][j]

    def __setitem__(self, keys, value):
        i, j = keys
        self.data[i][j] = value

    def map(self, fnc):
        for i in range(self.rows):
            for j in range(self.cols):
                self[i, j] = fnc(self[i, j])
        return self

    def __pow__(self, power, modulo=None):
        result = Matrix(self.rows, self.cols)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                result[i, j] = self[i, j]**2
        return result

    @staticmethod
    def transpose(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result[j, i] = matrix[i, j]
        return result

    @staticmethod
    def from_array(arr):
        length = len(arr)
        result = Matrix(length, 1)
        for i in range(0, length):
            result[i, 0] = arr[i]
        return result

    @staticmethod
    def elmult(m1, m2):
        if m1.rows != m2.rows or m1.cols != m2.cols :
            print("cols or rows don't match")
            return
        result = Matrix(m1.rows, m1.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                result[i, j] = m1[i, j] * m2[i, j]
        return result

    def randomize(self, start: int, end: int):
        for i in range(self.rows):
            for j in range(self.cols):
                randNum = random.uniform(start, end)
                self[i, j] = round(randNum, self.roundTo)
        return self

    def __str__(self):
        result = ""
        for i in range(0, self.rows):
            row = ""
            for j in range(0, self.cols):
                row += (str(self[i, j]) + "  ")
            result += row.center(20)
            result += "\n"
        return result

    def __add__(self, number):
        result = Matrix(self.rows, self.cols)
        if isinstance(number, Matrix):

            if self.rows != number.rows or self.cols != number.cols:
                print("Rows or Cols don't match in matrices")
                return
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + number[i, j]
        elif isinstance(number, int):
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] + number
        else:
            result = None

        return result

    def __sub__(self, number):
        result = Matrix(self.rows, self.cols)
        if isinstance(number, Matrix):

            if self.rows != number.rows or self.cols != number.cols:
                print("Rows or Cols don't match in matrices")
                return
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - number[i, j]
        elif isinstance(number, int):
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] - number
        else:
            result = None

        return result


    def __mul__(self, number):
        if isinstance(number, float):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self[i, j] * number
            return result
        elif isinstance(number, Matrix):
            if self.cols != number.rows:
                print("Number of cols in first matrix do not match the number of rows in second")
            else:
                result = Matrix(self.rows, number.cols)
                for i in range(self.rows):
                    for j in range(number.cols):
                        sum = 0
                        for k in range(self.cols):
                            sum += self[i, k] * number[k, j]
                        result[i, j] = round(sum, self.roundTo)
                return result

