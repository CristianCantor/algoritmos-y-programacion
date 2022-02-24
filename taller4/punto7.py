"""
Entradas: 2 valores enteros que indican el multiplicador de xp y el xp que dan los mounstruos
Multiplicador --> int --> M
XP --> int --> B
Salidas: El xp que dará el mounstruo actualmente
XP_actual --> int --> C
"""

while True:
    M = input().split() 
    X = int(M[0]) 
    M = int(M[1]) 
    if X == 0 and M == 0:
        break
    else: 
        C = M * X
    print(C) 