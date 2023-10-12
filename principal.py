import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from juego import *

print('librerias, leidas')

ventana = tk.Tk()
ventana.title("Interfaz Grafica")
ventana.geometry('400x500')

#comandos
def Imagen():
    img = Image.open('oros1.jpg')
    new_img = img.resize(300, 256)
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(ventana, Image = render)
    img1.Image = render
    img1.place(x = 18 ,y = 38)

def mensaje():
    salir = messagebox.askquestion("salir", "¿Desea salir de la interfaz?")
    if salir == 'yes':
        ventana.quit
        ventana.destroy()

boton = tk.Button(ventana, command = Imagen, text = "Pedir carta", height= 2, width= 28)
boton.place(x=100, y=350)

boton1 = tk.Button(ventana, command=mensaje, text = "salir", height= 2, width= 28)
boton1.place(x=100, y=458)

ventana.mainloop()

#j = Juego(MazoEspanol())
#j.iniciar_juego()
#j.jugar()
#j.valorar_juego()