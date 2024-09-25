import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta
import os
import subprocess
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

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
            caja_ventana = Frame(self.ventana,bg="#E0E1DD")
            caja_ventana.pack(fill="both", expand=True)
            
             # Frame para el Mensaje de Bienvenida
            LabelFrame1 = Frame(caja_ventana, height=100, bg="#1B263B", padx=5, pady=5)
            LabelFrame1.pack(side="top", fill="x")
            # Etiqueta indicativa
            etiqueta = Label(LabelFrame1, text="Caja Abierta", font=("arial", 16), bg="#1B263B", fg="white")
            etiqueta.pack(pady=20)

            # Frame para los botones dentro de la ventana de la caja
            botones_frame = Frame(caja_ventana, bg="#415A77", height=400, width=500)
            botones_frame.pack_propagate(False)
            botones_frame.pack(fill="y", expand=True, pady=5, padx=5)

            # Botón Registrar Venta
            boton_registrar_venta = Button(
                botones_frame,
                text="Registrar Venta",
                font=("arial", 20, "bold"),
                bg="#E0E1DD",
                fg="black",
                width=20,
                padx=5,
                command=self.abrir_registrar_venta  # Actualizado
            )
            boton_registrar_venta.pack(fill="x", side="top", expand= True, pady=5)
            
            # Botón Cerrar Caja
            def cerrarCaja():
                caja_ventana.destroy()
                # Volver a la pantalla de login
                from GestorGrafico.LogInGrafico import LogInGrafico
                LogInGrafico.Caja_Cerrada = True
                LogInGrafico(self.ventana)

            boton_cerrar_caja = Button(
                botones_frame,
                text="Cerrar Caja",
                font=("arial", 20, "bold"),
                bg="#E0E1DD",
                fg="black",
                width=20,
                padx=5,
                command=cerrarCaja
            )
            boton_cerrar_caja.pack(fill="x", side="top", expand= True, pady=5)

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

    def abrir_registrar_venta(self):
            registrar_venta_ventana = Toplevel(self.ventana)
            registrar_venta_ventana.title("Registrar Venta")
            registrar_venta_ventana.geometry("1000x800") 
            registrar_venta_ventana.config(bg="#F0F0F0")
            self.registrar_venta_ventana = registrar_venta_ventana  # Guardar referencia para cerrarla después

            # Etiqueta de título
            titulo = Label(registrar_venta_ventana, text="Registrar Nueva Venta", font=("arial", 16, "bold"), bg="#F0F0F0")
            titulo.pack(pady=10)

            # Sección para seleccionar tipo de entrega
            entrega_frame = LabelFrame(registrar_venta_ventana, text="Tipo de Entrega", bg="#F0F0F0", font=("arial", 12, "bold"))
            entrega_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Etiqueta explicativa
            instruccion_label = Label(entrega_frame, text="Por favor, seleccione el tipo de entrega (obligatorio):", bg="#F0F0F0", fg="red")
            instruccion_label.pack(pady=5)

            # Variable para los radiobuttons
            self.tipo_entrega_var = StringVar()

            # Radiobuttons para seleccionar el tipo de entrega
            self.entrega_inmediata_rb = Radiobutton(entrega_frame, text="Express", variable=self.tipo_entrega_var, value="Express", bg="#F0F0F0", command=self.verificar_entrega)
            self.entrega_inmediata_rb.pack(side="left", padx=10, pady=10)

            self.pedido_rb = Radiobutton(entrega_frame, text="Pedido", variable=self.tipo_entrega_var, value="Pedido", bg="#F0F0F0", command=self.verificar_entrega)
            self.pedido_rb.pack(side="left", padx=10, pady=10)
            
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
            self.agregar_producto_btn = Button(productos_frame, text="Agregar Producto", bg="#1ABC9C", fg="white",
                                    command=lambda: self.agregar_producto_a_lista(self.tipo_entrega_var.get()),
                                    state=DISABLED)
            self.agregar_producto_btn.grid(row=2, column=0, columnspan=2, pady=10)

            # Botón para agregar producto personalizado (inicialmente oculto)
            self.agregar_producto_personalizado_btn = Button(productos_frame, text="Agregar Producto Personalizado", bg="#3498DB", fg="white",
                                                            command=self.abrir_cuestionario_personalizado, state=DISABLED)
            self.agregar_producto_personalizado_btn.grid(row=2, column=1, pady=10)

            # Listbox para mostrar los productos agregados
            self.productos_listbox = Listbox(productos_frame, width=80)
            self.productos_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

            # Scrollbar para la Listbox
            scrollbar = Scrollbar(productos_frame, orient=VERTICAL, command=self.productos_listbox.yview)
            scrollbar.grid(row=3, column=2, sticky='ns')
            self.productos_listbox.config(yscrollcommand=scrollbar.set)

            # Mensaje de advertencia
            self.mensaje_advertencia = Label(productos_frame, text="", bg="#F0F0F0", fg="red")
            self.mensaje_advertencia.grid(row=4, column=0, columnspan=2)

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

    def verificar_entrega(self):
        # Activar el botón de agregar producto si se selecciona un tipo de entrega
        if self.tipo_entrega_var.get() == "":
            self.mensaje_advertencia.config(text="¡Selección obligatoria! Debe seleccionar un tipo de entrega.")
            self.agregar_producto_btn.config(state=DISABLED)
            self.agregar_producto_personalizado_btn.config(state=DISABLED)  # Deshabilitar el botón personalizado
        else:
            self.mensaje_advertencia.config(text="")
            self.agregar_producto_btn.config(state=NORMAL)

            # Deshabilitar los Radiobuttons para evitar cambios
            self.entrega_inmediata_rb.config(state=DISABLED)
            self.pedido_rb.config(state=DISABLED)

            # Habilitar el botón de producto personalizado solo si es "Pedido"
            if self.tipo_entrega_var.get() == "Pedido":
                self.agregar_producto_personalizado_btn.config(state=NORMAL)
            else:
                self.agregar_producto_personalizado_btn.config(state=DISABLED)
    
    def abrir_cuestionario_personalizado(self):
        # Crear una nueva ventana para el cuestionario
        self.cuestionario_ventana = Toplevel(self.registrar_venta_ventana)
        self.cuestionario_ventana.title("Agregar Producto Personalizado")
        self.cuestionario_ventana.geometry("400x500")  # Aumentar el tamaño de la ventana
        self.cuestionario_ventana.config(bg="#F0F0F0")

        # Entrada para la categoría
        categoria_label = Label(self.cuestionario_ventana, text="Categoría:", bg="#F0F0F0")
        categoria_label.pack(pady=5)
        self.categoria_label_entry = Entry(self.cuestionario_ventana)  # Definir como atributo
        self.categoria_label_entry.pack(pady=5)

        # Entrada para la cantidad
        cantidad_label = Label(self.cuestionario_ventana, text="Cantidad:", bg="#F0F0F0")
        cantidad_label.pack(pady=5)
        self.cantidad_personalizada_entry = Entry(self.cuestionario_ventana)  # Aquí se define como atributo
        self.cantidad_personalizada_entry.pack(pady=5)

        # Entrada para el precio
        precio_label = Label(self.cuestionario_ventana, text="Precio Unidad:", bg="#F0F0F0")
        precio_label.pack(pady=5)
        self.precio_entry = Entry(self.cuestionario_ventana)  # Aquí se define como atributo
        self.precio_entry.pack(pady=5)

        # Entrada para comentarios
        comentario_label = Label(self.cuestionario_ventana, text="Comentarios:", bg="#F0F0F0")
        comentario_label.pack(pady=5)
        self.comentario_text = Text(self.cuestionario_ventana, height=5, width=40)  # Text widget para comentarios más largos
        self.comentario_text.pack(pady=5)

        # Botón para agregar el producto personalizado
        agregar_btn = Button(self.cuestionario_ventana, text="Agregar Producto", bg="#2ECC71", fg="white", command=lambda: self.agregar_producto_personalizado())
        agregar_btn.pack(pady=20)

    def agregar_producto_personalizado(self):
        categoria = self.categoria_label_entry.get().strip()
        cantidad = self.cantidad_personalizada_entry.get().strip()
        precio = self.precio_entry.get().strip()
        comentario = self.comentario_text.get("1.0", "end-1c").strip()

        # Validar que todos los campos estén llenos
        if not (categoria and cantidad and precio):
            self.mostrar_mensaje_error("Todos los campos son obligatorios.")
            return

        # Validar que cantidad y precio sean números válidos
        try:
            cantidad_int = int(cantidad)
            precio_float = float(precio)
        except ValueError:
            self.mostrar_mensaje_error("Cantidad y Precio deben ser números válidos.")
            return
        
        # Verificar que categoria es un string no vacío y no contiene solo dígitos
        if not isinstance(categoria, str) or not categoria or categoria.isdigit():
            self.mostrar_mensaje_error("La categoría debe ser un string no vacío que no contenga solo números.")
            return

        # Verificar que comentario es un string no vacío y no contiene solo dígitos
        if not isinstance(comentario, str) or not comentario or comentario.isdigit():
            self.mostrar_mensaje_error("El comentario debe ser un string no vacío que no contenga solo números.")
            return


        
        self.cuestionario_ventana.destroy()

        nombre = "personalizado" + str(Producto.contador_personalizados)
        referencia = "idpersonalizado" + str(Producto.contador_personalizados)

        producto = Producto(nombre, referencia, cantidad_int, categoria, precio_float, None, None, comentario)

        # Aquí agregarías el producto a la lista o a donde sea necesario
        self.productos_listbox.insert(END, f"{producto.nombre} (Ref: {producto.referencia}) - Cantidad: {cantidad_int} - Precio Total: {precio_float} COP - Comentario: {comentario}")
    
    def mostrar_mensaje_error(self, mensaje):
        error_ventana = Toplevel(self.cuestionario_ventana)
        error_ventana.title("Error")
        Label(error_ventana, text=mensaje, padx=10, pady=10).pack()
        Button(error_ventana, text="Cerrar", command=error_ventana.destroy).pack(pady=5)

    def validar_campos(self):
        categoria = self.categoria_label_entry.get().strip()
        cantidad = self.cantidad_personalizada_entry.get().strip()
        precio = self.precio_entry.get().strip()

        if not categoria or not cantidad or not precio:
            self.mostrar_mensaje_error("Todos los campos son obligatorios.")
            return False
        return True     

    # Función para agregar productos a la lista
    def agregar_producto_a_lista(self, tipo_entrega):
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

        #Actualziar contador
        Producto.contador_personalizados+=1

        if not producto:
            messagebox.showerror("Error", "La referencia del producto no es válida.")
            return
        if(tipo_entrega == "Express"):
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

    def generar_factura_pdf(self, nombre_archivo, datos_factura):
        # Obtener la ruta del escritorio del usuario
        escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Ruta de la carpeta 'facturas' en el escritorio
        carpeta_facturas = os.path.join(escritorio, "facturas")
        
        # Crear la carpeta si no existe
        if not os.path.exists(carpeta_facturas):
            os.makedirs(carpeta_facturas)
        
        # Ruta completa donde se guardará el PDF
        ruta_completa = os.path.join(carpeta_facturas, nombre_archivo)
        
        # Crear el documento PDF
        c = canvas.Canvas(ruta_completa, pagesize=A4)

        # Agregar una imagen (logo) en la esquina superior izquierda
        logo_path = "BaseDeDatos\\Imagenes\\unnamed.jpg"  # Cambia esto a la ruta de tu imagen
        c.drawImage(logo_path, 50, 740, width=80, height=80)  # Ajuste del tamaño y posición de la imagen

        # Título de la factura
        titulo = "Velas Manare"
        c.setFont("Helvetica-Bold", 24)
        c.drawString(180, 780, titulo)  # Centrar el título

        # Información del cliente y la factura
        c.setFont("Helvetica", 12)
        c.drawString(50, 700, f"Fecha de la venta: {datos_factura['fecha']}")
        c.drawString(50, 680, f"Despachador@ responsable: {datos_factura['despachador@_responsable']}")
        c.drawString(50, 660, f"Codigo de venta: {datos_factura['ID Venta']}")
        c.drawString(50, 640, f"Identificación cliente: {datos_factura['ID Cliente']}")
        c.drawString(50, 620, f"Metodo de Pago: {datos_factura['Metodo de Pago']}")
        c.drawString(50, 600, f"Estado: {datos_factura['Estado']}")

        # Tabla con los productos
        y = 580
        for producto in datos_factura["productos"]:
            prod = producto[0]
            total_formateado = f"{prod.get_precio():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " COP"
            
            try:
                comentario = prod.get_comentario()
                if comentario is None:
                    descripcion = f"{prod.get_nombre()} - (Ref: {prod.get_referencia()}) - Precio: {total_formateado}"
                else:
                    descripcion = f"{prod.get_nombre()} - (Ref: {prod.get_referencia()}) - Precio: {total_formateado} - Comentario: {comentario}"
            except AttributeError:
                # Manejo de error en caso de que el atributo 'comentario' no exista
                descripcion = f"{prod.get_nombre()} - (Ref: {prod.get_referencia()}) - Precio: {total_formateado}"

            # Controlar el ancho de la línea (90 caracteres como límite)
            wrapped_text = textwrap.wrap(descripcion, width=90)
            
            # Dibujar cada línea envuelta
            for line in wrapped_text:
                c.drawString(50, y, line)
                y -= 20  # Ajustar la posición vertical para cada nueva línea
            
            c.drawString(50, y, f"Cantidad: {producto[1]}")
            y -= 20  # Espacio para la siguiente descripción


        # Calcular y mostrar el total
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y - 40, f"Total: {datos_factura['Total']}")

        # Agregar el pie de página con "Agario Solutions"
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(200, 30, "Agario Solutions")  # Posición cercana al pie de la página

        # Guardar el PDF
        c.save()
        print(f"Factura guardada en: {ruta_completa}")

        # Abrir el PDF automáticamente
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_completa)
        elif os.name == 'posix':  # Para macOS y Linux
            if sys.platform == "darwin":  # Para macOS
                subprocess.call(["open", ruta_completa])
            else:  # Para Linux
                subprocess.call(["xdg-open", ruta_completa])




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
        empleado = self.empleado.getNombre()
        # Formatear el total de la venta
        total_formateado = f"{venta.total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " COP"
        # Mostrar confirmación
        confirmacion = messagebox.askyesno("Confirmar Venta", 
            f"Atendido por: {empleado}\n"
            f"ID Cliente: {id_cliente}\n"
            f"Fecha: {venta.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Total: {total_formateado}\n"
            f"Método de Pago: {metodo_pago}\n\n"
            f"¿Desea confirmar la venta?"
        )

        if confirmacion:
            
            venta.id_venta = venta.crear_id_venta()

            if (self.tipo_entrega_var.get() != "Pedido"):
                venta.estado = 'confirmada'
            
            datos_factura = {
                "despachador@_responsable": empleado,
                "ID Venta" : venta.id_venta,
                "ID Cliente" : id_cliente,
                "fecha" : venta.fecha.strftime('%Y-%m-%d %H:%M:%S'),
                "Metodo de Pago" : metodo_pago,
                "productos": venta.productos,
                "Total" :  total_formateado,
                "Estado" : venta.estado
            }


            # Actualizar existencias
            if (self.tipo_entrega_var.get() != "Pedido"):
                for producto, cantidad in productos:
                    Producto.inventario.actualizar_existencias(producto, cantidad)
            messagebox.showinfo("Éxito", "Venta confirmada exitosamente.")
            nombre_factura = "Factura - " + venta.id_venta
            self.generar_factura_pdf(nombre_factura, datos_factura)
            # Cerrar la ventana de registro de venta
            self.registrar_venta_ventana.destroy()
        else:
            venta.estado = 'cancelada'
            messagebox.showinfo("Cancelado", "Venta cancelada.")
            # Opcional: limpiar la lista de productos
            self.productos_listbox.delete(0, END)
