from data.models import Matrix, Vector
from methods.north_west import NorthwestMethod
from methods.russel import RusselApproximation
from methods.vogel import VogelApproximation


def main():
    print("Enter a table for transportation problem")
    A: Matrix = Matrix()
    A.mInput()

    print("Enter a Demand vector")
    D: Vector = Vector()
    D.vInput()

    print("Enter a Supply vector")
    S: Vector = Vector()
    S.vInput()

    print("Solving transportation problem using Northwest Cornel rule...")
    n = NorthwestMethod(A, D, S)
    print("Feasible solution for northwest method: " + str(n.nw_solve()) + "\n")

    print("Solving transportation problem using Russel's approximation method...")
    r = RusselApproximation(A, D, S)
    print("Feasible solution for Russel's approximation method: " + str(r.r_solve()) + "\n")

    print("Solving transportation problem using Vogel's approximation method...")
    v = VogelApproximation(A, D, S)
    print("Feasible solution for Vogel's approximation method: " + str(v.v_solve()) + "\n")


if __name__ == "__main__":
    main()
