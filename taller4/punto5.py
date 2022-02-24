"""
Entradas: ----
Salidas: El numero de terminos nesesarios para que la exprexión se acerque a 1000
Terminos --> int --> Y
Sumatoria --> int --> B
"""
# Caja negra
Y = 1
while True:
    B = ((Y**2)+1)/Y
    if B > 1000:
        Y -= 1
        B = ((Y**2)+1)/Y
        break
    else: 
        print(Y)
        Y += 1
# Salidas
print("\nEl numero de terminos necesarios es:",Y)
print("El resultado de la sumatoria es:",B,"\ncuando k es:",Y,"\n")