from prettytable import PrettyTable
from data.models import Matrix, Vector


class Tabular:
    matrix: Matrix
    demand: Vector
    supply: Vector

    def __init__(self, a: Matrix, d: Vector, s: Vector):
        self.matrix = Matrix(a.getMatrix())
        self.demand = Vector(d.getVector())
        self.supply = Vector(s.getVector())
        self.table = None

    def create_table(self):
        """Creating first row of the table"""
        cols = ["col " + str(i + 1) for i in range(self.matrix.getWidth())]

        first_row = []
        first_row.append("*")
        first_row += cols
        first_row.append("Supply")

        self.table = PrettyTable(first_row)

        """Creating main rows of the table"""
        for i in range(self.matrix.getHeight()):
            rows = [str(self.matrix[i][j]) for j in range(self.matrix.getWidth())]

            row = []
            row.append("row " + str(i + 1))
            row += rows
            row.append(self.supply[i])

            self.table.add_row(row)

        final = [str(self.demand[i]) for i in range(self.matrix.getWidth())]

        """Creating last row of the table"""
        final_row = []
        final_row.append("Demand")
        final_row += final
        final_row.append("*")

        self.table.add_row(final_row)

    def print_table(self):
        print(self.table)
        print()
