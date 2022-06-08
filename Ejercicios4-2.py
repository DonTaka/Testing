import numpy as np
import random as rd
rd.seed(100)
relleno = [];
for i in range(10):
    relleno.append(rd.randint(0,1000))

arreglo_1 = np.array(relleno);
#Mostrar todos los elementos del arreglo
print(arreglo_1);
#Mostrar todos los elementos del arreglo uno a uno 
for i in range(len(arreglo_1)):
    print(f"Elemento {i+1} es: {arreglo_1[i]}");

#contar elementos 
contador = 0;
for i in range(len(arreglo_1)):
    if(arreglo_1[i]%2==0):
        contador+=1;
print(f"Hay {contador} numeros pares en el Array");

#sumar elementos impares
suma = 0;
for i in range(len(arreglo_1)):
    if(arreglo_1[i]%2!=0):
       suma = suma+arreglo_1[i]
        
print(f"La suma de los elementos impares es: {suma}");

#Mensaje por cada elemento primo
for x in range(len(arreglo_1)):
    for i in range(2,arreglo_1[x]):
        if (arreglo_1[x]%i==0):
            break;
    print(f"{arreglo_1[x]} es numero primo");



