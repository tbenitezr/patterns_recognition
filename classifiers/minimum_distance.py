# from __future__ import absolute_import
# from generic import generic_functions
import numpy as np
import cmath as math


def main(
        c=[
            np.array([[1, 3, 1, 2, 3], [2, 5, 5, 2, 3]]),
            np.array([[6, 6, 7, 8, 8], [4, 3, 4, 4, 5]])
        ], vector=[4, 5]):

    print 'vector: {}'.format(vector)

    # Numero de columnas
    N = c[0].shape[1]
    print N

    averages = list()
    vecs_avers = list()
    distances = list()
    cont = 0

    for matrix in c:
        cont += 1
        print ("Matriz ")
        print (matrix)
        # Obtener media
        averages.append(np.mean(matrix, axis=1))
        print ("promedio ")
        print (averages)

        vecs_avers.append(np.matrix(vector - np.transpose(averages[-1])))
        print ("vector - media %s" % vecs_avers[-1])

        # Obtener la distancia
        suma = 0
        print("jjj")
        for elto in vecs_avers[-1].A1:
            suma += elto * elto
        print ("suma %s" % suma)

        distances.append(np.real(math.sqrt(suma)))

        del averages[-1]

    print ("Distancias Mahalanobis")
    for distance in distances:
        print (distance)

    min_distance = min(distances)
    class_num = distances.index(min_distance) + 1
    return class_num


if __name__ == '__main__':
    c = [np.array([
        [27.02833724,  27.02292762,  27.33829558,  27.25872837,  28.60016858],
        [33.7201039,   33.63977915,  33.7586533,   32.40957152,  32.47295543],
        [28.06708081, 29.64821501, 29.73648303, 29.42754543, 28.5391679]]),
         np.array([
             [257.89821957,  255.58272568,  255.69955529,  257.88398161,  255.5505837],
             [250.97758644,  250.8465722,   250.106021,    251.19742626,  251.81396379],
             [252.24690301,  251.22753931,  251.25288564,  252.77040072,  251.46020036]
         ])
    ]
    vector = [252, 250, 255]
    print 'El vector pertenece a la clase {}'.format(main(c, vector))
