import tkinter as tk
from tkinter import *
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
          ventana_inventario.geometry("1000x500")  # Tamaño más grande para ver mejor el inventario
      
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
          texto_inventario = Text(frame_inventario, wrap="none", yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, font=("Arial", 12))
          texto_inventario.pack(fill="both", expand=True)
      
          # Configurar las barras de desplazamiento
          scrollbar_y.config(command=texto_inventario.yview)
          scrollbar_x.config(command=texto_inventario.xview)
      
          # Obtener el inventario
          inventario = Producto.inventario.mostrar_completo()  # Ahora esto retorna una lista de productos
      
          if inventario:  # Verificar que el inventario no esté vacío
              # Encabezados alineados
              headers = f"{'Producto':<25}\t{'Color/Aroma':<20}\t{'Referencia':<15}\t{'Precio':<10}\t{'Cantidad':<10}\t{'Categoría':<15}\n"
              texto_inventario.insert(END, headers)
              texto_inventario.insert(END, "-" * 120 + "\n")  # Separador visual
      
              # Colores alternos para las filas
              row_color = ["#E8E8E8", "#FFFFFF"]
      
              for idx, producto in enumerate(inventario):
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
      
                      # Formatear la fila con columnas alineadas
                      texto_formateado = f"{producto_nombre:<25}\t{color_aroma:<20}\t{referencia:<15}\t{precio:<10}\t{cantidad:<10}\t{categoria:<15}\n"
      
                      # Alternar color de fila
                      texto_inventario.tag_configure(f'row{idx}', background=row_color[idx % 2])
      
                      texto_inventario.insert(END, texto_formateado, f'row{idx}')
                  else:
                      print(f"Error en el formato del producto: {producto}")  # Mostrar un error en consola para depuración
      
          # Hacer que el widget de texto sea solo de lectura
          texto_inventario.config(state=DISABLED)
      


        def filtrarInventario():
            print("si funciona el de arriba este puede que también jasjasja")

        def agregarProducto():
            print("Esto funciona?")
        
        def actualizarStock():
            print("Esto funciona?")

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

