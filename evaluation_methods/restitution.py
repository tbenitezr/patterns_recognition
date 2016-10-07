from __future__ import absolute_import
from ..classifiers import k_nearest_neighbors
import numpy as np

def main(
	c = [
		np.array([[1,3,1,2,3],[2,5,5,2,3]]),
		np.array([[6,6,7,8,8],[4,3,4,4,5]])
 	], vector=[6, 5], k = 3):

	
	n_class = 0
	ok = 0
	bad = 0
	for matrix in c:
		n_class += 1
		coordenates = np.transpose(matrix)
		for elem in coordenates:
			vector = elem
			belong_c = k_nearest_neighbors.main(c, vector, k)
			print (belong_c)
			if belong_c == n_class:
				ok += 1
			else:
				bad += 1

	good = (ok / (bad+ok))*100
	print("Eficiencia del clasificador: "+ str(good) + "%")

		

if __name__ == '__main__':
	main()