from data.models import Matrix, Vector


class Exceptions:

    def __init__(self, a: Matrix, d: Vector, s: Vector):
        # Sanity checks for correct input
        assert isinstance(a, Matrix), "A is not a matrix"
        assert isinstance(d, Vector), "Demand is not a vector"
        assert isinstance(s, Vector), "Supply is not a vector"
        assert a.getHeight() == s.getWidth(), "Length of supply vector does not correspond to # of rows of matrix A"
        assert a.getWidth() == d.getWidth(), "Length of demand vector does not correspond to # of cols of matrix A"
        assert all(x >= 0 for x in s.getVector()), "Supply vector should be non-negative"
        assert all(x >= 0 for x in d.getVector()), "Demand vector should be non-negative"
