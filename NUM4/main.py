# Dominik Juszczyk
# Python 3.8
# Metody numeryczne, grupa nr 4
# Zadanie numeryczne NUM4

import unittest
import numpy as np
from sol import N, y

print('y = ', y, '^T')


def np_solution():
    A = np.ones((N, N))
    b = np.ones(N)
    b.fill(5)
    for n in range(N):
        A[n][n] = 10
        if n != (N - 1):
            A[n][n + 1] = 8
    result = np.linalg.solve(A, b)
    return result.tolist()


class TestNUM4(unittest.TestCase):

    def test_result(self):
        np_y = np_solution()
        for n in range(N):
            self.assertAlmostEqual(y[n], np_y[n])


if __name__ == '__main__':
    unittest.main()
