from tkinter import *
import tkinter as tk
from GestorAplicacion.LogIn import LogIn
from usuarios.Empleado import Empleado
from usuarios.Administrador import Administrador
from usuarios.Decoradora import Decoradora
from usuarios.Fabricador import Fabricador
from usuarios.Despachadora import Despachadora
from tkinter import messagebox
from GestorGrafico.MenuAdmin import MenuAdmin
from GestorGrafico.MenuDespachadora import MenuDespachadora

class PlaceHolderEntry(Entry):
    def __init__(self, parent, placeholder="", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.placeholder = placeholder
        self.default_fg_color = self.cget('fg')
        self.placeholder_fg_color = 'grey'
        self._set_placeholder()
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

    def _set_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_fg_color)

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self._set_placeholder()

class LogInGrafico(Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.config(bg="#E0E1DD", width=400, height=350)
        self.pack(fill="both",expand=True)
        self.ventana = ventana
        self.ventana.config(menu="")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Barra del Menu
        menuBar = Menu(self.ventana)
        self.ventana.option_add("*tearOff", False)
        self.ventana.config(menu=menuBar)

        #Menu para salir 
        menuSalir = Menu(menuBar)
        menuBar.add_cascade(label="Salir", menu=menuSalir, activebackground="#3A4D39")

        menuSalir.add_cascade(label="Salir de la aplicacion", activebackground="#3A4D39", command=self.ventana.destroy)


        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#415A77", padx=5, pady=5)
        LabelFrame.grid(row=0, column=0, sticky="ew")

        mensaje = "Bienvenidos al Sistema de Fabrica Velas Manare"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "bold"),bg="#E0E1DD" , fg = "black")
        mensajeBienv.pack(expand=True)

        # Frame para el log-in
        LogInFrame = Frame(self, height= 350, width= 500, bg="#778DA9")
        LogInFrame.grid(row= 1, column= 0, padx=10, pady=10)
        

        # Importar imagenes
        ImagenUsuarioCircular = "BaseDeDatos/Imagenes/user-circle-regular-120.png"

        foto = tk.PhotoImage(file=ImagenUsuarioCircular)

        LabelImagen = Label(LogInFrame, image= foto, bg="#778DA9")
        LabelImagen.image = foto
        LabelImagen.pack(pady=(75,0))


        FrameAuxiliar = Frame(LogInFrame,bg="#778DA9" )
        FrameAuxiliar.pack(padx=150, pady=(10,100))
        # Etiqueta para el id del usario
        self.EntryId = PlaceHolderEntry(FrameAuxiliar, placeholder="ID", width= 40, bd =5, bg = "#E0E1DD")
        self.EntryId.grid(row=1, column=1,padx=10, pady=10, ipadx=2, ipady=2)

        # Etiqueta para la contraseña
        self.EntryContraseña = PlaceHolderEntry(FrameAuxiliar, placeholder="Contraseña", width=40, bd = 5, bg= "#E0E1DD")
        self.EntryContraseña.grid(row=2, column=1,padx=10, pady=10,ipadx=2, ipady=2)

        
        # Importar imagenes
        ImagenUsuarioEntry = "BaseDeDatos/Imagenes/user-solid-24.png"

        foto2 = tk.PhotoImage(file=ImagenUsuarioEntry)
        LabelImagenUserEntry = Label(FrameAuxiliar, image=foto2, bg="#778DA9")
        LabelImagenUserEntry.image = foto2
        LabelImagenUserEntry.grid(row=1, column=0, padx=2)

        ImagenLockEntry = "BaseDeDatos/Imagenes/lock-alt-solid-24.png"

        foto3 = tk.PhotoImage(file=ImagenLockEntry)
        LabelImagenLockEntry = Label(FrameAuxiliar, image=foto3, bg="#778DA9")
        LabelImagenLockEntry.image = foto3
        LabelImagenLockEntry.grid(row=2, column=0, padx=2)


        ButtonLogIn = Button(
            FrameAuxiliar, 
            text= "Login", 
            bg="#E0E1DD",
            font=("Arial", 12, "bold"),
            width=10, 
            padx=2, 
            pady=2,
            command= self.login)
        
        ButtonLogIn.grid(row= 3, column=1, pady= 10)


    def centrar_ventana(self,ventana,ancho,alto):
        #Funcion para centrar una ventana en la pantalla
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def login(self):
        id_Usuario = self.EntryId.get()
        contraseña_Usuario = self.EntryContraseña.get()
        NumeroIdUser = 0 

        try:
            NumeroIdUser = int(id_Usuario)
        except:
            messagebox.showerror("Login", "Ingrese un id valido")
        else:  
            CredencialesCorrectas = LogIn.verificarCredenciales(NumeroIdUser, contraseña_Usuario)
            if CredencialesCorrectas:
                messagebox.showinfo("Login", "Login correcto, puede ingresar")

                UsuarioRegistrado = Empleado.buscarUsuario(NumeroIdUser)
                print(UsuarioRegistrado)
                
                if isinstance(UsuarioRegistrado, Administrador):
                    self.destroy()
                    MenuAdmin(self.ventana, UsuarioRegistrado)
                elif isinstance(UsuarioRegistrado, Despachadora):
                    self.destroy()
                    MenuDespachadora(self.ventana, UsuarioRegistrado)

                #elif isinstance(UsuarioRegistrado, Fabricador):
                    
                #else:
                    
            else:
                # ventana_emergente = tk.Toplevel(self)
                # ventana_emergente.title("Error al iniciar sesion.")
                # ventana_emergente.geometry("350x150")
                # ventana_emergente.config(bg="#e0e0e0")

                # # Centrar la ventana Toplevel en la pantalla
                # self.centrar_ventana(ventana_emergente,250,100)

                # # Añadir un mensaje dentro de la ventana
                # mensaje = tk.Label(ventana_emergente, text="Id o contraseña invalidas. Intente nuevamente.", bg="#e0e0e0", font=("Arial",12,"bold"), wraplength=200)
                # mensaje.pack(pady=10)

                # # Boton para cerrar la ventana emergente
                # boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command= ventana_emergente.destroy, bg="#007bff", fg="white", font=("Arial", 10, "bold"))
                # boton_cerrar.pack(pady=10)

                
                messagebox.showerror("Login", "Id o contraseña invalidas. Intente nuevamente.")


        
