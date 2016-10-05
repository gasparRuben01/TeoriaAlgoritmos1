import unittest
import Paths
from Digraph import Digraph

#esta clase tiene un digrafo con las aristas y vertices ya fijados a manos. Junto con la distancia de los nodos.
#la funcion de esta clase es para ser utilizadas en las pruebas.
#las aristas de este arbol tienen todas el mismo peso
class DigraphNoPonderado(object):
	def __init__(self):
		#hardcode digraph y distancias.
		self.digraph=Digraph(5)
		self.digraph.add_edge(0, 1, 1)
		self.digraph.add_edge(1, 2, 1)
		self.digraph.add_edge(1, 4, 1)
		self.digraph.add_edge(2, 3, 1)
		self.digraph.add_edge(3, 4, 1)
		self.digraph.add_edge(3, 1, 1)
		self.distancias=[[0, 1, float('inf'), float('inf'), 1], [float('inf'), 0, 1, 2, 3], [float('inf'), 2, 0, 1, 2], [float('inf'), 1, 2, 0, 1],
				[float('inf'), float('inf'),float('inf'), float('inf'), 0]]
	def check_distancias(self, path, origin):
		for destiny in range(5):
			if path.distance(i)!=self.distancias[origin][destiny]:
				self.wrong_distance_node=i
				return False
		self.wrong_distance_node=None
		return True
	

digraph_no_ponderado=DigraphNoPonderado()

class TestBFFS(unittest.TestCase):
	def test_distancia(self):
		for i in digraph_no_ponderado.digraph:
			bffs=BFFS(digraph_no_ponderado.digraph, i)
			self.asserTrue(digraph_no_ponderado.check_distancias(bffs, i),
				       "Error la distancia al nodo "+str(digraph_no_ponderado.wrong_distance_node)+" es incorrecta")


if __name__=='__main__':
	unittest.main()





