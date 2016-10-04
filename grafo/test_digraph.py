#!/usr/bin/env python

import unittest
from Digraph import Digraph

class TestDigraph(unittest.TestCase):
	def test_iterador_de_aristas_adyacentes_a_nodo_v(self):
		digraph=Digraph(11)
		nodo_origen=0
		nodos_adjacentes=[1, 5, 6, 9]
		for i in nodos_adjacentes:
			digraph.add_edge(nodo_origen, i)
		#esta lista guarda los nodos que ya fueron recorridos		
		nodos_recorridos=[]
		for i in digraph.adj_e(0):
			#checke si un nodo adjacente fue recorrido mas de una vez
			self.assertFalse(i[1] in nodos_recorridos, "el nodo "+str(i[1])+" se reccorio dos veces")
			#los nodos adjacents no son recorridos en ningun orden en especial, por lo que pregunto si es alguno de la lista
			self.assertTrue(i[1] in nodos_adjacentes)
			nodos_recorridos.append(i[1])
		

if __name__=='__main__':
	unittest.main()
