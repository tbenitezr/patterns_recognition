#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
import Image, ImageTk


class Memorama(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.root = root
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.n_players = IntVar()
        self.players = list()

    def main_frame(self):
        root.title("Memorama")
        menubar = Menu(self.root)

        # display the menu
        root.config(menu=menubar)
        menubar.add_command(label="Nueva partida", command=self.change_param_frame)
        menubar.add_command(label="Reiniciar partida", command=self.root.quit)
        menubar.add_command(label="Salir", command=self.root.quit)

        self.mainframe.grid(column=1, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # Configuration score frame
        self.score_frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.score_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.score_frame, text="Puntaje", font=("Helvetica", 16)).grid(column=1, row=2, sticky=N)
        ttk.Label(self.score_frame, text="Jugadores").grid(column=0, row=4)
        ttk.Label(self.score_frame, text="Score").grid(column=1, row=4)

        # Configuration game

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=2, pady=2)

    def change_param_frame(self):
        change_frame = Toplevel()
        change_frame.title("Nueva partida")

        ttk.Label(change_frame, text="Número de jugadores: ").grid(column=1, row=4, sticky=E)
        n_players_entry = ttk.Entry(change_frame, width=1, textvariable=self.n_players)
        n_players_entry.grid(column=2, row=4, sticky=(W, E))

        def key(event):
            player_name_l = list()
            puntaje = StringVar()
            puntaje.set("0")
            for n_player in range(1, self.n_players.get()+1, 1):
                player_info = list()
                player_name = StringVar()
                player_name_l.append(player_name)
                ttk.Label(change_frame, text="Jugador {} : ".format(n_player)).grid(column=1, row=4+n_player, sticky=E)
                player_name_entry = ttk.Entry(change_frame, width=1, textvariable=player_name)
                player_name_entry.grid(column=2, row=4+n_player, sticky=(W, E))

                player_info.append(player_name_l[n_player-1])
                player_info.append(puntaje)
                self.players.append(player_info)

        n_players_entry.bind("<Key>", key)

        ttk.Button(
            change_frame, text="Aceptar", command=lambda: self.save_changes(change_frame)
        ).grid(column=2, row=10, sticky=W)
        ttk.Button(change_frame, text="Cancelar", command=change_frame.destroy).grid(column=3, row=10, sticky=W)
        for child in change_frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

        n_players_entry.focus()

    def save_changes(self, change_frame):
        n_player = 0
        for player in self.players:
            n_player += 1
            for info in range(0, 2, 1):
                info_label = ttk.Label(self.score_frame, text=player[info].get())
                info_label.grid(column=info, row=5 * n_player)
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

    def project(self):
        pass

if __name__ == '__main__':
    root = Tk()
    app = Memorama(root)
    app.main_frame()
    root.mainloop()



