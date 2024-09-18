from tkinter import *
try:
    from PIL import Image, ImageTk
    image_lib_avaible = True
except ImportError:
    image_lib_avaible = False
    print("El módulo PIL (Pillow) no está instalado. Algunas funcionalidades pueden no estar disponibles.")

import tkinter as tk
from GestorAplicacion.LogIn import LogIn
from tkinter import messagebox


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

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame para el Mensaje de Bienvenida
        LabelFrame = Frame(self, height=100, bg="#415A77", padx=5, pady=5)
        LabelFrame.grid(row=0, column=0, sticky="ew")

        mensaje = "Bienvenidos al Sistema de Fabrica Velas Manare"
        mensajeBienv = Label(LabelFrame, text=mensaje, font=("arial", 20, "bold"),bg="#E0E1DD" , fg = "black")
        mensajeBienv.pack(expand=True)

        # Frame para el log-in
        LogInFrame = Frame(self, height= 350, width= 500, bg="#778DA9")
        LogInFrame.grid(row= 1, column= 0, padx=10, pady=10)
        
        if image_lib_avaible:
            try:
                ImagenUsuarioCircular = Image.open("BaseDeDatos/Imagenes/user-circle-regular-120.png")

                foto = ImageTk.PhotoImage(ImagenUsuarioCircular)

                LabelImagen = Label(LogInFrame, image= foto, bg="#778DA9")
                LabelImagen.image = foto
                LabelImagen.pack(pady=(75,0))

            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

        FrameAuxiliar = Frame(LogInFrame,bg="#778DA9" )
        FrameAuxiliar.pack(padx=150, pady=(10,100))
        # Etiqueta para el id del usario
        self.EntryId = PlaceHolderEntry(FrameAuxiliar, placeholder="ID", width= 40, bd =5, bg = "#E0E1DD")
        self.EntryId.grid(row=1, column=1,padx=10, pady=10, ipadx=2, ipady=2)

        # Etiqueta para la contraseña
        self.EntryContraseña = PlaceHolderEntry(FrameAuxiliar, placeholder="Contraseña", width=40, bd = 5, bg= "#E0E1DD")
        self.EntryContraseña.grid(row=2, column=1,padx=10, pady=10,ipadx=2, ipady=2)

        if image_lib_avaible:
            try:
                ImagenUsuarioEntry = Image.open("BaseDeDatos/Imagenes/user-solid-24.png")

                foto2 = ImageTk.PhotoImage(ImagenUsuarioEntry)
                LabelImagenUserEntry = Label(FrameAuxiliar, image=foto2, bg="#778DA9")
                LabelImagenUserEntry.image = foto2
                LabelImagenUserEntry.grid(row=1, column=0, padx=2)

                ImagenLockEntry = Image.open("BaseDeDatos/Imagenes/lock-alt-solid-24.png")

                foto3 = ImageTk.PhotoImage(ImagenLockEntry)
                LabelImagenLockEntry = Label(FrameAuxiliar, image=foto3, bg="#778DA9")
                LabelImagenLockEntry.image = foto3
                LabelImagenLockEntry.grid(row=2, column=0, padx=2)

            except Exception as e:
                print(f"Error al cargar la imagen: {e}")

        

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

    def login(self):
        id_Usuario = self.EntryId.get()
        contraseña_Usuario = self.EntryContraseña.get()
        print(type(id_Usuario))
        print(type(contraseña_Usuario))

        NumeroIdUser = 0 

        try:
            NumeroIdUser = int(id_Usuario)
        except:
            messagebox.showerror("Login", "Ingrese un id valido")

        CredencialesCorrectas = LogIn.verificarCredenciales(NumeroIdUser, contraseña_Usuario)
            
        if CredencialesCorrectas:
            messagebox.showinfo("Login", "Login correcto, puede ingresar")
        else:
            messagebox.showerror("Login", "Id o contraseña invalidas")


        
