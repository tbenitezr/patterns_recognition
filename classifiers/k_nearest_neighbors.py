#from __future__ import absolute_import
#from generic import generic_functions
import numpy as np
import cmath as math 

class Distancias:
    def __init__(self, clase, elemento, distancia):
        self.clase = clase
        self.elemento = elemento
        self.distancia = distancia
    def __cmp__(self, other):
        if self.distancia < other.distancia:
            return -1
        elif self.distancia > other.distancia:
            return 1
        else:
            return 0
    def __str__(self):
        return str(self.distancia)

def main(
    c = [
        np.array([[1,3,1,2,3],[2,5,5,2,3]]),
        np.array([[6,6,7,8,8],[4,3,4,4,5]])
    ], vector=[4, 5], k = 3):
	
    print 'vector: {}'.format(vector)

    #Numero de columnas
    N = c[0].shape[1] #Representantes
    n_cs = len(c) #Clases

    distances = list()
    n_class = 0
    e = 0

    for matrix in c:
        #Obtener la distacia del vector a cada representante
        trans = np.transpose(matrix)
        dif = vector - trans
        cuad = np.matrix(dif) * np.matrix(np.transpose(dif))
        diag = cuad.diagonal()
        diag_trans = np.transpose(diag)
        n_class += 1
        elem = 0
        for elto in diag_trans:
            elem += 1
            raiz = math.sqrt(elto)
            elem_distance = Distancias(n_class, elem, raiz.real)
            distances.append(elem_distance)

    distances.sort()
    lista_clases = list(map(lambda distan: distan.clase, distances))
    probabilitys = list()
    for dist_by_class in range(1, n_cs+1, 1):
        probability = lista_clases[:k].count(dist_by_class) / k
        probabilitys.append(probability)

    max_prob = max(probabilitys)
    class_num = probabilitys.index(max_prob) + 1

    #Ploteo de clases y del vector
    #generic_functions.plot_2d(c, vector, n_cs)
    return class_num

if __name__ == '__main__':
    print 'El vector pertenece a la clase {}'.format(main())