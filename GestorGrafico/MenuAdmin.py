import tkinter as tk
from tkinter import *
from GestorGrafico.MenuInventario import MenuInventario
from GestorGrafico.MenuReporte import MenuReporte
from tkinter import messagebox
from GestorAplicacion.DoubleList import DoubleList
from GestorAplicacion.InventarioDoubleList import InventarioDoubleList
from GestorAplicacion.Producto import Producto 
from BaseDeDatos.serializador import Serializador 

class MenuAdmin(Frame):
    def __init__(self, ventana, empleado):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.empleado = empleado
        self.ventana = ventana
        self.inventario = InventarioDoubleList()  # Instancia del inventario

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#1B263B", padx=5, pady=5)
        LabelFrame.pack(side="top", fill="x")

        mensaje = f"Bienvenido de vuelta {self.empleado.getNombre()} | Menu Principal"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "italic underline"),bg="#1B263B" , fg = "white")
        mensajeBienv.pack(side="left")

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


        # Frame que va a contener todas las funcionalidades del Administrador
        self.FrameFuncionalidades = Frame(self, height= 400, width= 500, bg="#415A77")
        self.FrameFuncionalidades.pack_propagate(False)
        self.FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)

        # Definimos funciones para cada botón
        #def abrirInventario():
        #    self.mostrarMenuInventario()
#
        #def verReporteVentas():
        #    self.mostrarMenuReporteVentas()
#
        #def enviarMensaje():
        #    self.mostrarMenuEnviarMensaje()
#
        #def revisarMensaje():
        #    self.mostrarMenuRevisarMensaje()

        # Funciones para las opciones
        def AbrirMenuReporte():
            self.destroy()
            MenuReporte(self.ventana, self.empleado)


        def AbrirMenuInventario():
            self.destroy()
            MenuInventario(self.ventana, self.empleado)



        # Botones de funcionalidades
        botonInventario = Button(
            self.FrameFuncionalidades, 
            text="Inventario",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command= AbrirMenuInventario)
        
        botonInventario.pack(fill="x", side="top",expand=True, padx= 5)

        botonReportes = Button(
            self.FrameFuncionalidades, 
            text="Reportes",
            bg="#E0E1DD",
            font=("Arial", 20, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command= AbrirMenuReporte)
        
        botonReportes.pack(fill="x", side="top",expand=True, padx=5)


    #def mostrarMenuInventario(self):
    #    # Elimina el frame de funcionalidades actual
    #    self.FrameFuncionalidades.pack_forget()
#
    #    # Crear un nuevo frame para el menú de inventario
    #    inventarioGrande = Frame(self, bg='#E0E1DD')
    #    inventarioGrande.pack(fill="both", expand=True)
#
#
#
    #    self.inventarioFrame = Frame(inventarioGrande, bg="#1B263B",height=400, width=500)
    #    self.inventarioFrame.pack(fill="y", expand=True)
    #    self.inventarioFrame.pack_propagate(False)
#
    #    
    #    # Título
    #    tituloLabel = Label(self.inventarioFrame, text="Inventario", font=("Arial", 25, "bold"), bg="#1B263B", fg="white")
    #    tituloLabel.pack(pady=10)
#
    #    # Opciones del inventario
    #    botonAgregar = Button(self.inventarioFrame, text="Crear Producto", bg="#E0E1DD", font=("Arial", 15), command=self.agregarProducto)
    #    botonAgregar.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    botonBuscar = Button(self.inventarioFrame, text="Modificar Stock", bg="#E0E1DD", font=("Arial", 15), command=self.buscarProducto)
    #    botonBuscar.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    botonEliminar = Button(self.inventarioFrame, text="Eliminar Producto", bg="#E0E1DD", font=("Arial", 15), command=self.eliminarProducto)
    #    botonEliminar.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    botonMostrar = Button(self.inventarioFrame, text="Ver Inventario", bg="#E0E1DD", font=("Arial", 15), command=self.mostrarInventario)
    #    botonMostrar.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    # Boton para volver al menu principal
    #    ImagenHome = "BaseDeDatos\Imagenes\home-solid-36.png"
    #    foto = tk.PhotoImage(file=ImagenHome)
#
    #    MenuPrincipalBoton = Button(LabelFrame, image=foto, command=lambda: self.volverMenu(self.inventarioFrame))
    #    MenuPrincipalBoton.image = foto
    #    MenuPrincipalBoton.pack(side="right")
#
#
    #def volverMenu(self, frameAnterior):
    #    # Elimina el frame actual (frameAnterior) y vuelve a mostrar las funcionalidades principales
    #    frameAnterior.pack_forget()
    #    self.FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)
    #
    ## Métodos para inventario
    #def agregarProducto(self):
    #    # Crear ventana emergente para ingresar los datos del producto
    #    agregarWin = Toplevel(self)
    #    agregarWin.title("Agregar Producto")
    #    
    #    # Etiquetas y campos de entrada
    #    Label(agregarWin, text="Nombre:").grid(row=0, column=0)
    #    nombre = Entry(agregarWin)
    #    nombre.grid(row=0, column=1)
#
    #    Label(agregarWin, text="Referencia:").grid(row=1, column=0)
    #    referencia = Entry(agregarWin)
    #    referencia.grid(row=1, column=1)
#
    #    Label(agregarWin, text="Stock:").grid(row=2, column=0)
    #    stock = Entry(agregarWin)
    #    stock.grid(row=2, column=1)
#
    #    Label(agregarWin, text="Categoría:").grid(row=3, column=0)
    #    categoria = Entry(agregarWin)
    #    categoria.grid(row=3, column=1)
#
    #    Label(agregarWin, text="Precio:").grid(row=4, column=0)
    #    precio = Entry(agregarWin)
    #    precio.grid(row=4, column=1)
#
    #    Label(agregarWin, text="Color (si aplica):").grid(row=5, column=0)
    #    color = Entry(agregarWin)
    #    color.grid(row=5, column=1)
#
    #    Label(agregarWin, text="Aroma (si aplica):").grid(row=6, column=0)
    #    aroma = Entry(agregarWin)
    #    aroma.grid(row=6, column=1)
#
    #    # Botón para agregar
    #    Button(agregarWin, text="Agregar", command=lambda: self.guardarProducto(agregarWin, nombre.get(), referencia.get(), stock.get(), categoria.get(), precio.get(), color.get(), aroma.get())).grid(row=7, column=0, columnspan=2)
#
    #def guardarProducto(self, ventana, nombre, referencia, stock, categoria, precio, color, aroma):
    #    # Crear y agregar el producto al inventario
    #    try:
    #        producto = Producto(nombre, referencia, int(stock), categoria, float(precio), color, aroma)
    #        print(producto.__str__())
    #        messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado exitosamente.")
    #        ventana.destroy()  # Cierra la ventana después de agregar el producto
    #    except Exception as e:
    #        messagebox.showerror("Error", f"Error al agregar el producto: {e}")
#
    #def buscarProducto(self):
    #    buscarWin = Toplevel(self)
    #    buscarWin.title("Buscar Producto")
    #    
    #    Label(buscarWin, text="Referencia del Producto:").grid(row=0, column=0)
    #    referencia = Entry(buscarWin)
    #    referencia.grid(row=0, column=1)
#
    #    Button(buscarWin, text="Buscar", command=lambda: self.mostrarProducto(buscarWin, referencia.get())).grid(row=1, column=0, columnspan=2)
#
    #def mostrarProducto(self, ventana, referencia):
    #    producto = self.inventario.buscar_producto(referencia)
    #    if producto:
    #        messagebox.showinfo("Producto Encontrado", str(producto))
    #    else:
    #        messagebox.showerror("Error", "Producto no encontrado.")
    #    ventana.destroy()
#
    #def eliminarProducto(self):
    #    eliminarWin = Toplevel(self)
    #    eliminarWin.title("Eliminar Producto")
    #    
    #    Label(eliminarWin, text="Referencia del Producto:").grid(row=0, column=0)
    #    referencia = Entry(eliminarWin)
    #    referencia.grid(row=0, column=1)
#
    #    Button(eliminarWin, text="Eliminar", command=lambda: self.eliminarProductoInventario(eliminarWin, referencia.get())).grid(row=1, column=0, columnspan=2)
#
    #def eliminarProductoInventario(self, ventana, referencia):
    #    producto = self.inventario.buscar(referencia)
    #    if producto:
    #        self.inventario.eliminar(producto)
    #        messagebox.showinfo("Éxito", f"Producto '{producto.get_nombre()}' eliminado exitosamente.")
    #    else:
    #        messagebox.showerror("Error", "Producto no encontrado.")
    #    ventana.destroy()
#
    #def mostrarInventario(self):
    #    # Elimina el frame de funcionalidades actual
    #    self.inventarioFrame.pack_forget()
    #    
    #    # Crear un nuevo frame para el menú de inventario
    #    inventarioFrame2 = Frame(self, bg="#1B263B")
    #    inventarioFrame2.pack(fill="both", expand=True)
#
    #    # Título
    #    tituloLabel = Label(inventarioFrame2, text="Inventario", font=("Arial", 25, "bold"), bg="#1B263B", fg="white")
    #    tituloLabel.pack(pady=10)
#
    #    # Opciones del inventario
    #    botonFiltrar = Button(inventarioFrame2, text="Filtrar Inventario", bg="#E0E1DD", font=("Arial", 15), command=self.agregarProducto)
    #    botonFiltrar.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    botonCompleto = Button(inventarioFrame2, text="Ver Inventario Completo", bg="#E0E1DD", font=("Arial", 15), command=self.buscarProducto)
    #    botonCompleto.pack(fill="x", side="top", expand=True, padx=5, pady=5)
#
    #    # Botón para volver al menú principal
    #    botonVolver = Button(inventarioFrame2, text="Volver", bg="#E0E1DD", font=("Arial", 15), command=lambda: self.volverMenu(inventarioFrame2))
    #    botonVolver.pack(pady=10)
#
#
#
#
    #def volverMenu(self, frameActual):
    #    # Destruir el frame actual
    #    frameActual.pack_forget()
#
    #    # Volver a mostrar el frame de funcionalidades
    #    self.FrameFuncionalidades.pack(fill="y", expand=True, pady=5, padx=5)
#