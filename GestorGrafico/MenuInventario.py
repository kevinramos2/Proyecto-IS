import tkinter as tk
from tkinter import *
from tkinter import messagebox
from GestorAplicacion.Producto import Producto

class MenuInventario(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.ventana = ventana
        self.empleado = empleado

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        LabelFrame.pack(side="top", fill="x")

        mensaje = "Menu De Inventario"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "italic underline"),bg="#1B263B" , fg = "white")
        mensajeBienv.pack(side="left", padx=2)

        def volverAlMenu():
            from GestorGrafico.MenuAdmin import MenuAdmin
            self.destroy()
            MenuAdmin(self.ventana,self.empleado)



        #Funciones para los botones

        def verInventario():
          ventana_inventario = Toplevel(self.ventana)  # Crear una nueva ventana
          ventana_inventario.title("Inventario Completo")
          
          # Ajustar el tamaño de la ventana según las columnas
          ventana_inventario.geometry("900x400")  # Tamaño ajustado a las columnas

          # Añadir un título en la nueva ventana
          titulo = Label(ventana_inventario, text="Inventario Completo", font=("Arial", 16, "bold"), bg="#1B263B", fg="white")
          titulo.pack(fill="x")

          # Frame para el contenido del inventario
          frame_inventario = Frame(ventana_inventario)
          frame_inventario.pack(fill="both", expand=True, padx=10, pady=10)

          # Crear una barra de desplazamiento vertical
          scrollbar_y = Scrollbar(frame_inventario)
          scrollbar_y.pack(side=RIGHT, fill=Y)

          # Crear una barra de desplazamiento horizontal
          scrollbar_x = Scrollbar(frame_inventario, orient="horizontal")
          scrollbar_x.pack(side=BOTTOM, fill=X)

          # Crear un widget de Text para mostrar el inventario con scroll horizontal y vertical
          texto_inventario = Text(frame_inventario, wrap="none", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, font=("Courier", 12))
          texto_inventario.pack(fill="both", expand=True)

          # Configurar las barras de desplazamiento
          scrollbar_y.config(command=texto_inventario.yview)
          scrollbar_x.config(command=texto_inventario.xview)

          # Obtener el inventario
          inventario = Producto.inventario.mostrar_completo()  # Ahora esto retorna una lista de productos

          if inventario:  # Verificar que el inventario no esté vacío
              # Encabezados alineados con el espacio adecuado usando fuente monoespaciada
              headers = f"{'Producto':<25}{'Color/Aroma':<15}{'Referencia':<10}{'Precio':<10}{'Cantidad':<10}{'Categoría':<15}\n"
              texto_inventario.insert(END, headers)
              texto_inventario.insert(END, "-" * 90 + "\n")  # Separador visual

              # Colores alternos para las filas (opcional, pero se puede agregar después si se desea)
              
              for producto in inventario:
                  # Separar los detalles
                  detalles = producto.split(" - ")

                  # Verificar que hay suficientes partes en la división para evitar errores de índice
                  if len(detalles) >= 6:
                      # Extraemos los datos de cada campo sin las etiquetas redundantes
                      producto_nombre = detalles[0].split(": ")[1] if ": " in detalles[0] else detalles[0]
                      color_aroma = detalles[1].split(": ")[1] if ": " in detalles[1] else detalles[1]
                      referencia = detalles[2].split(": ")[1] if ": " in detalles[2] else detalles[2]
                      precio = detalles[3].split(": ")[1] if ": " in detalles[3] else detalles[3]
                      cantidad = detalles[4].split(": ")[1] if ": " in detalles[4] else detalles[4]
                      categoria = detalles[5].split(": ")[1] if ": " in detalles[5] else detalles[5]

                      # Formatear la fila con columnas alineadas usando una fuente monoespaciada
                      texto_formateado = f"{producto_nombre:<25}{color_aroma:<15}{referencia:<10}{precio:<10}{cantidad:<10}{categoria:<15}\n"
                      texto_inventario.insert(END, texto_formateado)
                  else:
                      print(f"Error en el formato del producto: {producto}")  # Mostrar un error en consola para depuración

          # Hacer que el widget de texto sea solo de lectura
          texto_inventario.config(state=DISABLED)



        def filtrarInventario():
             # Crear una nueva ventana para seleccionar la categoría
            ventana_filtro = Toplevel(self.ventana)
            ventana_filtro.title("Filtrar Inventario por Categoría")
            ventana_filtro.geometry("300x200")

            # Crear un título para la ventana
            titulo = Label(ventana_filtro, text="Seleccione una Categoría", font=("Arial", 14, "bold"))
            titulo.pack(pady=10)

            # Crear una lista de categorías
            categorias = ["Velon", "Vela Lisa", "Vela Lisa Baby", "Esencia"]

            # Variable para guardar la selección
            categoria_seleccionada = StringVar(ventana_filtro)
            categoria_seleccionada.set(categorias[0])  # Valor por defecto

            # Crear un menú desplegable para seleccionar la categoría
            menu_categorias = OptionMenu(ventana_filtro, categoria_seleccionada, *categorias)
            menu_categorias.pack(pady=10)

            # Función que se ejecuta al hacer clic en el botón "Filtrar"
            def mostrar_filtrado():
                # Obtener la categoría seleccionada
                categoria = categoria_seleccionada.get()

                # Crear una nueva ventana para mostrar el inventario filtrado
                ventana_inventario_filtrado = Toplevel(self.ventana)
                ventana_inventario_filtrado.title(f"Inventario Filtrado - {categoria}")
                ventana_inventario_filtrado.geometry("900x400")

                # Añadir un título en la nueva ventana
                titulo = Label(ventana_inventario_filtrado, text=f"Inventario - {categoria}", font=("Arial", 16, "bold"), bg="#1B263B", fg="white")
                titulo.pack(fill="x")

                # Frame para el contenido del inventario filtrado
                frame_inventario = Frame(ventana_inventario_filtrado)
                frame_inventario.pack(fill="both", expand=True, padx=10, pady=10)

                # Crear una barra de desplazamiento vertical
                scrollbar_y = Scrollbar(frame_inventario)
                scrollbar_y.pack(side=RIGHT, fill=Y)

                # Crear una barra de desplazamiento horizontal
                scrollbar_x = Scrollbar(frame_inventario, orient="horizontal")
                scrollbar_x.pack(side=BOTTOM, fill=X)

                # Crear un widget de Text para mostrar el inventario con scroll horizontal y vertical
                texto_inventario = Text(frame_inventario, wrap="none", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, font=("Courier", 12))
                texto_inventario.pack(fill="both", expand=True)

                # Configurar las barras de desplazamiento
                scrollbar_y.config(command=texto_inventario.yview)
                scrollbar_x.config(command=texto_inventario.xview)

                # Obtener los productos filtrados por categoría
                productos_filtrados = Producto.inventario.mostrar_por_categoria(categoria)

                if productos_filtrados:  # Verificar que haya productos en la categoría seleccionada
                    # Encabezados alineados con el espacio adecuado usando fuente monoespaciada
                    headers = f"{'Producto':<25}{'Color/Aroma':<15}{'Referencia':<10}{'Precio':<10}{'Cantidad':<10}{'Categoría':<15}\n"
                    texto_inventario.insert(END, headers)
                    texto_inventario.insert(END, "-" * 90 + "\n")  # Separador visual

                    for producto in productos_filtrados:
                        # Separar los detalles
                        detalles = producto.split(" - ")

                        if len(detalles) >= 6:
                            # Extraer los datos de cada campo sin las etiquetas redundantes
                            producto_nombre = detalles[0].split(": ")[1] if ": " in detalles[0] else detalles[0]
                            color_aroma = detalles[1].split(": ")[1] if ": " in detalles[1] else detalles[1]
                            referencia = detalles[2].split(": ")[1] if ": " in detalles[2] else detalles[2]
                            precio = detalles[3].split(": ")[1] if ": " in detalles[3] else detalles[3]
                            cantidad = detalles[4].split(": ")[1] if ": " in detalles[4] else detalles[4]
                            categoria = detalles[5].split(": ")[1] if ": " in detalles[5] else detalles[5]

                            # Formatear la fila con columnas alineadas usando una fuente monoespaciada
                            texto_formateado = f"{producto_nombre:<25}{color_aroma:<15}{referencia:<10}{precio:<10}{cantidad:<10}{categoria:<15}\n"
                            texto_inventario.insert(END, texto_formateado)
                        else:
                            print(f"Error en el formato del producto: {producto}")  # Mostrar un error en consola para depuración
                else:
                    texto_inventario.insert(END, "No hay productos en esta categoría.")

                # Hacer que el widget de texto sea solo de lectura
                texto_inventario.config(state=DISABLED)

            # Crear un botón para aplicar el filtro 
            boton_filtrar = Button(ventana_filtro, text="Filtrar", command=mostrar_filtrado)
            boton_filtrar.pack(pady=10)

        def agregarProducto():
            ventana_agregar = Toplevel(self.ventana)
            ventana_agregar.title("Agregar Nuevo Producto")
            ventana_agregar.geometry("400x480")

            # Título
            titulo = Label(ventana_agregar, text="Agregar Producto", font=("Arial", 16, "bold"))
            titulo.pack(pady=10)

            # Nombre del producto
            lbl_nombre = Label(ventana_agregar, text="Nombre:")
            lbl_nombre.pack(pady=5)
            entry_nombre = Entry(ventana_agregar)
            entry_nombre.pack(pady=5)

            # Referencia
            lbl_referencia = Label(ventana_agregar, text="Referencia:")
            lbl_referencia.pack(pady=5)
            entry_referencia = Entry(ventana_agregar)
            entry_referencia.pack(pady=5)

            # Stock
            lbl_stock = Label(ventana_agregar, text="Cantidad en Stock:")
            lbl_stock.pack(pady=5)
            entry_stock = Entry(ventana_agregar)
            entry_stock.pack(pady=5)

            # Precio
            lbl_precio = Label(ventana_agregar, text="Precio:")
            lbl_precio.pack(pady=5)
            entry_precio = Entry(ventana_agregar)
            entry_precio.pack(pady=5)

            # Categoría
            lbl_categoria = Label(ventana_agregar, text="Categoría:")
            lbl_categoria.pack(pady=5)
            categorias = ["Velon", "Vela Lisa", "Vela Lisa Baby", "Esencia"]
            categoria_seleccionada = StringVar(ventana_agregar)
            categoria_seleccionada.set(categorias[0])  # Valor por defecto
            menu_categorias = OptionMenu(ventana_agregar, categoria_seleccionada, *categorias)
            menu_categorias.pack(pady=5)

            # Color o Aroma
            lbl_color_aroma = Label(ventana_agregar, text="Color/Aroma:")
            lbl_color_aroma.pack(pady=5)
            entry_color_aroma = Entry(ventana_agregar)
            entry_color_aroma.pack(pady=5)

            # Función para guardar el producto
            def guardarProducto():
                nombre = entry_nombre.get()
                referencia = entry_referencia.get()
                try:
                    stock = int(entry_stock.get())
                    precio = float(entry_precio.get())
                except ValueError:
                    # Mostrar mensaje de error si no se ingresan números válidos en stock y precio
                    messagebox.showerror("Error", "Ingrese valores numéricos válidos en 'Stock' y 'Precio'.")
                    return

                categoria = categoria_seleccionada.get()
                color_aroma = entry_color_aroma.get()

                # Crear nuevo producto
                if categoria == "Esencia":
                    nuevo_producto = Producto(nombre=nombre, referencia=referencia, stock=stock, categoria=categoria, precio=precio, aroma=color_aroma)
                else:
                    nuevo_producto = Producto(nombre=nombre, referencia=referencia, stock=stock, categoria=categoria, precio=precio, color=color_aroma)

                # Cerrar ventana después de agregar
                ventana_agregar.destroy()

                # Mostrar mensaje de confirmación en una ventana emergente
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado con éxito.")

            # Botón para guardar el producto
            btn_guardar = Button(ventana_agregar, text="Guardar Producto", command=guardarProducto)
            btn_guardar.pack(pady=10)
        
        def actualizarStock():
            # Crear una nueva ventana para actualizar inventario
            ventana_actualizar = Toplevel(self.ventana)
            ventana_actualizar.title("Actualizar Inventario")
            ventana_actualizar.geometry("400x400")

            # Título
            titulo = Label(ventana_actualizar, text="Actualizar Inventario", font=("Arial", 16, "bold"))
            titulo.pack(pady=10)

            # Campo de búsqueda
            lbl_buscar = Label(ventana_actualizar, text="Buscar Producto (por Nombre o Referencia):")
            lbl_buscar.pack(pady=5)
            entry_buscar = Entry(ventana_actualizar)
            entry_buscar.pack(pady=5)

            # Frame para mostrar los mensajes
            frame_mensajes = Frame(ventana_actualizar)
            frame_mensajes.pack(pady=5)

            # Frame para mostrar los detalles del producto y las opciones
            frame_resultados = Frame(ventana_actualizar)
            frame_resultados.pack(pady=5)

            # Función para buscar el producto
            def buscarProducto():
                # Limpiar mensajes y resultados previos
                for widget in frame_mensajes.winfo_children():
                    widget.destroy()
                for widget in frame_resultados.winfo_children():
                    widget.destroy()

                busqueda = entry_buscar.get()
                producto_encontrado = Producto.inventario.buscar_producto(busqueda)  # Suponiendo que tienes esta función

                if producto_encontrado:
                    # Mostrar los detalles del producto
                    detalles = f"Producto: {producto_encontrado.nombre} - Stock: {producto_encontrado.stock}"
                    lbl_detalles = Label(frame_resultados, text=detalles, font=("Arial", 12))
                    lbl_detalles.pack(pady=5)

                    # Frame para las opciones de eliminar o modificar stock
                    frame_opciones = Frame(frame_resultados)
                    frame_opciones.pack(pady=5)

                    # Botón para eliminar producto
                    btn_eliminar = Button(frame_opciones, text="Eliminar Producto", bg="red", fg="white", command=lambda: eliminarProducto(producto_encontrado))
                    btn_eliminar.grid(row=0, column=0, padx=10)

                    # Botón para modificar stock
                    btn_modificar = Button(frame_opciones, text="Modificar Stock", command=lambda: mostrarModificarStock(producto_encontrado))
                    btn_modificar.grid(row=0, column=1, padx=10)

                else:
                    # Mensaje de error si no se encuentra el producto
                    mensaje_error = Label(frame_mensajes, text="Producto no encontrado.", fg="red")
                    mensaje_error.pack()

            # Función para eliminar producto
            def eliminarProducto(producto):
                # Limpiar mensajes previos
                for widget in frame_mensajes.winfo_children():
                    widget.destroy()

                Producto.inventario.eliminar_producto(producto.referencia)  # Suponiendo que tienes esta función

                mensaje_exito = Label(frame_mensajes, text=f"Producto '{producto.nombre}' eliminado.", fg="green")
                mensaje_exito.pack()

                # Limpiar los resultados ya que el producto fue eliminado
                for widget in frame_resultados.winfo_children():
                    widget.destroy()

            # Función para mostrar la opción de modificar el stock
            def mostrarModificarStock(producto):
                # Limpiar mensajes previos
                for widget in frame_mensajes.winfo_children():
                    widget.destroy()

                # Limpiar el frame de resultados para solo mostrar la opción de modificar stock
                for widget in frame_resultados.winfo_children():
                    widget.destroy()

                # Frame para modificar stock
                frame_modificar_stock = Frame(frame_resultados)
                frame_modificar_stock.pack(pady=10)

                lbl_nuevo_stock = Label(frame_modificar_stock, text="Nuevo Stock:")
                lbl_nuevo_stock.pack(side="left", padx=5)
                entry_nuevo_stock = Entry(frame_modificar_stock)
                entry_nuevo_stock.pack(side="left", padx=5)

                def modificarStock():
                    # Limpiar mensajes previos
                    for widget in frame_mensajes.winfo_children():
                        widget.destroy()

                    try:
                        nuevo_stock = int(entry_nuevo_stock.get())
                        producto.stock = nuevo_stock
                        mensaje_exito = Label(frame_mensajes, text=f"Stock del producto '{producto.nombre}' actualizado a {nuevo_stock}.", fg="green")
                        mensaje_exito.pack()

                        # Limpiar los resultados ya que el stock fue actualizado
                        for widget in frame_resultados.winfo_children():
                            widget.destroy()
                    except ValueError:
                        mensaje_error = Label(frame_mensajes, text="Error: El stock debe ser un número.", fg="red")
                        mensaje_error.pack()

                # Botón para aplicar el nuevo stock
                btn_aplicar_stock = Button(frame_modificar_stock, text="Aplicar", command=modificarStock)
                btn_aplicar_stock.pack(side="left", padx=5)

            # Botón para buscar producto
            btn_buscar = Button(ventana_actualizar, text="Buscar", command=buscarProducto)
            btn_buscar.pack(pady=10)

            # Botón para cancelar operación
            btn_cancelar = Button(ventana_actualizar, text="Cancelar", bg="gray", command=ventana_actualizar.destroy)
            btn_cancelar.pack(pady=10)

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

        botonVerInventarioC = Button(
            FrameFuncionalidades, 
            text="Ver Inventario",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=verInventario)
        
        botonVerInventarioC.pack(fill="x", side="top",expand=True, padx= 5)

        botonFiltrarInventario = Button(
            FrameFuncionalidades, 
            text="Filtrar Inventario",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command=filtrarInventario)
        
        botonFiltrarInventario.pack(fill="x", side="top",expand=True, padx= 5)


        botonAgregarProducto = Button(
            FrameFuncionalidades, 
            text="Agregar Producto",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command= agregarProducto)
        
        botonAgregarProducto.pack(fill="x", side="top",expand=True, padx= 5)


        #En actualizar inventario estara:
        #Buscar producto
        #Eliminar producto
        #Modificar stock
        botonActualizarStock = Button(
            FrameFuncionalidades, 
            text="Actualizar Inventario",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command= actualizarStock)
        
        botonActualizarStock.pack(fill="x", side="top",expand=True, padx= 5)

