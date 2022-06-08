import numpy as np
import random as rd
rd.seed(100);
relleno = [];
for i in range(10):
    relleno.append(rd.randint(0,100))

arreglo = np.array(relleno)
arreglo2 = arreglo[:].copy()
print(arreglo2)
print(arreglo2.max())
print(arreglo2.min())
print(arreglo2.sum())
print(arreglo2.mean())
for i in arreglo2:
    print(i)

