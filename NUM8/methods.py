
def simpson(function, a, b, e):
    h = (b - a) / 2
    I = function(a) + function(b)
    I += 4 * function((a + b) / 2)
    I *= h / 3

    error = e
    while error >= e:
        Iprev = I
        h /= 2
        xi = a + h
        # first_sum = f_1 + f_3 + ... + f_(n-1)
        first_sum = 0
        while xi < b:
            first_sum += function(xi)
            xi += 2 * h
        xi = a + 2 * h
        # second_sum = f_2 + f_4 + ... + f_(n-2)
        second_sum = 0
        while xi < b:
            second_sum += function(xi)
            xi += 2 * h
        I = (h / 3) * (function(a) + 4 * first_sum + 2 * second_sum + function(b))
        error = abs(I - Iprev)

    return I


def romberg(function, a, b, e):
    h = b - a
    # R - aktualny wiersz
    R = [(h / 2) * (function(a) + function(b))]
    n, m = 1, 1
    error = e

    while error >= e:
        n += 1
        m *= 2
        h /= 2
        # Rprev - poprzedni wiersz
        Rprev = R

        suma = sum([function(a + h * i) for i in range(1, m, 2)])
        R = [0.0] * n
        R[0] = Rprev[0] / 2 + h * suma  # R(n-1, 0)
        pow4 = 4

        for i in range(1, n):
            R[i] = R[i - 1] + (R[i - 1] - Rprev[i - 1]) / (pow4 - 1)    # reszta elementów wiersza
            pow4 *= 4

        error = abs(R[-1] - Rprev[-1])  # |R(n-1, n-1) - R(n-2, n-2)|

    return R[-1]
