import tkinter as tk
from tkinter import *

class MenuReporte(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.ventana = ventana

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        LabelFrame.pack(side="top", fill="x")

        mensaje = "Menu De Reportes"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "italic underline"),bg="#1B263B" , fg = "white")
        mensajeBienv.pack(side="left", padx=2)

        # Boton para volver al menu principal
        ImagenHome = "BaseDeDatos\Imagenes\home-solid-36.png"
        MenuPrincipalBoton = Button(LabelFrame, image=ImagenHome)
        MenuPrincipalBoton.pack(side="right", padx=2)