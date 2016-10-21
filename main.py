#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from generic import generic_functions
from classifiers import k_nearest_neighbors
import numpy as np
from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
import Image, ImageTk


class Frames(object):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.n_class = StringVar()
        self.n_repres = StringVar()
        self.k = StringVar()
        self.create = StringVar()
        self.type_ent = StringVar()
        self.centers = list()

    def main_frame(self):
        root.title("Reconocimiento de patrones")
        menubar = Menu(root)

        # display the menu
        root.config(menu=menubar)
        # Menu de clasificadores
        classifiers_ = Menu(menubar, tearoff=0)
        classifiers_.add_command(label="Distancia minima", command=self.distan)
        classifiers_.add_command(label="Maxima probabilidad", command=self.proba)
        classifiers_.add_command(label="Distancia Mahalanobis", command=self.maha)
        classifiers_.add_command(label="knn", command=self.knn)
        menubar.add_cascade(label="Clasificadores", menu=classifiers_)
        menubar.add_command(label="Salir", command=root.quit)

        self.mainframe.grid(column=1, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        param_frame = ttk.Frame(root, padding="3 3 12 12")
        param_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(param_frame, text="Parámetros actuales", font=("Helvetica", 16)).grid(column=1, row=2, sticky=N)
        self.n_class_label = ttk.Label(param_frame, text="Número de clases: ")
        self.n_class_label.grid(column=1, row=3, sticky=W)
        ttk.Label(param_frame, text="Vector: ").grid(column=1, row=4, sticky=W)
        param_button = ttk.Button(param_frame, text="Cambiar Parámetros", command=self.change_param_frame)
        param_button.grid(column=1, row=6, sticky=W)
        vector_button = ttk.Button(param_frame, text="Elegir vector")
        vector_button.grid(column=2, row=6, sticky=W)

        #self.image = Canvas(self.mainframe, width=200, height=150, borderwidth=1, relief=SUNKEN)
        #self.image.grid(column=0, row=1, sticky=(N, W))
        ttk.Button(self.mainframe, text="Seleccionar imagen", command=self.provide_img).grid(column=0, row=0, sticky=E)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=2, pady=2)

        #root.bind('<Return>', self.calculate)

    def change_param_frame(self):
        change_frame = Toplevel()
        change_frame.title("Modificaciones")
        ttk.Label(change_frame, text="Cambio de parámetros", font=("Helvetica", 16)).grid(column=1, row=1)
        ttk.Label(change_frame, text="Número de clases: ").grid(column=1, row=4, sticky=E)
        ttk.Label(change_frame, text="Número de representantes: ").grid(column=1, row=5, sticky=E)
        ttk.Label(change_frame, text="k: ").grid(column=1, row=6, sticky=E)
        ttk.Label(change_frame, text="Crear clases: ").grid(column=1, row=7, sticky=E)
        ttk.Label(change_frame, text="Tipo de entrada: ").grid(column=1, row=8, sticky=E)

        n_class_entry = ttk.Entry(change_frame, width=1, textvariable=self.n_class)
        n_class_entry.grid(column=2, row=4, sticky=(W, E))
        n_repres_entry = ttk.Entry(change_frame, width=1, textvariable=self.n_repres)
        n_repres_entry.grid(column=2, row=5, sticky=(W, E))
        k_entry = ttk.Entry(change_frame, width=1, textvariable=self.k)
        k_entry.grid(column=2, row=6, sticky=(W, E))
        create_entry = ttk.Radiobutton(change_frame, text="Automática", variable=self.create, value=1)
        create_entry.grid(column=2, row=7, sticky=(W, E))
        create_entry = ttk.Radiobutton(change_frame, text="Manual", variable=self.create, value=2)
        create_entry.grid(column=3, row=7, sticky=(W, E))
        type_ent_entry = ttk.Radiobutton(change_frame, text="Automática", variable=self.type_ent, value=1)
        type_ent_entry.grid(column=2, row=8, sticky=(W, E))
        type_ent_entry = ttk.Radiobutton(change_frame, text="Por imagen", variable=self.type_ent, value=2)
        type_ent_entry.grid(column=3, row=8, sticky=(W, E))

        ttk.Button(
            change_frame, text="Aceptar", command=lambda: self.save_changes(change_frame)
        ).grid(column=2, row=10, sticky=W)
        ttk.Button(change_frame, text="Cancelar", command=change_frame.destroy).grid(column=3, row=10, sticky=W)
        for child in change_frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

        n_class_entry.focus()

    def save_changes(self, change_frame):
        print self.n_class.get()
        self.n_class_label.configure(text="Número de clases: "+self.n_class.get())
        root.update_idletasks()
        change_frame.destroy()

    def select_image(self, image):
        self.provide_img(root, image, self.centers, self.n_class.get())
        #root.update_idletasks()

    def provide_img(self):

        frame = Frame(self.mainframe, bd=2, relief=SUNKEN)
        frame.grid(column=0, row=1, sticky=(N, W))
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=E+W)
        yscroll = Scrollbar(frame)
        yscroll.grid(row=0, column=1, sticky=N+S)
        self.canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        xscroll.config(command=self.canvas.xview)
        yscroll.config(command=self.canvas.yview)
        #frame.pack(fill=BOTH, expand=1)

        File = askopenfilename(parent=self.mainframe, initialdir="C:/", title='Selecciona la imagen')
        if not File:
            print 'No se Selecciona archivo'
        else:
            im = Image.open(File)
            img = ImageTk.PhotoImage(im)
            prix = im.load()
            self.canvas.create_image(0, 0, image=img, anchor="nw")
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))

            def get_coords(event):
                self.centers.append(np.matrix(prix[event.x, event.y]))
                #numbers_centers = len(centers)
                # if numbers_centers == n_classes:
                # root.destroy()
                #    return

            self.canvas.bind("<Button 1>", get_coords)

    def distan(self):
        distance(c,vector)

    def distance(self, c, vector):
        pass

    def proba(self):
        #probability(c, vector)
        pass

    def probability(self, c,vector):
        pass

    def maha(self):
        #probability(c, vector)
        pass

    def mahalanobis(self, c,vector):
        pass

    def knn(self):
        w = Label(root, text="k:", font=("Helvetica", 16))
        w.pack()
        #w_text = e.get()
        kknn(c,vector,k)

    def kknn(self, c,vector,k):
        k_nearest_neighbors.main(c, vector, k)

if __name__ == '__main__':
    root = Tk()
    app = Frames()
    app.main_frame(root)
    root.mainloop()


