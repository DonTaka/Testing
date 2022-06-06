#Numpy sera nuestra biblioteca que nos permitira usar Array como variable
#Se debe instalar aplicando ctrl + shift + Ñ para abrir la consola de visual studio
#Ingrearemos el comando pip install numpy , esperamos y listo 
#Para utilizarla se debe colocar al inicio del codigo "import numpy"
import numpy as np

arreglo = np.array([1,2,3,4])
print(arreglo)
print(arreglo.ndim)
print(len(arreglo))
print(arreglo.shape)
print(arreglo[1:3])
#a[start:stop:step]
print(arreglo[1:3:2])
print(arreglo[2::1])

arreglo2 =[i for i in range(5)]
print(arreglo2)

for i in range(0,len(arreglo2)):
    print(arreglo2[i])

#arange nos permite rellenar un array con valores hasta el numero que definamos en el parentesis
#4 = rellenaria de 0 a 3 
#4.0 = rellenaria de 0 a 3 con decimal
#(4,7)= rellenaria con numeros de 4 a 7
arreglo3 = np.arange(4)
print (arreglo3)

#para copiar un arreglo podemos hacer lo sig 
arreglo4 = np.array([1,2,3])
# Forma 1 : arreglo5 = arreglo4[:]
# Forma 2 : 
arreglo5 = arreglo4[:].copy()
print(arreglo5)
arreglo5[0] = 100;
print(arreglo4)
print(arreglo5)
