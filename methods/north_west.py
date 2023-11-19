from data.models import Matrix, Vector, IdentityMatrix
from dataclasses import dataclass


@dataclass
class Northwest:
    value: float


class NorthwestMethod:
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

    def nw_solve(self):
        a = self.a
        d = self.d
        s = self.s
        answer = self.answer

        i = 0
        j = 0

        while i < s.getHeight() and j < d.getHeight():
            if d.getVector()[j] > s.getVector()[i]:
                answer.getMatrix()[i][j] = s.getVector()[i]

                d.getVector()[j] -= s.getVector()[i]
                s.getVector()[i] = 0

                i += 1
            elif d.getVector()[j] < s.getVector()[i]:
                answer.getMatrix()[i][j] = d.getVector()[j]

                s.getVector()[i] -= d.getVector()[j]
                d.getVector()[j] = 0

                j += 1
            else:
                answer.getMatrix()[i][j] = s.getVector()[i]

                d.getVector()[i] = 0
                s.getVector()[j] = 0

                i += 1
                j += 1

        value = 0
        for i in range(0, a.getHeight()):
            for j in range(0, a.getWidth()):
                if answer.getMatrix()[i][j] is None:
                    continue

                value += answer.getMatrix()[i][j] * a.getMatrix()[i][j]

        return value
