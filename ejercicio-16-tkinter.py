# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

from tkinter import *

root = Tk()
elemento = StringVar()
list_box = Listbox(root)

list_element = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]

for item in list_element:
    list_box.insert(END, item)


list_box.pack()
label = Label(text="Lista de Pokemones")
label.pack()

root.mainloop()