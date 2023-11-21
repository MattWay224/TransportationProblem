from data.models import Matrix, Vector, ZeroMatrix
from data.tabular import Tabular
from dataclasses import dataclass


@dataclass
class Russel:
    """Stores a solution to simplex method.
        Args:
            answer (Matrix): Matrix of decision variables
            value (float): Solution to maximization problem
        """
    answer: Matrix
    value: int


class RusselApproximation:
    a: Matrix
    d: Vector
    s: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):

        self.answer = ZeroMatrix(a.getWidth(), a.getHeight())
        self.delta = ZeroMatrix(a.getWidth(), a.getHeight())
        self.a = a
        self.d = d
        self.s = s

    @staticmethod
    def sum_v(vector: list):
        value = 0
        for i in range(len(vector)):
            value += vector[i]

        return value

    """Finds minimal delta in delta matrix"""
    def find_min_delta(self, delta: Matrix):
        coordinates = [-1] * 2
        min = self.sum_v(self.d.getVector()) + self.sum_v(self.d.getVector())  # Making a big number
        for i in range(0, delta.getHeight()):
            for j in range(0, delta.getWidth()):
                if delta[i][j] < min and delta:
                    min = delta.getMatrix()[i][j]
                    coordinates = [i, j]
        return coordinates

    """Creates delta matrix"""
    def create_delta(self, a: Matrix, max_in_rows, max_in_cols):
        for i in range(a.getHeight()):
            for j in range(0, a.getWidth()):
                if a[i][j] != 0 and max_in_rows[i] != 0 and max_in_cols[j] != 0:
                    self.delta[i][j] = a[i][j] - max_in_rows[i] - max_in_cols[j]
                else:
                    self.delta[i][j] = 0

    @staticmethod
    def eliminate_row(row, a: Matrix):
        for i in range(a.getWidth()):
            a[row][i] = 0

    @staticmethod
    def eliminate_column(col, a: Matrix):
        for i in range(a.getHeight()):
            a[i][col] = 0

    def r_solve(self):
        a = Matrix(self.a.getMatrix())
        d = self.d.getVector().copy()
        s = self.s.getVector().copy()
        value = 0

        while self.sum_v(s) != 0:
            max_in_rows = [max(row) for row in a]
            max_in_cols = [max(col) for col in zip(*a)]
            self.create_delta(a, max_in_rows, max_in_cols)

            min_delta_axes = self.find_min_delta(self.delta)
            if min_delta_axes == [-1, -1]:
                break

            min_value = min(s[min_delta_axes[0]], d[min_delta_axes[1]])
            if min_value == 0:
                if s[min_delta_axes[0]] == 0:
                    self.eliminate_row(min_delta_axes[0], a)
                if d[min_delta_axes[1]] == 0:
                    self.eliminate_column(min_delta_axes[1], a)

                continue

            else:
                value += a[min_delta_axes[0]][min_delta_axes[1]] * min_value
                self.answer[min_delta_axes[0]][min_delta_axes[1]] = min_value

                d[min_delta_axes[1]] -= min_value
                s[min_delta_axes[0]] -= min_value

                if s[min_delta_axes[0]] == 0:
                    self.eliminate_row(min_delta_axes[0], a)
                if d[min_delta_axes[1]] == 0:
                    self.eliminate_column(min_delta_axes[1], a)

        self.tabular()

        return value

    """Function to create and print answer table"""
    def tabular(self):
        t = Tabular(self.answer, self.d, self.s)
        t.create_table()
        t.print_table()
