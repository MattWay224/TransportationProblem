from data.models import Matrix, Vector, IdentityMatrix
from dataclasses import dataclass


@dataclass
class Vogel:
    value: float


class VogelApproximation:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = a.hconcat(IdentityMatrix(a.getHeight()))
        self.a = a
        self.d = d
        self.s = s

    def __get_penalty(self, matrix: 'Matrix'):
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
            if supply[row] != 0:
                matrix = matrix.removeCol(col)
                demand.pop(col)
            else:
                matrix = matrix.removeRow(row)
                supply.pop(row)

        return value
