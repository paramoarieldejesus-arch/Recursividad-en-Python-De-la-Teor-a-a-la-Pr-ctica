#4 Caminos en un Tablero

def contar_caminos(n, m):
    if n == 1 or m == 1:
        return 1
    
    return contar_caminos(n - 1, m) + contar_caminos(n, m - 1)

print(contar_caminos(3, 3))  # 6
