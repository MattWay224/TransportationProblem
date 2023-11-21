from data.models import Matrix, Vector
from data.exceptions import Exceptions
from data.tabular import Tabular
from methods.north_west import NorthwestMethod
from methods.russel import RusselApproximation
from methods.vogel import VogelApproximation


def main():
    print("This program oriented to solve transportation problem. User may print matrix with any size\n")

    print("Enter a matrix for transportation problem with (m x n) size")
    A: Matrix = Matrix()
    A.mInput()

    print("Enter a Demand vector with (1 x n) size")
    D: Vector = Vector()
    D.vInput()

    print("Enter a Supply vector with (1 x m) size")
    S: Vector = Vector()
    S.vInput()

    """Check initial data for exceptions"""
    E: Exceptions(A, D, S)

    """Filling initial matrix and printing it"""
    print("Input table looks like: ")
    t = Tabular(A, D, S)
    t.create_table()
    t.print_table()

    print("Solving transportation problem using Northwest Cornel rule...")
    print("Solution table:")
    n = NorthwestMethod(A, D, S)
    print("Feasible solution for northwest method: " + str(n.nw_solve()) + "\n\n")

    print("Solving transportation problem using Russel's approximation method...")
    print("Solution table:")
    r = RusselApproximation(A, D, S)
    print("Feasible solution for Russel's approximation method: " + str(r.r_solve()) + "\n\n")

    print("Solving transportation problem using Vogel's approximation method...")
    print("Solution table:")
    v = VogelApproximation(A, D, S)
    print("Feasible solution for Vogel's approximation method: " + str(v.v_solve()) + "\n\n")


if __name__ == "__main__":
    main()
