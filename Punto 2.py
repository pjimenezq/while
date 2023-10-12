# Problema planteado: Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

x:int#Se declara la variable x, especificando que es de tipo int (dado a que el programa funciona con números enteros)
x=1#Se inicializa a x en 1, ya que el listado de los números impares debe empezar con este número

while x<=999 and x%2!=0:#Se ejecuta el bloque mientras x sea menor o igual a 999 (el listado de impares debe llegar hasta 999) y mientras el residuo de x dividido 2 sea diferente a 0 (propiedad de números impares)
    print(x)#Se imprime el valor del número impar x
    x+=2#x se incrementa dos unidades (sumando 2 a un número impar se obtiene otro número impar) para reiniciar el ciclo hasta que x>999

#Cuando la condición del ciclo while se deja de cumplir, este se termina y se empieza a ejecutar el siguiente bloque de instrucciones

x=2#Se inicializa a x en 2, ya que el listado de los números pares debe empezar con este número

while x<=1000 and x%2==0:#Se ejecuta el bloque mientras x sea menor o igual a 1000 (el listado de impares debe llegar hasta 1000) y mientras el residuo de x dividido 2 sea igual a 0 (propiedad de números pares)
    print(x)#Se imprime el valor del número par x
    x+=2#x se incrementa dos unidades (Sumando 2 a un número par se obtiene otro número par) para reiniciar el ciclo hasta que x>1000

#En teoría, no es necesario agregar en las condiciones de ambos ciclos while que el residuo de x dividido 2 es diferente o igual a 0, pues para que una lista sea de números impares basta con empezar con un número impar y sumar en cada ciclo 2 unidades (lo mismo aplica para una lista de números pares)
#Aun así, se agrega esta condición en caso de que el valor de 1 de la variable x sea cambiado por un número par o si el valor 2 de la variable x es cambiado por un número impar