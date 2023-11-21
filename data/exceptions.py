from data.models import Matrix, Vector


class Exceptions:

    def __init__(self, a: Matrix, d: Vector, s: Vector):
        # Sanity checks for correct input
        assert isinstance(a, Matrix), "A is not a matrix"
        assert isinstance(d, Vector), "Demand is not a vector"
        assert isinstance(s, Vector), "Supply is not a vector"
        assert a.getHeight() == s.getWidth(), "Length of supply vector does not correspond to # of rows of matrix A"
        assert a.getWidth() == d.getWidth(), "Length of demand vector does not correspond to # of cols of matrix A"
        assert all(x >= 0 for x in s.getVector()), "Supply vector values should be positive"
        assert all(x >= 0 for x in d.getVector()), "Demand vector values should be positive"
        for i in range(a.getHeight()):
            assert all(x >= 0 for x in a.getMatrix()[i]), "Matrix values should be positive"
        assert d.sumV() >= s.sumV(), "Infeasible solution: supply vector cannot be bigger than demand vector"
