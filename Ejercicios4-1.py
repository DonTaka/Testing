import numpy as np
import random as rd
rd.seed(500);
relleno = [];
for i in range(10):
    relleno.append(rd.randint(0,500))

arregloA = np.array(relleno);
print(arregloA)
#Indice par
for i in range(1,len(arregloA)):
    if(i%2==0):
        print(arregloA[i])

#Mayor
print(f"Elemento mayor del arreglo: {arregloA.max()}");

#Indice del numero mayor del arreglo
indiceMayor=0;
for i in range(len(arregloA)):
    if(arregloA[i]==arregloA.max()):
        indiceMayor=i;

print(f"Indice del numero mayor: {indiceMayor}")

#Elemento Menor
print(arregloA.min())

#Copia ArregloA y multi 3

arregloB = arregloA[:].copy();
print(arregloB)
arregloB = arregloB*3;
print(arregloB)

#Suma elementos segundo arreglo
print(arregloB.sum())

#Promedio elementos segundo arreglo
print(arregloB.mean())

