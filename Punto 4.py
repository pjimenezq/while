# Problema planteado: En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones.
# Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

print("Este algoritmo permite determinar el año en el que la población del país B superará a la del país A")#Se explica el propósito del programa

poblacionPaisA:int#Se declara la variable correspondiente a la población del país A, se nombra con camelcase y se especifica que es de tipo int (pues se trata del conteo de personas)
poblacionPaisA=25000000#Se inicializa la variable de poblacionPaisA en 25000000 (que según el problema planteado son los habitantes del país A)
poblacionPaisB:int#Se declara la variable correspondiente a la población del país B, se nombra con camelcase y se especifica que es de tipo int (pues se trata del conteo de personas)
poblacionPaisB=18900000#Se inicializa la variable de poblacionPaisB en 18900000 (que según el problema planteado son los habitantes del país B)
año:int#Se declara la variable de año, especificando que es de tipo int (los años son números enteros)
año=2022#Se inicializa la avariable de año en 2022 (ya que los datos de las poblaciones de ambos paises son del año 2022)

while poblacionPaisB<poblacionPaisA:#Se ejecuta el bloque mientras la población del país B sea menor que la población del país A
    poblacionPaisA=(poblacionPaisA*0.02)+poblacionPaisA#La población del país A equivale a su poblacion sumada con crecimiento anual de su población (que se halla multiplicando la población por el crecimiento anual de 2%)
    poblacionPaisB=(poblacionPaisB*0.03)+poblacionPaisB#La población del país B equivale a su poblacion sumada con crecimiento anual de su población (que se halla multiplicando la población por el crecimiento anual de 3%)
    año+=1#El año aumenta una unidad en cada ciclo, esta variable permite determinar posteriormente en qué año la población del país B superará a la del país A
#El ciclo se reinicia hasta que el número correspondiente a la población del país B sea mayor que el número correspondiente a la población del país A

poblacionPaisA=int(poblacionPaisA)#Se usa int(), para que la población sea dada como un entero (Al multiplicar la población por la tasa de crecimiento anual, esta se conviritió en un decimal, pero es imposible que la cantidad de habitantes del país sea un número decimal)
poblacionPaisB=int(poblacionPaisB)#Se usa int(), para que la población sea dada como un entero (Al multiplicar la población por la tasa de crecimiento anual, esta se conviritió en un decimal, pero es imposible que la cantidad de habitantes del país sea un número decimal)
print("La población del país B superará la población del país A en el año "+ str(año)+ ". La población del país B será de " + str(poblacionPaisB)+ " habitantes y la población del país A será de " + str(poblacionPaisA)+" habitantes.")#Se imprime el año en el cual la población del país B superará a la del A, junto a la cantidad de habitantes de ambos paises en ese año
