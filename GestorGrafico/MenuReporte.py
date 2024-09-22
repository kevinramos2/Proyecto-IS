import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from GestorAplicacion.ReporteVentaDiario import ReporteDeVentas
from GestorAplicacion.Gasto import Gasto
from BaseDeDatos.serializador import Serializador



class MenuReporte(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.ventana = ventana
        self.empleado = empleado

        def cerrarSesion():
            from GestorGrafico.LogInGrafico import LogInGrafico
            self.destroy()
            LogInGrafico(self.ventana)
        
        def cerrarAplicacion():
            Serializador.Serializar()
            self.ventana.destroy()


        # Barra del Menu
        menuBar = Menu(self.ventana)
        self.ventana.option_add("*tearOff", False)
        self.ventana.config(menu=menuBar)

        # Menu para salir 
        menuSalir = Menu(menuBar)
        menuBar.add_cascade(label="Salir", menu=menuSalir, activebackground="#415A77")

        menuSalir.add_cascade(label="Salir de la aplicacion", activebackground="#415A77", command=cerrarAplicacion)
        menuSalir.add_cascade(label="Cerrar Sesion", activebackground="#415A77",command=cerrarSesion)

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
        ImagenHome = "BaseDeDatos/Imagenes/home-solid-36.png"
        foto = tk.PhotoImage(file=ImagenHome)

        MenuPrincipalBoton = Button(LabelFrame, image=foto, command=volverAlMenu)
        MenuPrincipalBoton.image = foto
        MenuPrincipalBoton.pack(side="right")

        # Frame que va a contener todas las funcionalidades del menu reporte
        FrameFuncionalidades = Frame(self, height= 400, width= 500, bg="#415A77")
        FrameFuncionalidades.pack_propagate(False)
        FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)

        

        # Funciones para cada boton

        def AbrirReporteVentas():
            from GestorGrafico.LogInGrafico import LogInGrafico
            if (LogInGrafico.Caja_Cerrada):
                ventana_Reporte = Toplevel(self.ventana)
                ventana_Reporte.title("Reporte de venta")
                ventana_Reporte.geometry("400x500")

                reporteDeVentas = ReporteDeVentas()

                # Frame titulo y fecha actual
                LabelFrame = Frame(ventana_Reporte, height=100, bg="#1B263B", padx=5, pady=5)
                LabelFrame.pack(side="top", fill="x")

                fechaActual = datetime.now().strftime('%Y-%m-%d')
                mensaje = f"Reporte de ventas del dia {fechaActual}"

                mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 15, "italic underline"),bg="#1B263B" , fg = "white")
                mensajeBienv.pack(side="left", padx=2)

                #Generar todo el frame del reporte
                reporteDeVentas.generar_Reporte_diario_tkinter(ventana_Reporte)
            else:
                messagebox.showerror("Error en Reportes", "No se puede acceder al reporte diario sin antes cerrar caja.")

        def AbrirGastos():
            ventana_Gastos =  Toplevel(self.ventana)
            ventana_Gastos.title("Gastos")
            ventana_Gastos.geometry("400x500")

            # Frame titulo 
            LabelFrame = Frame(ventana_Gastos, height=100, bg="#1B263B", padx=5, pady=5)
            LabelFrame.pack(side="top", fill="x")

            mensaje = "Gastos"

            mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 15, "italic underline"),bg="#1B263B" , fg = "white")
            mensajeBienv.pack(side="left", padx=2)

            Gasto.generar_gastos_tkinter(ventana_Gastos)

            


        # Botones de funcionalidades
        botonReporteVenta = Button(
            FrameFuncionalidades, 
            text="Reporte Ventas del dia",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=AbrirReporteVentas)
        
        botonReporteVenta.pack(fill="x", side="top",expand=True, padx= 5)

        # Botones de funcionalidades
        botonReporteGasto = Button(
            FrameFuncionalidades, 
            text="Gastos",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=AbrirGastos)
        
        botonReporteGasto.pack(fill="x", side="top",expand=True, padx= 5)

