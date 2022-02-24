"""
Entradas ---
Salidas: todos los numeros enteros impares menores que 100, sin contar multiplos de 7 
Numeros --> int --> B
"""

# Caja negra 
B = 1
for i in range(50):
    if (B%7) != 0:
        print(B) 

# Salida
        B += 2
    else: 
        B += 2