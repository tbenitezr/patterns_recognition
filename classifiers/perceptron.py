# from __future__ import absolute_import
# from generic import generic_functions
import numpy as np
import cmath as math


def main(c, vector, peso_sinap, factor_correc):
    n_repre = c[0].shape[1]  # Representantes
    w = np.ones(n_repre) * peso_sinap

def interation(rep, w):
    



if __name__ == '__main__':
    c = [
        np.array([0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0]),
        np.array([0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1])
    ]
    vector = []
    peso_sinap = 1
    factor_correc = 1
    print 'El vector pertenece a la clase {}'.format(main(c, vector, peso_sinap, factor_correc))