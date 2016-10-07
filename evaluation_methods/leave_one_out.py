from __future__ import absolute_import
from ..classifiers import k_nearest_neighbors
import numpy as np

def main(
	c = [
		np.array([[1,3,1,2,3],[2,5,5,2,3]]),
		np.array([[6,6,7,8,8],[4,3,4,4,5]])
 	], vector=[6, 5], k = 3):

	n_cs = len(c)
	n_class = 0
	pos_clas = 0
	ok = 0
	bad = 0
	new_c = c
	for matrix in c:
		n_class += 1
		coordenates = np.transpose(matrix)
		n_elem = 0
		for elem in coordenates:
			vector = elem
			new_c[pos_clas] = np.transpose(np.delete(coordenates, n_elem, 0))
			belong_c = k_nearest_neighbors.main(new_c, vector, k)
			print (belong_c)
			if belong_c == n_class:
				ok += 1
			else:
				bad += 1
			n_elem += 1
		pos_clas += 1

	good = (ok / (bad+ok))*100
	print("Eficiencia del clasificador: "+ str(good) + "%")

		

if __name__ == '__main__':
	main()