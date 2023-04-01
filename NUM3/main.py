# Dominik Juszczyk
# Python 3.8
# Metody numeryczne, grupa nr 4
# Zadanie numeryczne NUM3

import unittest
import numpy as np
from lu import cal_y, calc_det


det = calc_det()
y = cal_y()

print('Wyznacznik: ', det)
print('y = ', y, '^T')


class TestNUM3(unittest.TestCase):

    def setUp(self):
        self.matrix = np.zeros((100, 100))
        for i in range(100):
            self.matrix[i][i] = 1.2
            if i != 0:
                self.matrix[i][i - 1] = 0.2
            if i != 99:
                self.matrix[i][i + 1] = 0.1 / (i + 1)
                if i != 98:
                    self.matrix[i][i + 2] = 0.4 / pow(i + 1, 2)
        self.x = [i+1 for i in range(100)]

    def test_det(self):
        self.assertAlmostEqual(np.linalg.det(self.matrix), det, 5)

    def test_y(self):
        for i in range(100):
            self.assertAlmostEqual(np.linalg.solve(self.matrix, self.x)[i], y[i])


if __name__ == '__main__':
    unittest.main()
