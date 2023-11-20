from data.models import Matrix, Vector, IdentityMatrix
from dataclasses import dataclass


@dataclass
class Russel:
    value: float


class RusselApproximation:
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
        self.delta = a.hconcat(IdentityMatrix(a.getHeight()))
        self.a = a
        self.d = d
        self.s = s

    def r_solve(self):
        a = self.a
        d = self.d
        s = self.s
        answer = self.answer
        value = 0

        max_in_rows = [-1] * a.getHeight()
        for i in range(a.getHeight()):
            max = -1
            for j in range(a.getWidth()):
                if a.getMatrix()[i][j] > max:
                    max = a.getMatrix()[i][j]
            max_in_rows[i] = max

        max_in_cols = [-1] * a.getWidth()
        for i in range(a.getWidth()):
            max = -1
            for j in range(a.getHeight()):
                if a.getMatrix()[j][i] > max:
                    max = a.getMatrix()[j][i]
            max_in_cols[i] = max

        for i in range(a.getHeight()):
            for j in range(0, a.getWidth()):
                self.delta.getMatrix()[i][j] = a.getMatrix()[i][j] - max_in_rows[i] - max_in_cols[j]

        while d.sumV() != 0 and s.sumV() != 0:
            min_delta_axes = self.find_min_delta(self.delta)
            min_value = min(s.getVector()[min_delta_axes[0]], d.getVector()[min_delta_axes[1]])
            if min_value == 0:
                self.delta[min_delta_axes[0]][min_delta_axes[1]] = 0
                continue
            else:
                value += a.getMatrix()[min_delta_axes[0]][min_delta_axes[1]] * min_value
                answer.getMatrix()[min_delta_axes[0]][min_delta_axes[1]] = min_value

                d.getVector()[min_delta_axes[0]] -= min_value
                s.getVector()[min_delta_axes[1]] -= min_value

                self.delta[min_delta_axes[0]][min_delta_axes[1]] = 0

        return value

    def find_min_delta(self, delta: Matrix):
        coordinates = [-1] * 2
        min = self.d.sumV() + self.s.sumV()  # Making a big number
        for i in range(0, delta.getHeight()):
            for j in range(0, delta.getHeight()):
                if delta.getMatrix()[i][j] < min:
                    min = delta.getMatrix()[i][j]
                    coordinates = [i, j]
        return coordinates
