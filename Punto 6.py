# Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
n:int=1#Se declara e inicializa la variable n, especificando que es de tipo int y que tiene un valor inicial de 1
print("Piense en un número que se encuentre entre 1 y 100")
print("El programa va a adivinar ese número, usted solo debe ingresar la palabra 'mayor', 'menor', o 'igual' en minúsculas")#Se muestra el propósito del programa

while n<=100:#Se ejecuta el bloque mientras el número que se esté adivinando sea menor o igual a 100
    pregunta=str(input("El número que usted está pensando es mayor, menor o igual que "+ str(n)+"? "))#El usuario debe contestar "mayor", "menor" o "igual"
    if pregunta=="mayor":#si el usuario escribe mayor
        n+=9#Se incrementa 9 unidades la variable n, para reiniciar el ciclo
    elif pregunta=="menor":#si el usuario escribe menor
        n-=1#Se le resta una unidad a la variable n, para reiniciar el ciclo
    else:#Cuando el usuario escribe igual, se imprime el número que ya se adivinó y se acaba el ciclo usando break
        print("El número que usted pensó es: "+ str(n))
        break
