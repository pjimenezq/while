# Problema planteado: Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
print("En este programa usted ingresa un número natural n y el programa imprime los números pares en forma descendente desde n hasta 2. ")#Se explica el propósito del programa
n:int#Se declara la variable n, especificando que es de tipo int (dado a que el programa funciona con números enteros)
n=int(input("Ingrese un número natural: "))#Se utiliza la función input(), para que el usuario pueda ingresar el valor de n

while n>=2:#Se ejecuta el bloque mientras n sea mayor o igual a 2 (el listado de números pares debe llegar hasta 2)
    if n%2!=0:#Con if se identifica si el número n dado es impar; este es impar cuando se cumple la condición de que el residuo de n dividido 2 es distinto a 0
        n-=1#Si n es impar, se le resta una unidad para que se pueda imprimir el primer número par menor que n
    print(n)#Ya que n es par se imprime su valor
    n-=2#Se restan dos unidades (restando 2 a n par se obtiene el siguiente n par en forma descendente) para reiniciar el ciclo hasta que n llegue a ser menor que 2
print("Ciclo terminado")#Se imprime cuando se evalúa la condición dada y esta ya no se cumple, acabando así el ciclo y el código