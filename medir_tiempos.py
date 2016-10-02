#!/usr/bin/env python

import random
import time
import sys
import importlib

def medir(orden_k, n, k):
	"""mide el tiempo de ejecucion consumido por orden_k, para encontrar el k-esimo elemento mas pequenio
	   en una lista de n elementos generados al azar. Supone que orden_k solo recibe una lista y un entero k como parametros"""
	list=[]
	for i in range(n):
		list.append(random.uniform(0, n))
	
	tiempo_inicial=time.time()
	orden_k(list, k)
	return time.time()-tiempo_inicial

#recibe como primer parametro la ruta del module que contiene la funcion, como segundo parametro el nombre de la funcion 
#, como tercer parametro el tamanio de la n-upla y por ultimo el k

if __name__=='__main__':
	if len(sys.argv)<5:
		raise ValueError("expected almost 4 parameters got "+str(len(sys.argv)))

	module=importlib.import_module(sys.argv[1])
	print medir(getattr(module, sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
