Alumno = "Picart Fernando"
email = "fxpicart@gmail.com"

# Ej 1
def fibonacci(num):
    """ 
    Sucesion de fibonacci para un numero dado.
    """
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

# Ej 2
def suma_enteros(num):
    """
    Suma numeros comprendidos entre cero y un número entero dado.
    """
    if num == 0:
        return 0
    else:
        return suma_enteros(num-1) + num

#Ej 3
def producto(num1, num2):
    """
    Multiplica dos números dados.
    """
    if (num1 == 0) or (num2 == 0):
        return 0
    else:
        return num1 + producto(num1, num2 -1) 

#Ej 4
def potencia(base, exponente):
    """
    Devuelve potencia de dos numeros enteros.
    """
    if (exponente == 0):
        return 1 
    elif (base == 0):
        return 0
    elif (base == 1):
        return 1
    elif (exponente == 1):
        return base
    elif (exponente < 0) :
        return 1 / producto(base, 0-exponente)  #Si el exponente es negativo se calcula la potencia y se invierte
    else:
        return base * potencia(base, exponente-1)

#EJ 5        
def invertir_cadena(cadena):
    """
    Devuelve una cadena de forma espejada.
    """
    if (len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:-1])

#Ej 6
def serie_fraccionada(num):
    """ 
    Serie h(n) = 1 + 1/2 + 1/3 + ... + 1/n.
    """
    if (num == 1):
        return 1
    else:
        return 1/num + serie_fraccionada(num-1)

#Ej 7
def decimal_a_binario(num):
    """
    Convierte un numero decimal a binario.
    """
    if num == 1:
        return "1"
    elif num == 0:
        return "0"
    else:
        return "" + decimal_a_binario(num // 2) + str(num % 2)

#Ej 8
def logaritmo(base, num):
    """
    Logaritmo entero de un numero dado.
    """
    if (base == num):
        return 1
    else:
        return 1 + logaritmo (base, num/base)

#Ej 9
def contar_digitos(num):
    """
    Cuantos digitos tiene un numero ingresado.
    """
    if (num < 0):
        num = -num
    if (num < 10):
        return 1
    else:
        return 1 + contar_digitos(num/10)

#Ej 10
def invertir_decimal(num, ubicacion=-1):
    """
    Devuelve forma espejada de un numero entero positivo. 
    """
    ubicacion += 1
    digitos = contar_digitos(num)
    if (digitos == 1):
        return num * potencia(10, ubicacion)
    numero_actual = num // potencia(10, digitos-1)
    numero_restante = num - numero_actual * potencia(10, digitos-1) 
    return numero_actual * potencia(10, ubicacion) + invertir_decimal(numero_restante, ubicacion)

#EJ 11
def max_comun_div(num1, num2):
    """
    Calcula el Maximo Comun Divisor de dos numeros.
    """
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
    if mayor % menor == 0:
        return menor                
    else:
        return max_comun_div(menor, mayor % menor)

#EJ 12
def min_comun_mult(num1,num2):
    """
    Calcula el Minimo Comin Multiplo entre dos numeros.
    """
    if (num2 % num1 == 0):
        return num2
    else:
        return min_comun_mult(num2, num1*num2)

#EJ 13
def suma_digitos(num, ):
    """
    Suma los digitos de un entero positivo.
    """
    digitos = contar_digitos(num)
    if (digitos == 1):
        return num
    numero_actual = num // potencia(10, digitos-1)
    numero_restante = num - numero_actual * potencia(10, digitos-1) 
    return numero_actual + suma_digitos(numero_restante)

#EJ 14
def raiz_cuadrada(num,r):
    """"
    Raiz cuadrada de un numero entero.
    Funciona solo con raices cuadradas, si damos un numero que no la tiene, se vuelve una recursividad infinita.
    """
    if r*r == num:
        return r
    elif r*r > num:
        return raiz_cuadrada(num,r-1)
    else:
        return raiz_cuadrada(num,r+1)

#EJ 15
def sucesion_geo(num):
    if (num == 1):
        return 2
    else:
        return -3 * sucesion_geo(num-1)

#EJ 16
def lista_invertida(vec):
    """
    Muestra valores de una lista de forma invertida.
    """
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        lista_invertida(vec[0:-1])

#EJ 17
def recorrer_matriz(lista):
    """
    Recorre e imprime una lista
    """
    for elemento in lista:
        if type(elemento) == list:
            recorrer_matriz(elemento)
        else:
            print(elemento)

#EJ 18
def formula_ej18(num):
    if (num <= 0):
        return 'error'
    elif (num == 1):
        return 2
    else:
        return (num+1) / formula_ej18(num-1)

#EJ 19
vec = [1,2,3,4,5,6,7]
i = 0
def busqueda_secuencial(bus, vec):
    """
    Busca un elemento dentro de una lista.
    """
    global i
    if (bus == vec[i]):
        return i
    else:
        i += 1
        return busqueda_secuencial(bus,vec)
print(busqueda_secuencial(4,vec))

#EJ 20
lista = [0,4,7,18,19,20,33,88,50,10]
def quicksort(lista,pri,ult):
    """
    Ordenar un array por metodo QuickSort
    """
    if (pri < ult):
        aux = ult
        izq = pri
        der = ult-1
        while (izq < der):
            while (lista[izq] < lista[aux-1]):
                izq += 1
            while (lista[der] > lista[aux-1]):
                der -= 1
            if (izq < der):
                lista[izq], lista[der] = lista[der], lista[izq]
        if (lista[izq] > lista[aux-1]):
            lista[izq], lista[aux-1] = lista[aux-1], lista[izq]
        quicksort(lista, pri, izq-1)
        quicksort(lista, izq+1, ult) 

def busqueda_binaria(bus, lista, pri=-1, ult=-1):
    """
    Busca un valor en una lista ordenada.
    Devuelve ubicacion o -1
    """
    if (pri == -1) and (ult == -1):
        pri = 0
        ult = len(lista) - 1 
    med = (ult + pri) // 2
    if (ult - pri) == 1:
        if bus == lista[pri]:
            return pri
        elif bus == lista[ult]:
            return ult
        else:
            return -1
    elif (bus == lista[med]):
        return med
    elif (bus < lista[med]):
        return busqueda_binaria(bus, lista, pri, ((ult + pri) // 2))
    elif (bus > lista[med]):
        return busqueda_binaria(bus, lista, ((ult + pri) // 2), ult)

#ej 21
lista =[['15,25', 'blaster principal', False],
        ['40,50', 'blaster secundario', True],
        ['13,87', 'cañon', True],
        ['42,05', 'blaster principal', False]]
def contar_naves(vec):
    if (len(vec) == 0):
        return 0
    else:
        if (vec[-1][2]):
            return (1 + contar_naves(vec[0:-1]))
            print(vec)
        else:
            return (0 + contar_naves(vec[0:-1]))
            print(vec)

#EJ 23
def torres_de_Hanoi(cantidad_discos):
    """
    Extraido de: Programacion en Turbo Pascal 7 3ra edicion
    Luis Joyanes Aguilar
    Mc Graw Hill
    """       
    def mover_torre( numero_discos, torre1, torre2, torre3):
        def mover_disco(desde, hasta):
            print("mover un disco desde el poste %d hasta el poste %d" %(desde, hasta))
        
        if numero_discos == 1 :             #Condicion de salida
            mover_disco(torre1, torre3)
        else:
            mover_torre(numero_discos-1, torre1, torre3, torre2)
            mover_disco(torre1, torre3)
            mover_torre(numero_discos-1, torre2, torre1, torre3)
    ###INICIO
    print("Para %d discos los movimientos sucesivos son: " %cantidad_discos)
    mover_torre(cantidad_discos, 1, 2, 3)
    #FIN torres_de_Hanoi

#Ej 24
def sucesion24(num):
    if(num==1):
        return 5.25
    else:
        return sucesion24(num-1) * 4
#Ej 25
def formula_ej25(num):
    if (num <= 0):
        return 'error'
    elif (num == 1):
        return 3
    else:
        return (formula_ej25(num-1) + 2)





#FALTAN 22,26,27,28