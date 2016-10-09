#!usr/bin/env python



def partition(elements):
	""" Funcion interna de quick_select, particiona la secuencia en tres grupos.
	    Los elementos de la secuencia menores a index (elemento de la secuencia en la posicion index) a la izquierda de este y
            los mayores a su derecha. Retorna index (no el elemento, si no la posicion)"""
	if not elements:
		raise ValueError('empty sequence')
	else:
		index=-1
		#tomo ultimo elemento como pivote
		for i,j in enumerate(elements[0:-1]):
			if j<elements[-1]:
				index+=1
				elements[i],elements[index]=elements[index],elements[i]
		index+=1		
		elements[index], elements[-1]=elements[-1], elements[index]
	return index


def quick_select(elements, k):
	"""Retorana k-esimo elemento mas pequenio si k es positivo. Si k es mayor a n (la longitud de la secuencia) retorna el maximo valor, si k es negativo
	   retorna el k-esimo mas grande. Si |k|>n, retorna el minimo elemento"""
	if k<0:
		k=len(elements)+k+1
		if k<0:
			k=1
	index=partition(elements)	
	if index+1==k:
		return elements[index]
	elif index+1<k:
		if index+1==len(elements):
			return elements[index]
		return quick_select(elements[index+1:],k-index-1)
	return quick_select(elements[:index], k)
