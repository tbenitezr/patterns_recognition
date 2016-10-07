import matplotlib.pyplot as plt
import numpy as np
import cmath as math 

def main(
	c = [
		np.array([[1,3,1,2,3],[2,5,5,2,3]]),
		np.array([[6,6,7,8,8],[4,3,4,4,5]]),
		np.random.rand(2,5) + 4,
 		np.random.rand(2,5) + 1
 	], vector=[4, 5]):
	#Colores
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
	markers = [ '.', ',', 'o',"v", "^", "<", ">", "1",
				"2", "3", "4", "8", "s", "p", "*", "h",
				"H", "+", "x", "D", "d", "|", "_", "TICKLEFT", 	
				"TICKRIGHT", "TICKUP", "TICKDOWN", "CARETLEFT",
				"CARETRIGHT", "CARETUP", "CARETDOWN"]

	
	print (vector)

	plt.figure()

	#Numero de columnas
	N = c[0].shape[1]
	print N

	averages = list()
	pre_covs_matrix = list()
	covariances = list()
	inverses = list()
	vecs_avers = list()
	mahalannobis = list()
	exps = list()
	dets = list()
	probabilitys = list()
	figures = list()
	cont = 0
	for matrix in c:
		cont += 1
		label_figure =  "Clase "+ str(cont)
		figures.append(plt.scatter(matrix[0], matrix[1], color=colors[cont], marker=markers[cont], label=label_figure))
		print ("Matriz ")
		print (matrix[-1])
		#print (matrix[-1][1])
		#Obtener media
		averages.append(np.mean(matrix,axis=1))	
		print ("promedio ")	
		print (averages[-1])
		#Covarianza
		pre_covs_matrix.append(np.matrix(matrix - np.transpose(averages)) )
		print ("Covarianza ")
		print (pre_covs_matrix[-1])
		covariances.append(pre_covs_matrix[-1] * np.transpose(pre_covs_matrix[-1]) / N )
		print (covariances[-1])
		#Inversa
		inverses.append(np.linalg.inv(covariances[-1]))
		print ("Inversa ")
		print (inverses[-1])
		#Mahalanobis
		vecs_avers.append(np.matrix(vector - averages[-1]))
		print (vecs_avers[-1])
		mahalannobis.append(vecs_avers[-1] * inverses[-1] * np.transpose(vecs_avers[-1]))
		print (mahalannobis[-1])
		#Exponentes
		exps.append(math.exp(-.5 * mahalannobis[-1]))
		print (exps[-1])
		#Determinantes
		dets.append(np.linalg.det(covariances[-1]))
		print (dets[-1])
		#Resultados
		probabilitys.append((1/(2*math.pi*np.power(dets[-1],.5))) * exps[-1])
		print (probabilitys[-1])

		del averages[-1]

	for probability in probabilitys:
		print (probability)

	max_prob = max(probabilitys)
	class_num = probabilitys.index(max_prob) + 1
	print ("El vector pertenece a la clase: " + str(class_num))


	#Ploteo de clases y del vector
	figures.append(plt.scatter(vector[0], vector[1], color='b', marker='*', label="Vector"))
	plt.title("Grafica 4 clases")
	plt.xlabel("Eje x")
	plt.ylabel("Eje y")
	plt.legend(handles=figures, loc=4, fontsize=8)
	plt.show()

if __name__ == '__main__':
	main()