import numpy as np

a = np.array([1, 2, 3])
# sima egydimenziós tömb létrehozva 3 elemmel
print(a)
print(type(a))
# 2d-s tömb float adatmeghatározással
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print(b)
print(type(b))
# 3d-s tömb megadása explicite float típussal
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)
print(c)
print(type(c))

x = np.array([5, 6, 7])
y = np.array([2, 3, 8])

print('x:', x)
print('y:', y)
Result = x - y
print('Kivonás eredménye:', Result)
Result = x + y
print('Összeadás eredménye: ', Result)
Result = x / y
print('Osztás eredménye: ', Result)
Result = x * y
print('Szorzás eredménye: ', Result)
Result = np.exp(x)
print('hatvány eredménye: ', Result)


