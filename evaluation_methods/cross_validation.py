from __future__ import absolute_import
from ..classifiers import k_nearest_neighbors
import numpy as np
import random

def main(
	c = [
		np.array([[1,3,1,2,3],[2,5,5,2,3]]),
		np.array([[6,6,7,8,8],[4,3,4,4,5]])
 	], vector=[6, 5], k = 3):

	#Numero de representantes para entrenar y para validar
	N = c[0].shape[1] 
	n_test = N // 2
	n_train = N - n_test
	ok = 0
	bad = 0
	#Numero de clases
	n_cs = len(c)
	#Elementos totales 
	elem_tot = N * n_cs

	for i in range(0,20):
		elem_test = random.sample(range(0, N), n_test)
		n_class = 0
		for matrix in c:
			#Nuevo conjunto de clases
			new_c = c
			print ("nueva c" + str(new_c))
			n_class += 1
			pos_clas = n_class - 1
			coordenates = np.transpose(matrix)
			n_elem = 0
			for elem in coordenates:
				aux_c = np.delete(coordenates, elem_test, 0)
				new_c[pos_clas] = np.transpose(aux_c)
				print (new_c)
				flag = 0
				for elem_new_c in aux_c:
					if np.array_equal(elem, elem_new_c):
						flag = 1
						break

				if flag == 0:
					vector = elem
					belong_c = k_nearest_neighbors.main(new_c, vector, k)
					print (belong_c)
					if belong_c == n_class:
						ok += 1
					else:
						bad += 1
					n_elem += 1

	good = (ok / (bad+ok))*100
	print("Eficiencia del clasificador: "+ str(good) + "%")

		

if __name__ == '__main__':
	main()