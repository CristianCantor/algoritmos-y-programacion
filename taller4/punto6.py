"""
Entradas: 2 numeros enteros que se procederan a dividir utilizando restas sucesivas
Numero 1 --> int --> x
Numero 2 --> int --> Y
Salidas: El resto de la división 
Resto --> int --> x
"""

# Entradas 
x = int(input("\nDime el primer numero (Dividendo) "))
Y = int(input("Dime el Segundo numero (Divisor) "))

# Caja negra
print()
C = int(x/Y)
N = 0
for i in range(C):
    print(f"{x} - {Y} = {x-Y}")
    x = x - Y
    N += 1

# Salidas
print(f"\nEl resto de la división es {x}")
print(f"El cociente de la dicisión es {N}\n")