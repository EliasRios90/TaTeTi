import tkinter as tk
from PIL import Image, ImageTk

from TaTeTi import TaTeTi

class Ventana_Eleccion(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.raiz = raiz
        self.config(background="gray17")

        tk.Label(self, 
            background="gray17",
            text="Elija un símbolo", 
            fg="orange",
            font=("Cooper Black", 34, "bold", "underline")).pack(pady=50)
        
        self.imagen_x = ImageTk.PhotoImage(Image.open("imagenes/letra-chica-x.png"))
        boton_x = tk.Button(self,
            background="gray17",
            image=self.imagen_x,
            relief=tk.GROOVE,
            bd=5,
            command=lambda: self.__set_eleccion("x"))
        boton_x.pack(padx=(100, 0), side=tk.LEFT, ipadx=20, ipady=5)
        
        self.imagen_o = ImageTk.PhotoImage(Image.open("imagenes/letra-chica-o.png"))
        boton_o = tk.Button(self,
            background="gray17",
            image=self.imagen_o,
            relief=tk.GROOVE,
            bd=5,
            command=lambda : self.__set_eleccion("o"))
        boton_o.pack(padx=(0, 100), side=tk.RIGHT, ipadx=20, ipady=5)
        
        # Eventos de mouse
        boton_x.bind("<Enter>", lambda evento: evento.widget.config(bg="white"))
        boton_x.bind("<Leave>", lambda evento: evento.widget.config(bg="gray17"))
        boton_o.bind("<Enter>", lambda evento: evento.widget.config(bg="white"))
        boton_o.bind("<Leave>", lambda evento: evento.widget.config(bg="gray17"))
    
    def __set_eleccion(self, simbolo):
        TaTeTi(self.raiz, simbolo).pack()
        self.destroy()