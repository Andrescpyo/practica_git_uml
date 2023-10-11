import tkinter as tk
from tkinter import *

from tkinter import messagebox
from juego import *

print('librerias, leidas')

ventana = tk.Tk()
ventana.title("Interfaz Grafica")
ventana.geometry('400x500')


boton = tk.Button(ventana, command = imagen, text = "Pedir carta", height= 2, width= 28)
boton.place(x=100, y=350)

boton = tk.Button(ventana, text = "salir", height= 2, width= 28)
boton.place(x=100, y=458)

#comandos
def Imagen():
    img = Image.open('sprites\española\oros\1.jpg')
    new_img = img.resize(300, 256)
    render = ImageTk.PhotoImage(new_img)
    img1 = label(ventana, Image = render)
    img1.image = render
    img1.place(x = 18 ,y = 38)

def mensaje():
    salir = messagebox.askquestion("salir", "¿Desea salir de la interfaz?")
    if salir == 'yes':
        ventana.quit
        ventana.destroy()
        
    imagen1 = Button (ventana,text="Imagen",command=Imagen).grid(row=7, columnspan=9 )

ventana.mainloop()

#j = Juego(MazoEspanol())
#j.iniciar_juego()
#j.jugar()
#j.valorar_juego()