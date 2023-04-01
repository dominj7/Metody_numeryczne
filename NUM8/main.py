# Dominik Juszczyk
# Python 3.8
# Metody numeryczne, grupa nr 4
# Zadanie numeryczne NUM8

import unittest
from math import sin
from methods import simpson, romberg
from scipy.integrate import quad

print('\nFunkcja sin(x):')
print('\tSimpson: %.10f' % simpson(sin, 0, 1, 10 ** -10))
print('\tRomberg: %.10f' % romberg(sin, 0, 1, 10 ** -10))
print('\tquad: %.10f' % quad(sin, 0, 1)[0])


class TestNUM8(unittest.TestCase):

    def test_simpson(self):
            self.assertAlmostEqual(simpson(sin, 0, 1, 10 ** -10), quad(sin, 0, 1)[0], 10)

    def test_romberg(self):
        self.assertAlmostEqual(romberg(sin, 0, 1, 10 ** -10), quad(sin, 0, 1)[0], 10)


if __name__ == '__main__':
    unittest.main()
