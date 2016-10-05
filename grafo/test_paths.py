import unittest
import paths
from bfs import BFS
from digraph import Digraph

#esta clase tiene un digrafo con las aristas y vertices ya fijados a manos. Junto con la distancia de los nodos.
#la funcion de esta clase es ser utilizada en las pruebas.
#las aristas de este arbol tienen todas el mismo peso
class DigraphNoPonderado(object):
	def __init__(self):
		#hardcode digraph y distancias.
		self.digraph=Digraph(10)
		self.digraph.add_edge(0, 1, 1)
		self.digraph.add_edge(0, 9, 1)
		self.digraph.add_edge(1, 2, 1)
		self.digraph.add_edge(2, 9, 1)
		self.digraph.add_edge(2, 5, 1)
		self.digraph.add_edge(2, 0, 1)
		self.digraph.add_edge(5, 3, 1)
		self.digraph.add_edge(5, 6, 1)
		self.digraph.add_edge(6, 7, 1)
		self.digraph.add_edge(3, 4, 1)
		self.digraph.add_edge(4, 7, 1)
		self.digraph.add_edge(8, 4, 1)
		self.distancias=[[0, 1, 2, 4, 5, 3, 4, 5, float('inf'), 1], [2, 0, 1, 3, 4, 2, 3, 5, float('inf'), 2], [1, 2, 0, 2, 3, 1, 2, 3, float('inf'), 1],
				  [float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), float('inf'), 2, float('inf'), float('inf')], 
				  [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf'), float('inf'), 1, float('inf'), float('inf')],
				  [float('inf'), float('inf'), float('inf'), 1, 2, 0, 1, 2, float('inf'), float('inf')],
				  [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), float('inf')],
				  [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf'), float('inf')],
				  [float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), float('inf'), float('inf'),0 , float('inf')],
				  [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]]
	def check_distancias(self, path, origin):
		for destiny in range(5):
			if path.distance(destiny)!=self.distancias[origin][destiny]:
				self.wrong_distance=(origin, destiny, path.distance(destiny))
				return False
		
		self.wrong_distance=None
		return True
	

digraph_no_ponderado=DigraphNoPonderado()

class TestBFFS(unittest.TestCase):
	def test_distancia(self):
		for i in digraph_no_ponderado.digraph:
			bfs=BFS(digraph_no_ponderado.digraph, i)
			if not digraph_no_ponderado.check_distancias(bfs, i):
				self.assertTrue(False, "Error la distancia: "+str(digraph_no_ponderado.wrong_distance[2])+" al nodo "+
						str(digraph_no_ponderado.wrong_distance[1])+" desde "+
						str(digraph_no_ponderado.wrong_distance[0])+" es incorrecta")


if __name__=='__main__':
	unittest.main()





