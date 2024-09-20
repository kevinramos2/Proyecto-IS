import tkinter as tk
from tkinter import *

class MenuDespachadora(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both", expand=True)
        self.empleado = empleado
        self.ventana = ventana

        # Frame para el Mensaje de Bienvenida
        label_frame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        label_frame.pack(side="top", fill="x")

        mensaje = f"Bienvenido de vuelta {self.empleado.getNombre()}"
        mensaje_bienv = Label(
            label_frame,
            text=mensaje,
            font=("arial", 20, "italic underline"),
            bg="#1B263B",
            fg="white"
        )
        mensaje_bienv.pack(side="left")

        # Función para cerrar sesión
        def cerrarSesion():
            from GestorGrafico.LogInGrafico import LogInGrafico
            self.destroy()
            LogInGrafico(self.ventana)

        # Función para abrir caja
        def abrirCaja():
            # Destruir la ventana principal
            self.destroy()

            # Crear una nueva ventana emergente para la caja
            caja_ventana = Toplevel(self.ventana)
            caja_ventana.title("Caja")
            caja_ventana.geometry("400x300")
            caja_ventana.config(bg="#F0F0F0")
            caja_ventana.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilitar el botón de cerrar de la ventana

            # Etiqueta indicativa
            etiqueta = Label(caja_ventana, text="Caja Abierta", font=("arial", 16), bg="#F0F0F0")
            etiqueta.pack(pady=20)

            # Frame para los botones dentro de la ventana de la caja
            botones_frame = Frame(caja_ventana, bg="#F0F0F0")
            botones_frame.pack(pady=10)

            # Botón Registrar Venta
            boton_registrar_venta = Button(
                botones_frame,
                text="Registrar Venta",
                font=("arial", 12),
                bg="#3498DB",
                fg="white",
                width=20,
                command=lambda: None  # Placeholder para futura funcionalidad
            )
            boton_registrar_venta.pack(pady=5)

            # Botón Enviar Mensaje
            boton_enviar_mensaje = Button(
                botones_frame,
                text="Enviar Mensaje",
                font=("arial", 12),
                bg="#2ECC71",
                fg="white",
                width=20,
                command=lambda: None  # Placeholder para futura funcionalidad
            )
            boton_enviar_mensaje.pack(pady=5)

            # Botón Cerrar Caja
            def cerrarCaja():
                caja_ventana.destroy()
                # Recrear la ventana principal
                new_frame = MenuDespachadora(self.ventana, self.empleado)

            boton_cerrar_caja = Button(
                botones_frame,
                text="Cerrar Caja",
                font=("arial", 12),
                bg="#E74C3C",
                fg="white",
                width=20,
                command=cerrarCaja
            )
            boton_cerrar_caja.pack(pady=5)

        # Frame para los botones funcionales
        frame_funcionalidades = Frame(self, bg="#415A77")
        frame_funcionalidades.pack(fill="both", expand=True, pady=20, padx=20)

        # Crear un contenedor para centrar los botones
        botones_container = Frame(frame_funcionalidades, bg="#415A77")
        botones_container.pack(expand=True)

        # Botón Abrir Caja
        boton_abrir_caja = Button(
            botones_container,
            text="Abrir caja",
            font=("arial", 14),
            bg="#1ABC9C",
            fg="white",
            width=15,
            command=abrirCaja
        )
        boton_abrir_caja.pack(pady=10)

        # Botón Cerrar Sesión
        boton_cerrar_sesion = Button(
            botones_container,
            text="Cerrar Sesión",
            font=("arial", 14),
            bg="#E74C3C",
            fg="white",
            width=15,
            command=cerrarSesion
        )
        boton_cerrar_sesion.pack(pady=10)
