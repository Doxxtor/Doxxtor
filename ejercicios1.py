import sys
def ej1_max2Num(n1, n2):
#Esta funcion devuelde el mayor de dos numeros dados aunque esta funcion del ya existe en python como max()
    if n1 > n2:
        print(f"El numero mas grande es {n1}")
    else:
        print(f"El numero mas grande es {n2}")
def ej2_max_de_tres(n1, n2, n3):
    #We going to take the value of three arguments and showing as result the maximum of them.
    #Basicamente lo que hice fue añadir un elif mas a la funcion, quiza no es la solucion mas elegeante pero funciona.
    if n1 > n2 and n3:
         print(f"El numero mas grande es {n1}")
    elif n2 > n3:
        print(f"El numero mas grande es {n2}")
    else:
        print(f"El numero mas grande es {n3}")
def ej3_len(listORstring):
#print(len(listORstring)) Esta es con la funcion por defecto en python len(), podriamos usar la nuestra ahora que seguro es algo similar.
    cuenta= 0
    for i in listORstring:
        cuenta +=1
    print(cuenta)
def ej4_Vocal(letra):
    letra1 = str(letra).lower()
    vocales = ["a", "e", "i", "o" , "u"]
    if letra1 in vocales:
        print("Esta letra es una Vocal")
    else:
        print("Esta letra no es una Vocal")
def ej5_sum(lista):
    #Primero creamos la variable X para la suma de los numeros, despues con un for  vamos listando los numeros de variable
    #"lista" dada, depsues imprimimos X 
    x = 0
    for i in lista:
        x += i
    print(f"Resultado: {x}")
def ej5_multip(lista):
    #Lo mismo que en la funcion sum pero multiplicando pero asignando a "X" 1 en vez de 0 porque 0*0 o 0*"X" es "F"
    x = 1
    for i in lista:
        x *= i
    print(f"Resultado: {x}")
def ejer6_inversa(texto):
    x = str(texto) [::-1] #Aqui usamos el [::-1] para ir hacia atras -1 osea uno a uno -2 ira de dos en dos
    print(x)
def ejer7_palindromo(texto):
    """Pues aqui tarde mas de lo normal, no supe como obligar al a entrada de la funcion de la cadena sea minusculas
        o llamar a mi otra funcion para que haga el reverse en fin estoy seguro de que lo puedo mejorar"""
    textoL = texto.lower()
    reves = textoL [::-1]
    if reves == textoL:
        print("Palindromo")
    else:
        print("Noo palindromo")
        print(reves)
def ejer8_superposicion(lista1, lista2):
    #sys.exit()  Sin los sys se ve mas bonito porque indica en que indice hay duplicidad y en cuales no, aparte de leer todos
                            # valores no como con los sys que se para al encontrar una diferencia.
    for i in lista1:
        if i in lista2:
            print("Hay duplicated")
            print(i)
            #sys.exit()      #Esta es la solucion que yo plantée pero la mostrada abajo esa mas simple.
        else:
            print("No hay duplicated\n")
def ejer9_generar_n_caracteres(str, int):
#ejer9_generar_n_caracteres("Te amo \n", 50)s
    print(str * int)
def ejer10_procedimiento(lista):
    for i in lista:# Es las solucion mas logica, escalable simplemente va leyendo los valores con un FOR y imprimiendo tantas estrellitas
        print("*" * i)# como sean necesarias
"""
Ejercicios Python
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""