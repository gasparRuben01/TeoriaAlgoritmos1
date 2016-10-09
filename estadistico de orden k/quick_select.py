#!usr/bin/env python

import pdb

def partition(elements, iz, derch):
	""" Funcion interna de quick_select, particiona la secuencia en tres grupos.
	    Los elementos de la secuencia menores a index (elemento de la secuencia en la posicion index) a la izquierda de este y
            los mayores a su derecha. Retorna index (no el elemento, si no la posicion)"""
	if not elements or iz>derch or iz>len(elements) or derch>len(elements):
		raise ValueError('empty sequence')
	else:
		index=iz-1
		#tomo ultimo elemento como pivote
		for i,j in enumerate(elements[iz:derch], iz):
			if j<elements[derch]:
				index+=1
				elements[i],elements[index]=elements[index],elements[i]
		index+=1		
		elements[index], elements[derch]=elements[derch], elements[index]
	return index

def quick_select(elements, k):
	""" si k es positivo o cero retorna el k esimo elemento mas pequenio, si k>len(elements), retorna el maximo
	    si k es negativo retorna el k esimo elemento mas grande, si -k>len(elements), retorna el minimo"""
	if k<0:
		#si k es negativo retorno el k esimo elemento mas grande, si |k|>n entonces retorno el minimo elemento
		k=max(len(elements)+k,0)
	i=0
	d=len(elements)-1
	while True:
		index=partition(elements, i, d)
		if index==k:
			return elements[index]
		elif index<k:
			if index+1==len(elements):
				return elements[index]
			i=index+1
		else:
			d=index-1


