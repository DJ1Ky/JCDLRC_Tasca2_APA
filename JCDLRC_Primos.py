

""" 
    Nombre: Juan Camilo De Los Ríos
    Práctica 2: Manejo de números primos
"""


# Devuelve "True" si numero es primo, y "False" si no lo es.

def esPrimo(numero):
    for prueba in range(2, numero):
        if numero % prueba == 0: 
            return False
    return True


# Devuelve una lista con todos los números primos menores que su argumento.

def primos(numero):
    lista = []
    for prueba in range(2, numero):
        if esPrimo(prueba) == True:
            lista.append(prueba) 
    return lista


# Devuelve una tupla con la descomposición en factores primos de número.

def descompon(numero):
    
    lista = primos(numero)
    divisible = ()
    x = 0
    if not esPrimo(numero):
        while (numero != 1):
            if (numero % lista[x] == 0):
                divisible += (lista[x], )
                numero = numero / lista [x]
            else: x += 1
    return divisible


# Calculamos el número positivo más pequeño que es múltiplo de numero1 y numero2

def mcm(numero1, numero2):
    d1 = descompon(numero1)
    d2 = descompon(numero2)
    factores = set(d1 + d2)
    dic1 = {primo: 0 for primo in factores}
    dic2 = {primo: 0 for primo in factores}
    lon1 = len(d1)
    lon2 = len(d2)
    resultado = 1

    for x in range(lon1):
        dic1[d1[x]] += 1
    
    for y in range(lon2):
        dic2[d2[y]] += 1

    for x in factores:
        if dic1[x] >= dic2[x]:
            resultado *= (x ** dic1[x])
        else: resultado *= (x ** dic2[x])
        
    return resultado



# Devuelve el máximo común divisor de sus argumentos
    
def mcd(numero1, numero2):
    d1 = descompon(numero1)
    d2 = descompon(numero2)
    factores = set(d1 + d2)
    dic1 = {primo: 0 for primo in factores}
    dic2 = {primo: 0 for primo in factores}
    lon1 = len(d1)
    lon2 = len(d2)
    resultado = 1

    for x in range(lon1):
        dic1[d1[x]] += 1
    
    for y in range(lon2):
        dic2[d2[y]] += 1


    for x in factores:
        if dic1[x] <= dic2[x]:
            resultado *= (x ** dic1[x])
        else: resultado *= (x ** dic2[x])
        
        
    return resultado



print([ numero for numero in range(2, 50) if esPrimo(numero)])

print(primos(50))

# 36 * 175 * 143 = 900900 

print(descompon(36 * 175))

print(mcm(90, 14))

print(mcd(924, 780))


