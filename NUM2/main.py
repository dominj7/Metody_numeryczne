# Dominik Juszczyk
# Python 3.8
# Metody numeryczne, grupa nr 4
# Zadanie numeryczne NUM2

import numpy as np

A1 = np.array([[2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553],
               [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556],
               [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749],
               [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493],
               [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926]])

A2 = np.array([[2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473],
               [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589],
               [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923],
               [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124],
               [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678]])


b = np.array([5.40780228, 3.67008677, 3.12306266, -1.11187948, 0.54437218])
bprim = b.copy()
bprim[0] += 0.00001


y1 = np.linalg.solve(A1, b)
y1prim = np.linalg.solve(A1, bprim)

y2 = np.linalg.solve(A2, b)
y2prim = np.linalg.solve(A2, bprim)

delta1 = np.linalg.norm(y1 - y1prim)
delta2 = np.linalg.norm(y2 - y2prim)

kappa1 = np.linalg.cond(A1)
kappa2 = np.linalg.cond(A2)


print('y1 =  {}^T'.format(y1))
print('y1\' = {}^T\n'.format(y1prim))
print('y2 =  {}^T'.format(y2))
print('y2\' = {}^T\n'.format(y2prim))
print('delta1 = ', delta1)
print('delta2 = ', delta2)
print('\nkappa1 = ', kappa1)
print('kappa2 = ', kappa2)
