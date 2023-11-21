import unittest
from data.models import Matrix, Vector
from methods.north_west import NorthwestMethod
from methods.russel import RusselApproximation
from methods.vogel import VogelApproximation


class Test(unittest.TestCase):
    # test from lab
    def test_0(self):
        A = Matrix(
            [
                [7, 8, 1, 2],
                [4, 5, 9, 8],
                [9, 2, 3, 6],
            ]
        )
        d = Vector([120, 50, 190, 110])
        s = Vector([160, 140, 170])

        northwest = NorthwestMethod(A, d, s)
        russel = RusselApproximation(A, d, s)
        vogel = VogelApproximation(A, d, s)

        nw_solution = northwest.nw_solve()
        russel_solution = russel.r_solve()
        vogel_solution = vogel.v_solve()

        self.assertEqual(nw_solution, 3220)
        self.assertEqual(russel_solution, 1530)
        self.assertEqual(vogel_solution, 1330)

    def test_1(self):
        A = Matrix(
            [
                [7, 6, 3, 5],
                [1, 8, 4, 2],
                [9, 2, 7, 1],
            ]
        )
        d = Vector([60, 100, 120, 80])
        s = Vector([110, 170, 80])

        northwest = NorthwestMethod(A, d, s)
        russel = RusselApproximation(A, d, s)
        vogel = VogelApproximation(A, d, s)

        nw_solution = northwest.nw_solve()
        russel_solution = russel.r_solve()
        vogel_solution = vogel.v_solve()

        self.assertEqual(nw_solution, 1680)
        self.assertEqual(russel_solution, 890)
        self.assertEqual(vogel_solution, 890)

    def test_2(self):
        A = Matrix(
            [
                [5, 9, 4, 1],
                [2, 3, 7, 6],
                [4, 2, 8, 1],
            ]
        )
        d = Vector([70, 150, 180, 120])
        s = Vector([220, 160, 140])

        northwest = NorthwestMethod(A, d, s)
        russel = RusselApproximation(A, d, s)
        vogel = VogelApproximation(A, d, s)

        nw_solution = northwest.nw_solve()
        russel_solution = russel.r_solve()
        vogel_solution = vogel.v_solve()

        self.assertEqual(nw_solution, 3100)
        self.assertEqual(russel_solution, 1530)
        self.assertEqual(vogel_solution, 1530)

    def test_3(self):
        A = Matrix(
            [
                [4, 3, 7, 9],
                [5, 7, 6, 4],
                [7, 1, 1, 8],
            ]
        )
        d = Vector([220, 160, 190, 310])
        s = Vector([280, 400, 200])

        northwest = NorthwestMethod(A, d, s)
        russel = RusselApproximation(A, d, s)
        vogel = VogelApproximation(A, d, s)

        nw_solution = northwest.nw_solve()
        russel_solution = russel.r_solve()
        vogel_solution = vogel.v_solve()

        self.assertEqual(nw_solution, 4940)
        self.assertEqual(russel_solution, 3180)#may be not corr
        self.assertEqual(vogel_solution, 2860)#may be not corr

    # extra test 5x3
    def test_4(self):
        A = Matrix(
            [
                [2, 3, 4, 2, 4],
                [8, 4, 1, 4, 1],
                [9, 7, 3, 7, 2],
            ]
        )
        d = Vector([60, 70, 120, 130, 100])
        s = Vector([140, 180, 160])

        northwest = NorthwestMethod(A, d, s)
        russel = RusselApproximation(A, d, s)
        vogel = VogelApproximation(A, d, s)

        nw_solution = northwest.nw_solve()
        russel_solution = russel.r_solve()
        vogel_solution = vogel.v_solve()

        self.assertEqual(nw_solution, 1380)
        # self.assertEqual(russel_solution, 0) #not
        self.assertEqual(vogel_solution, 1260)


