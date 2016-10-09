# estadistico de orden k por fuerza bruta

def estadistico(n,k,elements):
    menoresQueN = 0
    for numero in elements:
        if numero < n:
            menoresQueN = menoresQueN + 1

    return k == menoresQueN


def fuerza_bruta(elements, k):
	estadistico_k = 0
	for n in elements:
		if estadistico(n,k,elements):
			estadistico_k = n
			break	

	return estadistico_k
