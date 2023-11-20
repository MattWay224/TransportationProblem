from data.models import Matrix, Vector, IdentityMatrix
from dataclasses import dataclass


@dataclass
class Northwest:
    value: float


class NorthwestMethod:
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

    def nw_solve(self):
        a = self.a
        d = self.d.getVector().copy()
        s = self.s.getVector().copy()
        answer = self.answer

        i = 0
        j = 0

        while i < len(s) and j < len(d):
            if d[j] > s[i]:
                answer.getMatrix()[i][j] = s[i]

                d[j] -= s[i]
                s[i] = 0

                i += 1
            elif d[j] < s[i]:
                answer.getMatrix()[i][j] = d[j]

                s[i] -= d[j]
                d[j] = 0

                j += 1
            else:
                answer.getMatrix()[i][j] = s[i]

                d[j] = 0
                s[i] = 0

                i += 1
                j += 1

        value = 0
        for i in range(0, a.getHeight()):
            for j in range(0, a.getWidth()):
                if answer.getMatrix()[i][j] is None:
                    continue

                value += answer.getMatrix()[i][j] * a.getMatrix()[i][j]

        return value
