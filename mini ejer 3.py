#3 Imprimir Patrón

def imprimir_patron(n):
    if n == 0:
        return
    
    imprimir_patron(n - 1)
    print("*" * n)

imprimir_patron(3)
# Salida:
# *
# **
# ***
