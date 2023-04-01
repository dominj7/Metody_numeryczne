# Rozwiazanie rownania Ay=b

N = 50
A1 = [7 for n in range(N - 1)]  # elementy nad diagonala
A2 = [9 for n in range(N)]      # diagonala
Aprim = [A1, A2]
b = [5 for n in range(N)]       # wektor b
u = [1 for n in range(N)]       # wektor u
v = u.copy()                    # wektor v


# backward substitution
def solve(vector):
    result = [vector[N - 1] / Aprim[1][N - 1]]
    for n in range(N - 2, -1, -1):
        element = (vector[n + 1] - Aprim[0][n] * result[N - n - 2]) / Aprim[1][n]
        result.append(element)
    result.reverse()
    return result


def mul(vector):
    result = 0
    for n in range(N):
        result += v[n] * vector[n]
    return result


z = solve(b)
q = solve(u)
frac = mul(z) / (mul(q) + 1)

y = list()
for n in range(N):
    y.append(z[n] - frac * q[n])
