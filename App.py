import tkinter as tk
from Ventana_Eleccion import Ventana_Eleccion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Ancho y altura de la ventana
        ancho_ventana = 500
        alto_ventana = 300
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # Calcular la posición para centrar la self
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        # Establecer la posición de la ventana
        self.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x, y))
        self.title("Ta Te Ti")
        self.iconbitmap("imagenes/tateti_icono.ico")
        self.config(background="gray17")
        self.resizable(0, 0)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        Ventana_Eleccion(self).pack()


if __name__=="__main__":
    app = App()
    app.mainloop()