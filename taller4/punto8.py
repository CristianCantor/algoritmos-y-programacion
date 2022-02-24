"""
Entradas: un valor entero que va a ser nuesta contraseña
Contraseña --> int --> X 
Salidas: 2 cadenas de texto dependiendo si la contraseña es correcta o no
Correcta --> str --> B 
Incorreta --> str ---> C
"""
# Entrada
X = int(input())

# Caja negra
while X != 2002:
    print("Senha Invalida") 
    X = int(input())

# Salida
print("Acesso Permitido")