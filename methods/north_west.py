from data.models import Matrix, Vector, ZeroMatrix
from data.tabular import Tabular
from dataclasses import dataclass


@dataclass
class Northwest:
    """Stores a solution to simplex method.
            Args:
                answer (Matrix): Matrix of decision variables
                value (float): Solution to maximization problem
            """
    answer: Matrix
    value: int


class NorthwestMethod:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = ZeroMatrix(a.getWidth(), a.getHeight())
        self.a = a
        self.d = d
        self.s = s

    def nw_solve(self):
        a = self.a
        d = self.d.getVector().copy()
        s = self.s.getVector().copy()
        i = 0
        j = 0
        s_len = len(s)
        d_len = len(d)

        while i < s_len and j < d_len:
            minimal_value = min(d[j], s[i])
            self.answer[i][j] = minimal_value

            s[i] -= minimal_value
            d[j] -= minimal_value

            i += (s[i] == 0)
            j += (d[j] == 0)

        """Calculating feasible solution value"""
        value = 0
        for i in range(0, a.getHeight()):
            for j in range(0, a.getWidth()):
                value += self.answer[i][j] * a[i][j]

        self.tabular()

        return value

    """Function to create and print answer table"""
    def tabular(self):
        t = Tabular(self.answer, self.d, self.s)
        t.create_table()
        t.print_table()
