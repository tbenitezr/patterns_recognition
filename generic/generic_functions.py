#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def plot_2d(classes, vector, n_cs):  
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

    for matrix in classes:
        cont += 1
        label_figure =  "Clase "+ str(cont)
        figures.append(plt.scatter(matrix[0], matrix[1], color=colors[cont], marker=markers[cont], label=label_figure))
    
    figures.append(plt.scatter(vector[0], vector[1], color='b', marker='*', label="Vector"))
    plt.title("Grafica " + str(n_cs) + " clases")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend(handles=figures, loc=4, fontsize=8)
    plt.show()

def create_class(c, flag_img, 
    n_classes = input("Ingrese el número de clases: "),
    n_repr = input("Número de representantes: ")
    ):
    centers = list()
    if flag_img == -1:
        provide_img(centers, n_classes)
        print 'Centros '
        print centers         
        dimention = centers[0].shape[1]
    else:
        dimention = input("Dimensión de los representantes: ")
    for i in range(n_classes):
        print 'Para la clase {} \n'.format(i+1)
        dispersal = input("Dispersión: ")
        if flag_img != -1:
            center = list(map(int,raw_input("Centro separado por comas: ").split(", "))) 
        else:
            pass
            print 'y Centro: {}'.format(centers[i])
        c.append(np.random.rand(dimention,n_repr) * dispersal + np.transpose(centers[i]))


def provide_img(centers, n_classes):
    root = Tk()

    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)
    
    File = askopenfilename(parent=root, initialdir="C:/",title='Selecciona la imagen')
    if not File:
        print 'No se Selecciona archivo'
    else:
        im = Image.open(File)
        img = ImageTk.PhotoImage(im)
        prix = im.load()
        canvas.create_image(0,0,image=img,anchor="nw")
        canvas.config(scrollregion=canvas.bbox(ALL))
        
        def get_coords(event):
            centers.append(np.matrix(prix[event.x,event.y]))            
            numbers_centers = len(centers)
            if  numbers_centers == n_classes :
                root.destroy()
                return 
        canvas.bind("<Button 1>",get_coords)

        root.mainloop()
    

if __name__ == "__main__":
    c = list()
    create_class(c, -1, 2, 5)
    vector = [20,5,-17]
    plot_2d(c, vector, 2)
