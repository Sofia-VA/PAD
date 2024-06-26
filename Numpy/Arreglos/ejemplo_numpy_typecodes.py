# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:56:26 2022

@author: ghernand

tomado de otro autor y comentado
Imprime una matriz de compatibilidad para conversión de tipos
"""

import numpy as np

mark = {False: ' -', True: ' Y'}

def print_table(ntypes):
    print('X ' + ' '.join(ntypes))
    print()
    for row in ntypes:
        print(row, end='')
        for col in ntypes:
            # can_cast() Devuelve True si la conversión entre tipos de datos 
            # puede ocurrir de acuerdo con la regla de conversión.
            print(mark[np.can_cast(row, col)], end='')
        print()


print_table(np.typecodes['All'])

'''
Salida del código 
X ? b h i l q p B H I L Q P e f d g F D G S U V O M m

? Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
b - Y Y Y Y Y Y - - - - - - Y Y Y Y Y Y Y Y Y Y Y - Y
h - - Y Y Y Y Y - - - - - - - Y Y Y Y Y Y Y Y Y Y - Y
i - - - Y Y Y Y - - - - - - - - Y Y - Y Y Y Y Y Y - Y
l - - - Y Y Y Y - - - - - - - - Y Y - Y Y Y Y Y Y - Y
q - - - - - Y Y - - - - - - - - Y Y - Y Y Y Y Y Y - Y
p - - - - - Y Y - - - - - - - - Y Y - Y Y Y Y Y Y - Y
B - - Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
H - - - Y Y Y Y - Y Y Y Y Y - Y Y Y Y Y Y Y Y Y Y - Y
I - - - - - Y Y - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - Y
L - - - - - Y Y - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - Y
Q - - - - - - - - - - - Y Y - - Y Y - Y Y Y Y Y Y - -
P - - - - - - - - - - - Y Y - - Y Y - Y Y Y Y Y Y - -
e - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y Y - -
f - - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y - -
d - - - - - - - - - - - - - - - Y Y - Y Y Y Y Y Y - -
g - - - - - - - - - - - - - - - Y Y - Y Y Y Y Y Y - -
F - - - - - - - - - - - - - - - - - Y Y Y Y Y Y Y - -
D - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y - -
G - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y - -
S - - - - - - - - - - - - - - - - - - - - Y Y Y Y - -
U - - - - - - - - - - - - - - - - - - - - - Y Y Y - -
V - - - - - - - - - - - - - - - - - - - - - - Y Y - -
O - - - - - - - - - - - - - - - - - - - - - - - Y - -
M - - - - - - - - - - - - - - - - - - - - - - Y Y Y -
m - - - - - - - - - - - - - - - - - - - - - - Y Y - Y
''
