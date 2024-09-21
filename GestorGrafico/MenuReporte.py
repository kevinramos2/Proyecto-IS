import tkinter as tk
from tkinter import *

class MenuReporte(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.ventana = ventana
        self.empleado = empleado

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        LabelFrame.pack(side="top", fill="x")

        mensaje = "Menu De Reportes"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "italic underline"),bg="#1B263B" , fg = "white")
        mensajeBienv.pack(side="left", padx=2)

        def volverAlMenu():
            from GestorGrafico.MenuAdmin import MenuAdmin
            self.destroy()
            MenuAdmin(self.ventana,self.empleado)


        # Boton para volver al menu principal
        ImagenHome = "BaseDeDatos\Imagenes\home-solid-36.png"
        foto = tk.PhotoImage(file=ImagenHome)

        MenuPrincipalBoton = Button(LabelFrame, image=foto, command=volverAlMenu)
        MenuPrincipalBoton.image = foto
        MenuPrincipalBoton.pack(side="right")

        # Frame que va a contener todas las funcionalidades del Administrador
        FrameFuncionalidades = Frame(self, height= 400, width= 500, bg="#415A77")
        FrameFuncionalidades.pack_propagate(False)
        FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)

        # Botones de funcionalidades
        botonReporteVenta = Button(
            FrameFuncionalidades, 
            text="Reporte Ventas Diarias",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2)
        
        botonReporteVenta.pack(fill="x", side="top",expand=True, padx= 5)

        # Botones de funcionalidades
        botonReporteGasto = Button(
            FrameFuncionalidades, 
            text="Reporte Gastos diarios",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2)
        
        botonReporteGasto.pack(fill="x", side="top",expand=True, padx= 5)