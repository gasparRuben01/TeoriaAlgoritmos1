# estadistico de orden k por fuerza bruta

def estadistico(n,k,vectorDeEnteros):
    menoresQueN = 0
    for numero in vectorDeEnteros:
        if numero < n:
            menoresQueN = menoresQueN + 1

    if k == menoresQueN:
        return True


def estadisticoDeOrdenk(k,vectorDeEnteros):
    for n in vectorDeEnteros:
        if estadistico(n,k,vectorDeEnteros):
            estadistico_k = n
    return estadistico_k
