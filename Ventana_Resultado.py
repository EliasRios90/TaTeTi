import tkinter as tk

class Ventana_Resultado(tk.Toplevel):
    def __init__(self, simbolo):
        super().__init__()

        # ancho y la altura de la ventana TopLevel
        ancho_top_level = 300
        alto_top_level = 110
        # centro la ventana a la pantalla
        x_pos = int(self.winfo_screenwidth() / 2 - ancho_top_level / 2)
        y_pos = int(self.winfo_screenheight() / 2 - alto_top_level / 2)
        self.geometry("{}x{}+{}+{}".format(ancho_top_level, alto_top_level, x_pos, y_pos))

        self.title("Ta Te Ti")
        self.config(background="white", relief=tk.SUNKEN, bd=8)
        self.resizable(0, 0)
        self.overrideredirect(True)  # Ocultar botones de ventana

        label_resultado = tk.Label(self, font=("Cooper Black", 28, "bold"), bg="white")
        label_resultado.pack(padx=20, pady=30)
        if simbolo=="x":
            label_resultado.configure(text="GANASTE!!!", fg="lime")
        elif simbolo=="o":
            label_resultado.configure(text="PERDISTE!!!", fg="red")
        else:
            label_resultado.configure(text="EMPATE!!!", fg="orange")
        
