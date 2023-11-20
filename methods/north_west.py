from data.models import Matrix, Vector, IdentityMatrix
from dataclasses import dataclass


@dataclass
class Northwest:
    value: int


class NorthwestMethod:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = a.hconcat(IdentityMatrix(a.getHeight()))
        self.a = a
        self.d = d
        self.s = s

    def nw_solve(self):
        a = self.a
        d = self.d.getVector().copy()
        s = self.s.getVector().copy()
        answer = [[0] * a.getWidth() for _ in range(a.getHeight())]
        i = 0
        j = 0
        s_len = len(s)
        d_len = len(d)

        while i < s_len and j < d_len:
            minimal_value = min(d[j], s[i])
            answer[i][j] = minimal_value
            s[i] -= minimal_value
            i += (s[i] == 0)
            d[j] -= minimal_value
            j += (d[j] == 0)

        value = 0
        for i in range(0, a.getHeight()):
            for j in range(0, a.getWidth()):
                value += answer[i][j] * a[i][j]

        return value
