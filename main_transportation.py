from data.models import Matrix, Vector
from methods.north_west import NorthwestMethod
from methods.vogel import VogelMethod


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
    print(n.nw_solve())

    print("Solving transportation problem using Russel's approximation method...")
    """R: RusselMethod(A, D, S)"""

    print("Solving transportation problem using Vogel's approximation method...")
    v = VogelMethod(A, D, S)
    print(v.vogel_solve())


if __name__ == "__main__":
    main()