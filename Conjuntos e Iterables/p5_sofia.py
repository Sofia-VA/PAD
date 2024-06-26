# Práctica 5.Conjuntos y Diccionarios
#   Problema de la Ruleta
#- **Fecha**: 19/09/2023  |  ITESO  
#- **Materia**: Programación para el Análisis de Datos
#- **Alumno**: Sofía Vargas Aceves is77375 


# ----------------------- CONJUNTOS ----------------------- #

import random

game = True
win = False
conjunto = 0

# Rueda
rueda = set(range (37)) | set (['00']) 
# Conjuntos
rojo = set( [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] )
negro, alto, bajo, par, impar, ganador = (set() for i in range(6))
# Llenado de conjunto
for valor in rueda:
    if(valor == '00' or valor == 0):
        ganador.add(valor)
        continue
    if (valor%2==0):
        par.add(valor)
    elif (valor%2!=0):
        impar.add(valor)
    if (valor not in rojo):
        negro.add(valor)
    if (valor>18):
        alto.add(valor)
    else:
        bajo.add(valor)

# Compienzo de juego
print("¡Bienvenid@ al juego de la ruleta!")
saldo = float(input("¿Cuál es tu saldo inicial? "))

while (game):
    
    # Puedes apostar por X
    print('''¿Por cuál atributo quieres apostar?
    1) Par    {}
    2) Impar  {}
    3) Rojo   {}
    4) Negro  {}
    5) Alto   {}
    6) Bajo   {}'''.format(par,impar,rojo,negro,alto,bajo))
    while (conjunto==0):
        try: 
            conjunto = int(input("Ingresa un número de atributo: "))
        except:
            contunto = 0
        if (conjunto!=0): 
            if(conjunto == 1): conjunto = par 
            elif(conjunto == 2): conjunto = impar 
            elif(conjunto == 3): conjunto = rojo 
            elif(conjunto == 4): conjunto = negro 
            elif(conjunto == 5): conjunto = alto 
            elif(conjunto == 6): conjunto = bajo
            else: conjunto = 0
        if (conjunto == 0):
            print("Opción inválida")

    # Determinar apuesta
    while (True):
        print('Saldo: $' + str(saldo))
        apuesta = float(input("¿Cuánto quieres apostar? "))
        if (apuesta > saldo): 
            print('No puedes apostar una cantidad menor a tu saldo')
        elif (apuesta<=0):
            print('Debes apostar una cantidad mayor a 0')
        else: 
            saldo -= apuesta
            break

    # Juego
    print(' > Ruleta girando...')
    giro = random.choice (list(rueda))
    print(' > La ruleta ha caído en: '+str(giro))
    
    if (giro in conjunto):
        print(' > ¡Has ganado!')
        saldo += (apuesta*2)
        print(' > Saldo: $'+str(saldo))
    elif (giro in ganador):
        print(' > ¡Has ganado el premio mayor!')
        saldo += (apuesta*35)
        print(' > Saldo: $'+str(saldo))
    else:
        print(' > ¡Mala suerte! El espacio no tiene tu atributo')

    # Salir del juego si no hay saldo
    if (saldo == 0): break

    # Salir del juego dada la opción
    game = input("¿Quieres jugar de nuevo? S/n").upper() == 'S'
    # Resetear
    conjunto = 0


print('El juego ha concluido')
print('Tu saldo final es de: $'+str(saldo))
print('¡Gracias por jugar!')


# ----------------------- DICCIONARIOS ----------------------- #
print('\n# ----------------------- DICCIONARIOS ----------------------- #')

# Escriba tres versiones de una función a la que se le pasa una lista, un diccionario y una clave K. 
# La función imprime el valor de K del diccionario si la clave está presente tanto en la lista como en el diccionario, de lo contrario imprime mensaje al usuario de que no está en ambos. 

# La versión 1 de la función será usando all() y una expresión generadora (Enlaces a un sitio externo.).
def foo(my_list, my_dict, k):
    if all((k != x or x not in my_dict) for x in my_list):
        print('La llave', k, 'no se encuentra en ambas la lista ni el diccionario.')   
    else:
        print('El valor de', k , 'en el diccionario es:', my_dict[k]) 
    

# La versión 2 de la función será usando el operador in
def foo2(my_list, my_dict, k):
    if (k in my_list and k in my_dict):
        print('El valor de', k , 'en el diccionario es:', my_dict[k]) 
    else:
        print('La llave', k, 'no se encuentra en ambas la lista ni el diccionario.')

# La versión 3 será usando intersección de conjuntos
def foo3(my_list, my_dict, k):
    k_list = set(my_list) & set(k)
    if(k_list & set(my_dict)):
        print('El valor de', k , 'en el diccionario es:', my_dict[k]) 
    else:
        print('La llave', k, 'no se encuentra en ambas la lista ni el diccionario.')


# Desarrolle dos casos de prueba (para cuando está presente la clave y para cuando no lo está) y ejecute las corridas de los dos casos.
my_list = ['a','b','c']
my_dict = {'a':25,'b':50,'d':100}

print('\n# --- Función 1 --- #')
foo(my_list,my_dict,'b')
foo(my_list,my_dict,'c')

print('\n# --- Función 2 --- #')
foo2(my_list,my_dict,'b')
foo2(my_list,my_dict,'d')

print('\n# --- Función 3 --- #')
foo3(my_list,my_dict,'a')
foo3(my_list,my_dict,'c')