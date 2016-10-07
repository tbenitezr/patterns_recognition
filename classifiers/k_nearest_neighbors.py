import matplotlib.pyplot as plt
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

def plot_2d(c, vector, n_cs):  
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    markers = [ 
                '.', ',', 'o',"v", "^", "<", ">", "1",
                "2", "3", "4", "8", "s", "p", "*", "h",
                "H", "+", "x", "D", "d", "|", "_", "TICKLEFT",  
                "TICKRIGHT", "TICKUP", "TICKDOWN", "CARETLEFT",
                "CARETRIGHT", "CARETUP", "CARETDOWN"
            ]
     
    plt.figure()
    figures = list() 
    cont = 0
    for matrix in c:
        cont += 1
        label_figure =  "Clase "+ str(cont)
        figures.append(plt.scatter(matrix[0], matrix[1], color=colors[cont], marker=markers[cont], label=label_figure))
    
    figures.append(plt.scatter(vector[0], vector[1], color='b', marker='*', label="Vector"))
    plt.title("Grafica " + str(n_cs) + " clases")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend(handles=figures, loc=4, fontsize=8)
    plt.show()

def main(
    c = [
        np.array([[1,3,1,2,3],[2,5,5,2,3]]),
        np.array([[6,6,7,8,8],[4,3,4,4,5]])
    ], vector=[4, 5], k = 3):
	
    print 'vector: {}'.format(vector)

    #Numero de columnas
    N = c[0].shape[1]
    n_cs = len(c)
    print n_cs
    print N

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
    plot_2d(c, vector, n_cs)
    return class_num

if __name__ == '__main__':
    print 'El vector pertenece a la clase {}'.format(main())