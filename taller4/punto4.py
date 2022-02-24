"""
Entradas: ---
Salidas: 2 valores enteros uno que el dato en la posición 12 de la sucesión, y la suma de los 
primeros 12 valores de la sucesión
Posición 12 --> int --> X
Suma --> int --> Y
"""

# entrada
Y = 0

# caja negra
for i in range(12):
    X = 5*i + 6
    Y = Y + X
    
# salida
print("\nEl término doceavo en la suceción es:",X) 
print("La suma de los primeros 12 numeros de la sucesión es:",Y,"\n") 