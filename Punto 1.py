#Problema planteado: Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

x:int#Se declara la variable x, especificando que es de tipo int (dado a que el programa funciona con números enteros)
x=1#Se inicializa a x en 1, ya que el listado debe empezar con este número

while x<=100:#Se ejecuta el bloque mientras x sea menor o igual a 100 (dado a que el listado debe llegar hasta 100)
    cuadrado=x**2#Se halla x elevado a la dos
    print(x, cuadrado, sep=", ")#Se imprimen los valores de x y de x al cuadrado, usando el parámetro separador
    x+=1#x se incrementa una unidad para reiniciar el ciclo hasta que no se cumpla la condición de x<=100

    