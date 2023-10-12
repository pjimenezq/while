# Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
print("Este programa imprime los divisores de un número ingresado por usted. El número debe estar entre 2 y 50")#Se explica el propósito del programa

n:int#Se declara la variable n, especificando que es de tipo int (el programa funciona con números enteros)
n=int(input("Ingrese un número que sea mayor o igual al 2 y menor o igual a 50: "))#Se utiliza la función input(), para que el usuario pueda ingresar el número n

divisor:int#Se declara la variable divisor, especificando que es de tipo int
divisor=1#Se inicializa a divisor en 1 (pues este es el primer divisor común a todos los números)

print("Los divisores de "+str(n)+ " son: ")#Se imprime esta frase, esta se muestra antes del listado de los divisores de n

while n>=2 and n<=50 and divisor<=(n/2): #Se ejecuta el bloque si n está entre 2 y 50 y mientras el divisor sea menor o igual a la mitad del número dado (dado a que es imposible que existan divisores, diferentes a n, que sean mayores a la mitad de n)
    if n%divisor==0: #Si el residuo de n dividido el valor del divisor es igual a 0, significa que el valor de la variable divisor sí es un divisor de n
        print(divisor)#Si se cumple la condición anterior se imprime el divisor
        divisor+=1#El divisor aumenta una unidad para reiniciar el ciclo hasta que la variable divisor sea mayor que n dividido entre 2
    else:#Si el residuo de n dividido el valor del divisor es distinto a 0, el valor de la variable divisor no es un divisor de n, por lo tanto el divisor no se imprime
        divisor+=1#El divisor aumenta una unidad para reiniciar el ciclo hasta que la variable divisor sea mayor que n dividido entre 2
print(n)#Dado a que se evaluaron los divisores menores o iguales a la mitad de n, se debe imprimir n porque este es un divisor para todo n