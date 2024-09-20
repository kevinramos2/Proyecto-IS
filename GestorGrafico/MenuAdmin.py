import tkinter as tk
from tkinter import *

class MenuAdmin(Frame):
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
        mensajeBienv.pack(side="left")

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

        # Frame que va a contener todas las funcionalidades del Administrador
        self.FrameFuncionalidades = Frame(self, height= 400, width= 500, bg="#415A77")
        self.FrameFuncionalidades.pack_propagate(False)
        self.FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)

        # Definimos funciones para cada botón
        def abrirInventario():
            self.mostrarNuevoFrame("Inventario", ["Producto 1", "Producto 2", "Producto 3"])

        def verReporteVentas():
            self.mostrarNuevoFrame("Reporte de Ventas", ["Total Ventas: 5000", "Ventas de Hoy: 300"])

        def enviarMensaje():
            self.mostrarNuevoFrame("Enviar Mensaje", ["Escribe tu mensaje aquí:"])

        def revisarMensaje():
            self.mostrarNuevoFrame("Revisar Mensaje", ["Mensaje 1: Hola", "Mensaje 2: Buenas"])

        # Botones de funcionalidades
        botonInventario = Button(
            self.FrameFuncionalidades, 
            text="Inventario",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=abrirInventario)
        
        botonInventario.pack(fill="x", side="top",expand=True, padx= 5)

        botonReportes = Button(
            self.FrameFuncionalidades, 
            text="Reporte de Ventas",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=verReporteVentas)
        
        botonReportes.pack(fill="x", side="top",expand=True, padx=5)

        botonEnviar = Button(
            self.FrameFuncionalidades, 
            text="Enviar Mensaje",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=enviarMensaje)
        
        botonEnviar.pack(fill="x", side="top",expand=True, padx=5)

        botonRevisar = Button(
            self.FrameFuncionalidades, 
            text="Revisar Mensaje",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=revisarMensaje)
        
        botonRevisar.pack(fill="x", side="top",expand=True, padx=5)

    def mostrarNuevoFrame(self, titulo, contenido):
        # Elimina el frame de funcionalidades actual
        self.FrameFuncionalidades.pack_forget()

        # Crear un nuevo frame para la funcionalidad seleccionada
        nuevoFrame = Frame(self, bg="#1B263B")
        nuevoFrame.pack(fill="both", expand=True)

        # Mostrar el título de la funcionalidad
        tituloLabel = Label(nuevoFrame, text=titulo, font=("Arial", 25, "bold"), bg="#1B263B", fg="white")
        tituloLabel.pack(pady=10)

        # Añadir el contenido de la funcionalidad
        for item in contenido:
            contenidoLabel = Label(nuevoFrame, text=item, font=("Arial", 15), bg="#1B263B", fg="white")
            contenidoLabel.pack(pady=5)

        # Añadir botón para volver al menú principal
        botonVolver = Button(nuevoFrame, text="Volver", bg="#E0E1DD", font=("Arial", 15), command=lambda: self.volverMenu(nuevoFrame))
        botonVolver.pack(pady=10)

    def volverMenu(self, frameActual):
        # Destruir el frame actual
        frameActual.pack_forget()

        # Volver a mostrar el frame de funcionalidades
        self.FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)
