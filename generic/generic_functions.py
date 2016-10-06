#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk
from PIL import Image
import numpy as np

def create_class(c, flag_img):
    n_classes = input("Ingrese el número de clases: ") 
    n_repr = input("Número de representantes: ")
    centers = list()
    if flag_img == -1:
        provide_img(centers, n_classes) 
        dimention = centers[0].shape[1]
        print centers[0]
        print dimention
    else:
        dimention = raw_input("Dimensión de los representantes: ")
    for i in range(n_classes):
        print 'Para la clase {} \n'.format(i+1)
        dispersal = input("Dispersión: ")
        if flag_img != -1:
            center = list(map(int,raw_input("Centro separado por comas: ").split(", "))) 
        else:
            print 'y Centro: {}'.format(centers[i])
        c.append(np.transpose(np.random.rand(dimention,n_repr) * dispersal) + np.transpose(centers[i]))
    print c

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
            #print (event.x,event.y)}
            print len(centers)
            if len(centers) != n_classes :
                print 'elementos centros {}'.format(len(centers))
                centers.append(np.matrix(prix[event.x,event.y]))
                print centers
            else:
                root.destroy()
                return 
        canvas.bind("<Button 1>",get_coords)

        root.mainloop()
    

if __name__ == "__main__":
    c = list()
    create_class(c, -1)
