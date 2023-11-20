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

        # Sanity checks for correct input
        assert isinstance(a, Matrix), "A is not a matrix"
        assert isinstance(d, Vector), "Demand is not a vector"
        assert isinstance(s, Vector), "Supply is not a vector"
        assert a.getHeight() == s.getWidth(), "Length of supply vector does not correspond to # of rows of matrix A"
        assert a.getWidth() == d.getWidth(), "Length of demand vector does not correspond to # of cols of matrix A"
        assert all(x >= 0 for x in s.getVector()), "Supply vector should be non-negative"
        assert all(x >= 0 for x in d.getVector()), "Demand vector should be non-negative"

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
        suply = self.s.getVector().copy()
        demand = self.d.getVector().copy()
        value = 0

        while matrix.getHeight() != 0:
            col, col_penalty = self.__get_penalty(matrix)
            row, row_penalty = self.__get_penalty(matrix.mTranspose())
            if col_penalty > row_penalty:
                column = matrix.getColumn(col).getVector()
                row = column.index(min(column))
            else:
                line = matrix.getColumn(col).getVector()
                col = line.index(min(line))

            temp = min(suply[row], demand[col])
            suply[row] -= temp
            demand[col] -= temp
            value += temp * matrix.getMatrix()[row][col]
            if suply[row] != 0:
                matrix = matrix.removeCol(col)
                demand.pop(col)
            else:
                matrix = matrix.removeRow(row)
                suply.pop(row)

        return value
