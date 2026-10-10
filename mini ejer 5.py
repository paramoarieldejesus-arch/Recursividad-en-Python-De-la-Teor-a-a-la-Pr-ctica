#5 Flatten List

def aplanar(lista):
    if len(lista) == 0:
        return []
    
    if isinstance(lista[0], list):
        return aplanar(lista[0]) + aplanar(lista[1:])
    else:
        return [lista[0]] + aplanar(lista[1:])

print(aplanar([1, [2, [3, 4], 5]]))  # [1, 2, 3, 4, 5]
