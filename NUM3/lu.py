
N = 100
a, b, c, d = list(), list(), list(), list()
for i in range(N):
    c.append(1.2)
    if i != 99:
        b.append(0.1 / (i + 1))
        d.append(0.2)
        if i != 98:
            a.append(0.4 / pow((i + 1), 2))
A = [a, b, c, d]


# LU
for i in range(N):
    if i != 0:
        if i != 99:
            A[1][i] -= (A[3][i-1] * A[0][i-1])
        A[2][i] -= (A[3][i-1] * A[1][i-1])
    if i != 99:
        A[3][i] /= A[2][i]


# Vector x
x = [i+1 for i in range(N)]


def calc_det():
    my_det = 1
    for i in range(N):
        my_det *= A[2][i]
    return my_det


def cal_y():
	# forward substitution
    v = list()
    v.append(x[0])
    for i in range(1, N):
        element = x[i] - (A[3][i - 1] * v[i - 1])
        v.append(element)

	# back substitution
    y = list()
    y.append(v[99] / A[2][99])
    y.append((v[98] - A[1][98] * y[0]) / A[2][98])
    for i in range(97, -1, -1):
        element = (v[i] - A[1][i] * y[98 - i] - A[0][i] * y[97 - i]) / A[2][i]
        y.append(element)

    y.reverse()
    return y
