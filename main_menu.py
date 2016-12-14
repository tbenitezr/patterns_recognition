#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
# from generic import generic_functions
from classifiers import minimum_distance, maximum_probability, \
    mahalanobis_distance, k_nearest_neighbors
from projects import project
import numpy as np
from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
import Image, ImageTk


class Frames(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.root = root
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.n_class = IntVar()
        self.n_repres = StringVar()
        self.k = StringVar()
        self.create = StringVar()
        self.type_ent = StringVar()
        self.centers = list()
        self.vector = [-1, -1]

    def main_frame(self):
        root.title("Reconocimiento de patrones")
        menubar = Menu(self.root)

        # display the menu
        root.config(menu=menubar)
        # Menu de clasificadores
        classifiers_ = Menu(menubar, tearoff=0)
        classifiers_.add_command(label="Distancia minima", command=self.distan)
        classifiers_.add_command(label="Maxima probabilidad", command=self.proba)
        classifiers_.add_command(label="Distancia Mahalanobis", command=self.maha)
        classifiers_.add_command(label="knn", command=self.knn)
        menubar.add_cascade(label="Clasificadores", menu=classifiers_)
        # Menu de practicas
        excercices = Menu(menubar, tearoff=0)
        excercices.add_command(label="Distancia minima", command=self.distan)
        excercices.add_command(label="Maxima probabilidad", command=self.proba)
        excercices.add_command(label="Distancia Mahalanobis", command=self.maha)
        classifiers_.add_command(label="knn", command=self.knn)
        menubar.add_cascade(label="Prácticas", menu=excercices)
        menubar.add_command(label="Proyecto", command=self.project)
        menubar.add_command(label="Salir", command=self.root.quit)

        self.mainframe.grid(column=1, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        param_frame = ttk.Frame(self.root, padding="3 3 12 12")
        param_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(param_frame, text="Parámetros actuales", font=("Helvetica", 16)).grid(column=1, row=2, sticky=N)
        self.n_class_label = ttk.Label(param_frame, text="Número de clases: ")
        self.n_class_label.grid(column=1, row=3, sticky=W)
        self.n_repres_label = ttk.Label(param_frame, text="Número de representantes: ")
        self.n_repres_label.grid(column=1, row=4, sticky=W)
        self.vector_label = ttk.Label(param_frame, text="Vector: ")
        self.vector_label.grid(column=1, row=5, sticky=W)
        param_button = ttk.Button(param_frame, text="Cambiar Parámetros", command=self.change_param_frame)
        param_button.grid(column=1, row=6, sticky=W)
        vector_button = ttk.Button(param_frame, text="Elegir vector", command=self.get_vector)
        vector_button.grid(column=2, row=6, sticky=W)

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
        self.n_class_label.configure(text="Número de clases: %s" % self.n_class.get())
        self.n_repres_label.configure(text="Número de representantes: %s" % self.n_repres.get())
        root.update_idletasks()
        change_frame.destroy()

    def select_image(self, image):
        self.provide_img(root, image, self.centers, self.n_class.get())
        #root.update_idletasks()

    def get_coords(self, event):
        numbers_centers = len(self.centers)
        print("%s %s" % (numbers_centers, self.n_class.get()))  # ------------------------------------------------------
        if numbers_centers <= self.n_class.get():
            self.centers.append(np.matrix(self.prix[event.x, event.y]))
            self.canvas.create_oval(event.x, event.y, event.x, event.y, outline="red", fill="red", width=2)
            return

    def get_vector_coords(self, event):
        print("vector %s" % self.vector)  # ----------------------------------------------------------------------------
        if self.vector != [-1, -1]:
            self.canvas.delete(self.vector_draw)
        self.vector = np.matrix(self.prix[event.x, event.y])
        self.vector_draw = self.canvas.create_oval(
            event.x, event.y, event.x, event.y, outline="yellow", fill="yellow", width=2
        )
        self.vector_label.configure(text="vector: %s" % self.vector)
        root.update_idletasks()
        return

    def get_vector(self):
        self.canvas.bind("<Button 1>", self.get_vector_coords)

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
            self.im = Image.open(File)
            img = ImageTk.PhotoImage(self.im)
            self.prix = self.im.load()
            self.canvas.create_image(0, 0, image=img, anchor="nw")
            self.canvas.image = img
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))

            self.canvas.bind("<Button 1>", self.get_coords)

    def create_class(self, c, flag_img, n_classes, n_repr):
        centers = list()
        if flag_img == -1:
            print 'Centros '
            print self.centers
            dimention = self.centers[0].shape[1]
        else:
            dimention = input("Dimensión de los representantes: ")
        for i in range(n_classes):
            print 'Para la clase {} \n'.format(i + 1)
            dispersal = input("Dispersión: ")
            if flag_img != -1:
                center = list(map(int, raw_input("Centro separado por comas: ").split(", ")))
            else:
                pass
                print 'y Centro: {}'.format(self.centers[i])
            c.append(np.random.rand(dimention, n_repr) * dispersal + np.transpose(self.centers[i]))

    def distan(self):
        c = list()
        self.create_class(c, -1, self.n_class.get(), int(self.n_repres.get()))
        own = minimum_distance.main(c, self.vector)
        print ("Pertenece a la clase %s" % own)

    def proba(self):
        c = list()
        self.create_class(c, -1, self.n_class.get(), int(self.n_repres.get()))
        own = maximum_probability.main(c, self.vector)
        print ("Pertenece a la clase %s" % own)

    def maha(self):
        c = list()
        self.create_class(c, -1, self.n_class.get(), int(self.n_repres.get()))
        own = mahalanobis_distance.main(c, self.vector)
        print ("Pertenece a la clase %s" % own)

    def knn(self):
        c = list()
        self.create_class(c, -1, self.n_class.get(), int(self.n_repres.get()))
        own = k_nearest_neighbors.main(c, self.vector, int(self.k.get()))
        print ("Pertenece a la clase %s" % own)

    def project(self):
        root = Tk()
        app = project.Memorama(root)
        app.main_frame()
        root.mainloop()

if __name__ == '__main__':
    root = Tk()
    app = Frames(root)
    app.main_frame()
    root.mainloop()



