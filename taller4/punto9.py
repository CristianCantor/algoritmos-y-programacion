"""
Entradas: Valores enteros correspondientes al tipo de gas
Tipo de gas --> int --> X
Salidas: 4 valores str con las respectiva cantidades de cada gas
MUITO OBRIGADO --> str --> B
Alcool --> str --> Alcool
Gasolina --> str --> Gasolina
Diesel --> str --> Diesel
"""

# entradas
# Caja negra
Alcool = 0 
Gasolina = 0 
Diesel = 0
while True:
    X = int(input()) 
    if X == 1: 
        Alcool += 1
    elif X == 2: 
        Gasolina += 1
    elif X == 3:
        Diesel += 1
    elif X == 4:
        break
    else: 
        X = X

# Salidas
print("MUITO OBRIGADO")
print("Alcool:",Alcool)
print("Gasolina:",Gasolina)
print("Diesel:",Diesel)