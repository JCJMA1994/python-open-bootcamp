# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje  como al principio.
# Al principio no tiene que haber una opción seleccionada.

from tkinter import *

root = Tk()
opcion = StringVar()
opcion.set(None)

monitor = Label()
monitor.pack()


def seleccionar_opcion():
    monitor.config(text="{}".format(opcion.get()))


def reset_opcion():
    opcion.set(None)
    monitor.config(text="")


Radiobutton(root,text="Pikachu", variable=opcion, value="Pikachu", command=seleccionar_opcion).pack(anchor=W)
Radiobutton(root,text="Charmander", variable=opcion, value="Charmander", command=seleccionar_opcion).pack(anchor=W)
Radiobutton(root,text="Squirtle", variable=opcion, value="Squirtle", command=seleccionar_opcion).pack(anchor=W)
Radiobutton(root,text="Bulbasaur", variable=opcion, value="Bulbasaur", command=seleccionar_opcion).pack(anchor=W)


Button(root, text="Reiniciar", command=reset_opcion).pack()


root.mainloop()