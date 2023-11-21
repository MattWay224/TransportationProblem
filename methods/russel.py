from data.models import Matrix, Vector, IdentityMatrix, ZeroMatrix
from data.tabular import Tabular
from dataclasses import dataclass


@dataclass
class Russel:
    value: int


class RusselApproximation:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = ZeroMatrix(a.getWidth(), a.getHeight())
        identity = IdentityMatrix(a.getHeight())
        self.delta = a.hconcat(identity)
        self.a = a
        self.d = d
        self.s = s

    @staticmethod
    def sum_v(vector: list):
        value = 0
        for i in range(len(vector)):
            value += vector[i]

        return value

    def find_min_delta(self, delta: Matrix):
        coordinates = [-1] * 2
        min = self.sum_v(self.d.getVector()) + self.sum_v(self.d.getVector())  # Making a big number
        for i in range(0, delta.getHeight()):
            for j in range(0, delta.getWidth()):
                if delta[i][j] < min:
                    min = delta.getMatrix()[i][j]
                    coordinates = [i, j]
        return coordinates

    def r_solve(self):
        a = self.a
        d = self.d.getVector().copy()
        s = self.s.getVector().copy()
        value = 0

        max_in_rows = [max(row) for row in zip(*a)]

        max_in_cols = [max(col) for col in zip(*a)]

        for i in range(a.getHeight()):
            for j in range(0, a.getWidth()):
                self.delta[i][j] = a[i][j] - max_in_rows[i] - max_in_cols[j]

        while self.sum_v(d) != 0 and self.sum_v(s) != 0:
            min_delta_axes = self.find_min_delta(self.delta)
            if min_delta_axes == [-1, -1]:
                break
            min_value = min(s[min_delta_axes[0]], d[min_delta_axes[1]])
            if min_value == 0:
                self.delta[min_delta_axes[0]][min_delta_axes[1]] = 0
                continue
            else:
                value += a[min_delta_axes[0]][min_delta_axes[1]] * min_value
                self.answer[min_delta_axes[0]][min_delta_axes[1]] = min_value

                d[min_delta_axes[1]] -= min_value
                s[min_delta_axes[0]] -= min_value

                self.delta[min_delta_axes[0]][min_delta_axes[1]] = 0

        self.tabular()

        return value

    def tabular(self):
        t = Tabular(self.answer, self.d, self.s)
        t.create_table()
        t.print_table()
