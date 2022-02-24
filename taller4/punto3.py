"""
Entradas ----
Salidas: la suma de todos los numeros pares 
Suma --> int --> B
"""

#entrada
B = 0 

# Caja negra 
for i in range(98,1003,2):
    B += i 

# salida
print(f"\n{B}\n") 