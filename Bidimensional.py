import numpy as np 

#Podemos declarar nuestro Array bidimensional de 2 maneras 
#m1 con carga directa 
#m2 con la carga de una lista precargada

m1 = np.array([[1,2,3],[4,5,6]]) 
lista = [[10,20,30],[40,50,60]]
m2 = np.array(lista)

#En este caso veremos como recorrer el multi dimensional completo y de manera unitaria 
matriz = np.array([[0,1,2],[3,4,5]])
for f in range(2):
    for c in range(3):
        print(matriz[f][c])
#En caso de que necesitemos buscar una ubicacion en especifico podemos ingresar la ubicacion directamente
#Posicion directa
print(matriz[0][1])
#Segun ubicacion 
#Mostrando un valor de la posicion
print(matriz[:,2])
#Mostrando todos los valores de esa posicion 
print(matriz[0,:])

#Dentro de las muchas funciones de numpy array podemos rellenar con valores segun lo necesitemos
#Rellenando con ceros
m0 = np.zeros((3,3))
print(m0)
#rellenando con unos
mUnos = np.ones((3,3))
print(mUnos)
#O tambien insertando una diagonal entre los valores de ingreso
mDiag = np.diag([1,1,1,1,1])
print(mDiag)

#Otra funcion de utilidad es hacer sumas de los valores de los arreglos

#De manera completa
list = [[1,2,3],[4,5,6]]
matriz = np.array(list)
print(matriz.sum())

#o podemos hacer suma de los arreglos segun posicion
print(f"Suma de elementos fila 0: {matriz[0,:].sum()}")
print(f"Suma de elementos fila 1: {matriz[1,:].sum()}")

#Por ultimo , podemos concatenar o unir los arreglos segun direccion del cubo
#axis dara la direccion para donde realizaremos la union
#0 seria en eje vertical
#1 seria en eje horizontal
ax0=np.concatenate((m1,m2),axis=0);
print(ax0);
#Axis 1
ax1=np.concatenate((m1,m2),axis=1);
print(ax1)
#m1 = [[1,2,3],[4,5,6]]
#m2 = [[10,20,30],[40,50,60]]
#Axis 0 Eje vertical
m3 =np.sum((m1,m2),axis=0)
print(m3)
#Axis 1 Eje Horizontal
m3 =np.sum((m1,m2),axis=1)
print(m3)