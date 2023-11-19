from simplex import Matrix, Vector
from methods import north_west


def main():
    print("Enter a table for transportation problem")
    A: Matrix = Matrix()
    A.mInput()

    print("Enter a Demand vector")
    D: Vector = Vector()
    D.mInput()

    print("Enter a Supply vector")
    S: Vector = Vector()
    S.mInput()

    print("Solving transportation problem using Northwest Cornel rule...")
    N: north_west.NorthwestMethod(A, D, S)

    print("Solving transportation problem using Russel's approximation method...")
    """R: russel_s_approximation.RusselMethod(A, D, S)"""

    print("Solving transportation problem using Vogel's approximation method...")
    """V: vogel_s_approximation.VogelMethod(A, D, S)"""


if __name__ == "__main__":
    main()