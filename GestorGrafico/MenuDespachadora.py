import tkinter as tk
from tkinter import *


class MenuDespachadora(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.empleado = empleado
        self.ventana = ventana

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        LabelFrame.pack(side="top", fill="x")

        mensaje = f"Bienvenido de vuelta {self.empleado.getNombre()}"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "italic underline"),bg="#1B263B" , fg = "white")
        mensajeBienv.pack(side= "left")

        def cerrarSesion():
            from GestorGrafico.LogInGrafico import LogInGrafico
            self.destroy()
            LogInGrafico(self.ventana)

        # Barra del Menu
        menuBar = Menu(self.ventana)
        self.ventana.option_add("*tearOff", False)
        self.ventana.config(menu=menuBar)

        # Menu para salir 
        menuSalir = Menu(menuBar)
        menuBar.add_cascade(label="Salir", menu=menuSalir, activebackground="#415A77")

        menuSalir.add_cascade(label="Salir de la aplicacion", activebackground="#415A77", command=self.ventana.destroy)
        menuSalir.add_cascade(label="Cerrar Sesion", activebackground="#415A77",command=cerrarSesion)


        # Frame 
        LaberFuncionalidades = Frame(self, height= 400, width= 500, bg="#415A77")
        LaberFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)