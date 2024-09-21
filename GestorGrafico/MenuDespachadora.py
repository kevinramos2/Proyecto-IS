import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta
# Removed playsound import since it's not needed

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
                command=self.abrir_registrar_venta  # Actualizado
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
                command=lambda: None  # Futura funcionalidad
            )
            boton_enviar_mensaje.pack(pady=5)

            # Botón Cerrar Caja
            def cerrarCaja():
                caja_ventana.destroy()
                # Volver a la pantalla de login
                from GestorGrafico.LogInGrafico import LogInGrafico
                LogInGrafico(self.ventana)

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

        # Eliminado el Botón "Cerrar Sesión"
        # Ya no se crea ni se empaca el botón "Cerrar Sesión"

    # Función para abrir la ventana de registrar venta
    def abrir_registrar_venta(self):
        registrar_venta_ventana = Toplevel(self.ventana)
        registrar_venta_ventana.title("Registrar Venta")
        registrar_venta_ventana.geometry("600x800") 
        registrar_venta_ventana.config(bg="#F0F0F0")
        self.registrar_venta_ventana = registrar_venta_ventana  # Guardar referencia para cerrarla después

        # Etiqueta de título
        titulo = Label(registrar_venta_ventana, text="Registrar Nueva Venta", font=("arial", 16, "bold"), bg="#F0F0F0")
        titulo.pack(pady=10)

        # Sección para agregar productos
        productos_frame = LabelFrame(registrar_venta_ventana, text="Productos", bg="#F0F0F0", font=("arial", 12, "bold"))
        productos_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Ajustar la cuadrícula para centrar los elementos
        productos_frame.columnconfigure(0, weight=1)
        productos_frame.columnconfigure(1, weight=3)

        # Entrada para el ID del producto (Referencia)
        id_producto_label = Label(productos_frame, text="Referencia del Producto:", bg="#F0F0F0")
        id_producto_label.grid(row=0, column=0, padx=5, pady=(5, 2), sticky="e")
        self.id_producto_entry = Entry(productos_frame)
        self.id_producto_entry.grid(row=0, column=1, padx=5, pady=(5, 2), sticky="w")

        # Entrada para la cantidad
        cantidad_label = Label(productos_frame, text="Cantidad:", bg="#F0F0F0")
        cantidad_label.grid(row=1, column=0, padx=5, pady=(2, 2), sticky="e")
        self.cantidad_entry = Entry(productos_frame)
        self.cantidad_entry.grid(row=1, column=1, padx=5, pady=(2, 2), sticky="w")

        # Botón para agregar producto a la lista
        agregar_producto_btn = Button(productos_frame, text="Agregar Producto", bg="#1ABC9C", fg="white", command=self.agregar_producto_a_lista)
        agregar_producto_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox para mostrar los productos agregados
        self.productos_listbox = Listbox(productos_frame, width=80)
        self.productos_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Scrollbar para la Listbox
        scrollbar = Scrollbar(productos_frame, orient=VERTICAL, command=self.productos_listbox.yview)
        scrollbar.grid(row=3, column=2, sticky='ns')
        self.productos_listbox.config(yscrollcommand=scrollbar.set)

        # Sección para ingresar ID del Cliente
        cliente_frame = LabelFrame(registrar_venta_ventana, text="Cliente", bg="#F0F0F0", font=("arial", 12, "bold"))
        cliente_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Centrar los elementos dentro de cliente_frame
        cliente_frame.columnconfigure(0, weight=1)
        cliente_frame.columnconfigure(1, weight=3)

        id_cliente_label = Label(cliente_frame, text="ID del Cliente:", bg="#F0F0F0")
        id_cliente_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.id_cliente_entry = Entry(cliente_frame)
        self.id_cliente_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Sección para seleccionar método de pago
        pago_frame = LabelFrame(registrar_venta_ventana, text="Método de Pago", bg="#F0F0F0", font=("arial", 12, "bold"))
        pago_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Centrar los elementos dentro de pago_frame
        pago_frame.columnconfigure(0, weight=1)
        pago_frame.columnconfigure(1, weight=3)

        opciones_pago = {
            "Transferencia": "Transferencia",
            "Efectivo": "Efectivo"
        }

        pago_label = Label(pago_frame, text="Seleccione Método de Pago:", bg="#F0F0F0")
        pago_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.metodo_pago_var = StringVar()
        self.metodo_pago_var.set("Transferencia")  # Por Defecto la transferencia

        metodo_pago_menu = OptionMenu(pago_frame, self.metodo_pago_var, *opciones_pago.values())
        metodo_pago_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Botón para confirmar venta
        confirmar_btn = Button(registrar_venta_ventana, text="Confirmar Venta", bg="#2ECC71", fg="white", font=("arial", 12, "bold"), command=self.confirmar_venta)
        confirmar_btn.pack(pady=20)

    # Función para agregar productos a la lista
    def agregar_producto_a_lista(self):
        id_producto = self.id_producto_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()

        # Validaciones
        if not id_producto:
            messagebox.showerror("Error", "Debe ingresar una referencia de producto.")
            return
        if not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showerror("Error", "La cantidad debe ser un número entero positivo.")
            return

        # Buscar el producto en el inventario usando la referencia
        producto = Producto.inventario.buscar_producto(id_producto)
        if not producto:
            messagebox.showerror("Error", "La referencia del producto no es válida.")
            return
        if producto.stock < int(cantidad):
            messagebox.showerror("Error", f"Solo hay {producto.stock} existencias de este producto.")
            return

        cantidad_int = int(cantidad)
        precio_unitario = producto.get_precio()
        precio_total = precio_unitario * cantidad_int

        # Formatear los precios con separadores de miles
        precio_unitario_formateado = f"{precio_unitario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        precio_total_formateado = f"{precio_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Agregar producto a la lista con el precio total
        self.productos_listbox.insert(END, f"{producto.nombre} (Ref: {producto.referencia}) - Cantidad: {cantidad_int} - Precio Total: {precio_total_formateado} COP")

        # Limpiar los campos de entrada
        self.id_producto_entry.delete(0, END)
        self.cantidad_entry.delete(0, END)

    # Función para confirmar la venta
    def confirmar_venta(self):
        # Obtener productos de la lista
        productos = []
        for i in range(self.productos_listbox.size()):
            item = self.productos_listbox.get(i)
            try:
                # Extraer la referencia y cantidad del string
                # Formato esperado: "Nombre (Ref: referencia) - Cantidad: cantidad - Precio Total: precio_total"
                partes = item.split(" - ")
                nombre_ref = partes[0]
                cantidad_str = partes[1].split(": ")[1]
                # precio_total = partes[2].split(": ")[1]  # Opcional si deseas usarlo
                nombre, ref_part = nombre_ref.split(" (Ref: ")
                referencia = ref_part.rstrip(")")
                cantidad = int(cantidad_str)
            except (ValueError, IndexError):
                messagebox.showerror("Error", f"Formato inválido en el producto: {item}")
                return

            # Buscar el producto por referencia
            producto = Producto.inventario.buscar_producto(referencia)
            if producto:
                productos.append((producto, cantidad))
            else:
                messagebox.showerror("Error", f"No se encontró el producto con referencia: {referencia}")
                return

        if not productos:
            messagebox.showerror("Error", "Debe agregar al menos un producto a la venta.")
            return

        # Obtener ID del cliente
        id_cliente = self.id_cliente_entry.get().strip()
        if not id_cliente.isdigit() or int(id_cliente) <= 0:
            messagebox.showerror("Error", "El ID del cliente debe ser un número entero positivo.")
            return
        id_cliente = int(id_cliente)

        # Obtener método de pago
        metodo_pago = self.metodo_pago_var.get()

        # Crear instancia de Venta
        venta = Venta()
        venta.id_cliente = id_cliente
        venta.productos = productos
        venta.fecha = datetime.now()
        venta.total = venta.total_venta(productos)
        # Nota: La clase Venta original no tiene el atributo 'metodo_pago'.
        # Si deseas almacenarlo, necesitarás modificar la clase Venta.
        # Aquí, lo almacenaremos como un atributo dinámico.
        venta.metodo_pago = metodo_pago
        venta.estado = 'pendiente'

        # Formatear el total de la venta
        total_formateado = f"{venta.total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Mostrar confirmación
        confirmacion = messagebox.askyesno("Confirmar Venta", 
            f"Atendido por: {self.empleado.getNombre()}\n"
            f"ID Venta: {venta.crear_id_venta()}\n"
            f"ID Cliente: {id_cliente}\n"
            f"Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Total: {total_formateado} COP\n"
            f"Método de Pago: {metodo_pago}\n\n"
            f"¿Desea confirmar la venta?"
        )

        if confirmacion:
            venta.id_venta = venta.crear_id_venta()
            venta.estado = 'confirmada'
            # Actualizar existencias
            for producto, cantidad in productos:
                Producto.inventario.actualizar_existencias(producto, cantidad)
            Venta._todas_las_ventas.append(venta)
            messagebox.showinfo("Éxito", "Venta confirmada exitosamente.")
            # Cerrar la ventana de registro de venta
            self.registrar_venta_ventana.destroy()
        else:
            venta.estado = 'cancelada'
            messagebox.showinfo("Cancelado", "Venta cancelada.")
            # Opcional: limpiar la lista de productos
            self.productos_listbox.delete(0, END)
