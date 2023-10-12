# Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

def primo (n:int)->int: #Se crea la función llamado primo, que permite hallar los primos desde 1 hasta n
    i:int=2#Se declara e inicializa i, este es entero y su valor inicial es 2. i corresponde a cada número entre 2 y n.
    x:int=2#Se declara e inicializa x, es entero y su valor inicial también es 2. x va a ser el divisor de i (cuando todos los residuos del mismo i dividido los valores de x sean distintos a 0, el número i es primo )

    while i<=n:#el bloque se va a ejecutar mientras i sea menor o igual al n dado 
        if (x<=(i**0.5)): #Se determina que i puede ser primo solo si x es menor o igual a la raiz cuadrada de i (ya que para determinar si i es o no primo basta con buscar si x es un divisor hasta la raiz cuadrada de i, pues si hasta la raiz cuadrada de i no se ha encontrado ningun divisor es imposible encontrar otro divisor luego.)
            if i%x==0:#Si el residuo de i dividido x es igual a 0, entonces el número i no es un primo
                i+=1#i aumenta una unidad para reiniciar el ciclo hasta que i sea mayor que n
                x=2#x vuelve a inicializarse en 2, para reiniciar el ciclo y determinar si el siguiente valor de i corresponde o no a un número primo
            else:#Si el residuo de i dividido x es distinto a 0
                x+=1#x aumenta una unidad para reiniciar el ciclo y determinar si i es primo o no
        else:#Se determina que si x es mayor a la raiz cuadrada de i, el número es primo
            print (i)#Se imprime el número primo
            i+=1#i aumenta una unidad para reiniciar el ciclo hasta que i sea mayor que n
            x=2#x vuelve a inicializarse en 2, para reiniciar el ciclo y determinar si el siguiente valor de i corresponde o no a un número primo
    

if __name__=="__main__":#Función principal
    n:int=100#se declara e inicializa n, esta variable es de tipo int y su valor es 100 (pues la instrucción pide los números primos hasta el 100)
    primosHastaCien=primo(n)#Se llama la función declarada al inicio del algoritmo, para que se muestren los números primos hasta 100
    

