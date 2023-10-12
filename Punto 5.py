# Imprimir el factorial de un número natural n dado.
print("Este programa imprime el factorial de un número ingresado por usted")#Se explica el propósito del programa

n:int#Se declara la variable n, especificando que es de tipo int (el programa funciona con números enteros)
n=int(input("Ingrese un número natural para hallar su factorial: "))#Se utiliza la función input(), para que el usuario pueda ingresar el valor de n
m:int#Se declara la variable m, la cual es de tipo int
m=(n-1)#El valor de m corresponde a n-1

while m>=1:#Se ejecuta el bloque mientras m sea mayor o igual a 1
    n*=m#n es igual a n multiplicado por m 
    m-=1#m se reduce una unidad para que se reinicie el ciclo hasta que m sea menor que 1

print("El factorial del número ingresado es "+ str(n)+ ".")#Cuando se acaba el ciclo, se imprime el factorial que corresponde a n*(n-1)*(n-2)...*1
