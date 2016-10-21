#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk, ttk
from PIL import Image


class Frames(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)

    def main(self):
        frame = Frame(root, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=E + W)
        yscroll = Scrollbar(frame)
        yscroll.grid(row=0, column=1, sticky=N + S)
        canvas = Canvas(
            frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set
        )
        canvas.grid(row=0, column=0, sticky=N + S + E + W)
        xscroll.config(command=canvas.xview)
        yscroll.config(command=canvas.yview)
        frame.pack(fill=BOTH, expand=1)

        File = askopenfilename(
            parent=root, initialdir="C:/", title='Selecciona la imagen'
        )
        if not File:
            print 'No se Selecciona archivo'
        else:
            im = Image.open(File)
            img = ImageTk.PhotoImage(im)
            prix = im.load()
            canvas.create_image(0, 0, image=img, anchor="nw")
            canvas.config(scrollregion=canvas.bbox(ALL))
            centers = list()

            def get_coords(event):
                print (event.x, event.y)
                centers.append(prix[event.x, event.y])
                # n_c = input("Num class: ")
                # for i in range(n_c):

            canvas.bind("<Button 1>", get_coords)

if __name__ == "__main__":
    root = Tk()
    app = Frames()
    app.main(root)
    root.mainloop()
