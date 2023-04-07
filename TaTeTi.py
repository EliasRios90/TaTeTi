import tkinter as tk
import random
from PIL import Image, ImageTk

from Ventana_Resultado import Ventana_Resultado

class TaTeTi(tk.Frame):
    def __init__(self, raiz, simbolo):
        super().__init__(raiz)
        self.raiz = raiz
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.tablero = [["-" for _ in range(3)] for _ in range(3)]
        self.ranking = {"ganados":0, "perdidos":0, "empates":0}

        # Ancho y altura de la ventana
        ancho_ventana = 500
        alto_ventana = 600
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.raiz.winfo_screenwidth()
        alto_pantalla = self.raiz.winfo_screenheight()

        # Calcular la posición para centrar la self
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        # Establecer la posición de la ventana
        self.raiz.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x, y))
        self.config(background="gray17")
        
        tk.Label(self, 
            text="¡A JUGAR!", 
            activebackground="goldenrod",
            background="gray17", 
            foreground="orange", 
            font=("Cooper Black", 34, "bold")).pack(pady=(10, 15))
        
        if simbolo=="x":
            #self.usuario = ImageTk.PhotoImage(Image.open("imagenes/letra-x.png"))
            self.usuario = tk.PhotoImage(file="imagenes\letra-x.png")
            self.maquina = ImageTk.PhotoImage(Image.open("imagenes/letra-o.png"))
        else:
            self.usuario = ImageTk.PhotoImage(Image.open("imagenes/letra-o.png"))
            self.maquina = ImageTk.PhotoImage(Image.open("imagenes/letra-x.png"))
        
        self.imagen_fondo = ImageTk.PhotoImage(Image.open("imagenes/abstracto.png"))
        
        self.__crear_tablero()
        self.__frame_ranking()
        
    
    
    ##########################################################################################

    
    def __crear_tablero(self):
        self.frame_juego = tk.Frame(self)
        self.frame_juego.pack();

        for i in range(3):
            for j in range(3):
                boton = tk.Label(self.frame_juego,
                    background="khaki",
                    relief=tk.GROOVE,
                    bd=10,
                    cursor="hand2",
                    image=self.imagen_fondo)
                boton.bind("<Button-1>", lambda evento, i=i, j=j: self.__seleccion_usuario(evento, i, j))
                boton.bind("<Enter>", lambda evento, i=i, j=j: self.__al_entrar(evento, i, j))
                boton.bind("<Leave>", lambda evento, i=i, j=j: self.__al_salir(evento, i, j))
                boton.grid(row=i, column=j)
                
                self.botones[i][j] = boton
    


    def __seleccion_usuario(self, evento, fila, columna):
        if self.tablero[fila][columna]!="x" and self.tablero[fila][columna]!="o":
            evento.widget.configure(image=self.usuario)
            evento.widget.configure(background="yellow")
            evento.widget.configure(cursor="arrow")
            self.tablero[fila][columna] = "x"
            self.__seleccion_maquina()

    
    
    def __seleccion_maquina(self):
        if not self.__jugadas():

            while True:# Selecciono al azar una posicion en el tablero
                fila_azar = random.randint(0, 2)
                columna_azar = random.randint(0, 2)
                if self.tablero[fila_azar][columna_azar]=="-":
                    self.botones[fila_azar][columna_azar].configure(image=self.maquina)
                    self.botones[fila_azar][columna_azar].configure(background="white")
                    self.botones[fila_azar][columna_azar].configure(cursor="arrow")
                    self.tablero[fila_azar][columna_azar] = "o"
                    break
            self.__comprobar_ganador()
        
        elif self.__jugadas():
            if self.__comprobar_ganador()==None:
                self.__actualizar_ranking("empates")
                self.__mostrar_resultado("-")
                self.__reiniciar_tablero()
                
    

    def __comprobar_ganador(self):
        auxiliar = None
        # comprobando filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != "-":
                auxiliar = fila[0]
        # comprobando columnas
        for i in range(3):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != "-":
                auxiliar = self.tablero[0][i]
        # comprobando diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != "-":
            auxiliar = self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != "-":
            auxiliar = self.tablero[0][2]        
        
        if auxiliar!=None:
            if auxiliar=="x":
                self.__actualizar_ranking("ganados")
                self.__mostrar_resultado("x")
                self.__reiniciar_tablero()
            else:
                self.__actualizar_ranking("perdidos")
                self.__mostrar_resultado("o")
                self.__reiniciar_tablero()
        
        return auxiliar
    
    
    
    def __jugadas(self):
        # devuelve la cantidad de "x" que tiene la tabla
        contX = sum(1 for fila in self.tablero for elemento in fila if elemento=="x")
        return (contX==5) # Numero maximo de clicks que puede hacer el usuario

    
    
    def __reiniciar_tablero(self):
        for i in range(3):
            for j in range(3):
                self.botones[i][j].configure(image=self.imagen_fondo)
                self.botones[i][j].configure(state=tk.NORMAL)
                self.botones[i][j].configure(background="khaki")
                self.botones[i][j].configure(cursor="hand2")
                self.tablero[i][j] = "-"
    


    def __mostrar_resultado(self, simbolo):
        resultado = Ventana_Resultado(simbolo)
        resultado.after(1000, resultado.destroy)
    


    def __frame_ranking(self):
        frame = tk.Frame(self, background="dodgerblue")
        frame.pack(pady=20)
        frame_ganadas = tk.Frame(frame)
        self.ganados = tk.Label(frame_ganadas, text="Ganados: 0", font=("Verdana", 10, "bold"), background="dodgerblue", foreground="white")
        self.ganados.pack() # COLOCAR pack() POR SEPARADO PARA QUE FUNCIONE LA ACTUALIZACION DEL LABEL
        frame_ganadas.pack(padx=10, side=tk.LEFT)
        frame_perdidas = tk.Frame(frame)
        self.perdidos = tk.Label(frame_perdidas, text="Perdidos: 0", font=("Verdana", 10, "bold"), background="dodgerblue", foreground="white")
        self.perdidos.pack()
        frame_perdidas.pack(padx=40, side=tk.LEFT)
        frame_empates = tk.Frame(frame)
        self.empates = tk.Label(frame_empates, text="Empates: 0", font=("Verdana", 10, "bold"), background="dodgerblue", foreground="white")
        self.empates.pack()
        frame_empates.pack(padx=10, side=tk.LEFT)
    


    def __actualizar_ranking(self, nombre):
        if nombre=="ganados": 
            self.ranking[nombre] += 1
            self.ganados["text"] = "Ganados: " + str(self.ranking["ganados"])
        elif nombre=="perdidos": 
            self.ranking[nombre] += 1
            self.perdidos["text"] = "Perdidos: " + str(self.ranking["perdidos"])
        else: 
            self.ranking[nombre] += 1
            self.empates["text"] = "Empates: " + str(self.ranking["empates"])
        
            

    def __al_entrar(self, evento, fila, columna):
        if self.tablero[fila][columna]!="x" and self.tablero[fila][columna]!="o":
            evento.widget.configure(background="palegreen")
    
    
    
    def __al_salir(self, evento, fila, columna):
        if self.tablero[fila][columna]!="x" and self.tablero[fila][columna]!="o":
            evento.widget.configure(background="khaki")
