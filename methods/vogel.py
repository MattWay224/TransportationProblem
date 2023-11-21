from data.models import Matrix, Vector, ZeroMatrix
from data.tabular import Tabular
from dataclasses import dataclass


@dataclass
class Vogel:
    """Stores a solution to simplex method.
            Args:
                answer (Matrix): Matrix of decision variables
                value (float): Solution to maximization problem
            """
    answer: Matrix
    value: float


class VogelApproximation:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = ZeroMatrix(a.getWidth(), a.getHeight())
        self.a = a
        self.d = d
        self.s = s

    @staticmethod
    def __get_penalty(matrix: 'Matrix'):
        return max(map(
            lambda x: (x[0], x[1][1 % len(x[1])] - x[1][0]),
            [(i, sorted(matrix.getColumn(i))) for i in range(matrix.getWidth())]
        ),
            key=lambda x: x[1])

    def v_solve(self):

        matrix = Matrix(self.a.getMatrix())
        supply = self.s.getVector().copy()
        demand = self.d.getVector().copy()
        value = 0

        while matrix.getHeight() != 0:
            col, col_penalty = self.__get_penalty(matrix)
            row, row_penalty = self.__get_penalty(matrix.mTranspose())
            if col_penalty > row_penalty:
                column = matrix.getColumn(col).getVector()
                row = column.index(min(column))
            else:
                line = matrix.mTranspose().getColumn(row).getVector()
                col = line.index(min(line))

            temp = min(supply[row], demand[col])
            supply[row] -= temp
            demand[col] -= temp
            value += temp * matrix.getMatrix()[row][col]
            self.answer[row][col] = temp ###

            if supply[row] != 0:
                matrix = matrix.removeCol(col)
                demand.pop(col)
            else:
                matrix = matrix.removeRow(row)
                supply.pop(row)

        self.tabular()

        return value

    """Function to create and print answer table"""
    def tabular(self):
        t = Tabular(self.answer, self.d, self.s)
        t.create_table()
        t.print_table()
