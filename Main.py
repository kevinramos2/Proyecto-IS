import tkinter as tk
import sys
from GestorAplicacion import InventarioDoubleList, Producto
from GestorAplicacion.LogIn import LogIn
from usuarios.Administrador import Administrador
from usuarios.Decoradora import Decoradora
from usuarios.Despachadora import Despachadora
from usuarios.Fabricador import Fabricador
from BaseDeDatos.deserializador import Deserializador
from BaseDeDatos.serializador import Serializador
from GestorAplicacion.InventarioDoubleList import InventarioDoubleList
from GestorAplicacion.Producto import Producto
from GestorGrafico.LogInGrafico import LogInGrafico


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Agario Solutions")
        self.resizable(0,0)
        self.geometry("865x625")
        

        Login_Frame = LogInGrafico(self)
        


if __name__ == "__main__":
    Deserializador.Deserializar()

    # despachadora1 = Despachadora("Tomas",1025,"123")
    # admin1 = Administrador("Kevin",1036,"987")
    # fabricador1 = Fabricador("Alejandro", 1098, "hola")
    # decoradora1 = Decoradora("Juan", 6785, "kkkk")
    
    # # Crear productos
    # p1 = Producto("Velón #6", "001", 10, "Velon", 2500, "Blanco",None)
    
    # p2 = Producto("Velón #6", "002", 10, "Velon", 2500, "Azul",None)

    # p3 =  Producto("Velón #6", "003", 10, "Velon", 2500, "Rojo",None)
  
    # p4 =  Producto("Velón #6", "004", 10, "Velon",  2500,"Amarillo",None)
  
    # p5 =  Producto("Velón #15", "011", 10, "Velon", 6000,"Blanco",None)
   
    # p6 =  Producto("Velón #15", "012", 10, "Velon",  6000,"Azul",None)
    
    # p7 =  Producto("Velón #15", "013", 10, "Velon",  6000,"Rojo",None)
    
    # p8 =  Producto("Velón #15", "014", 10, "Velon", 6000,"Amarillo",None )
    
    # p9 =  Producto("Velón #25", "021", 10, "Velon",  15000,"Blanco",None)
 
    # p10 = Producto("Velón #25", "022", 10, "Velon",  15000,"Azul",None)
 
    # p11 = Producto("Velón #25", "023", 10, "Velon",  15000,"Rojo",None)

    # p12 = Producto("Velón #25", "024", 10, "Velon",  15000,"Amarillo",None)
    
    # p13 = Producto("Vela Lisa Blanca", "111", 10, "Vela Lisa",  6000,"Blanco",None)
 
    # p14 = Producto("Vela Lisa Azul", "112", 10, "Vela Lisa", 6000,"Azul",None)
    
    # p15 = Producto("Vela Lisa Roja", "113", 10, "Vela Lisa", 6000, "Rojo",None)

    # p16 = Producto("Vela Lisa Amarilla", "114", 10, "Vela Lisa", 6000, "Amarillo",None)
 
    # p17 = Producto("Vela Lisa Baby Blanca", "121", 10, "Vela Lisa Baby",  9000,"Blanco",None)

    # p18 = Producto("Vela Lisa Baby Azul", "122", 10, "Vela Lisa Baby",  9000,"Azul",None)

    # p19 = Producto("Vela Lisa Baby Roja", "123", 10, "Vela Lisa Baby",  9000,"Rojo",None)

    # p20 = Producto("Vela Lisa Baby Amarilla", "124", 10, "Vela Lisa Baby", 9000,"Amarillo",None)
 
    # p21 = Producto("Esencia de Maracuyá", "201", 10, "Esencia",3000,None,"Maracuyá")
  
    # p22 = Producto("Esencia de Mandarina", "202", 10, "Esencia",3000,None,"Mandarina",)
    
    # p23 = Producto("Esencia de Kiwi", "203", 10, "Esencia",3000,None,"Kiwi")
    
    # p24 = Producto("Esencia de Naranja", "204", 10, "Esencia",3000,None,"Naranja")
    
    # p25 = Producto("Esencia de Coco", "205", 10, "Esencia",3000,None,"Coco")
    
    # p26 = Producto("Esencia de Talco", "206", 10, "Esencia",3000,None,"Talco")
    
    # p27 = Producto("Esencia Chicle", "207", 10, "Esencia",3000,None,"Chicle")
   
    # p28 = Producto("Esencia de Tutti Frutti", "208", 10, "Esencia",3000,None,"Tutti Frutti")
   
    # p29 = Producto("Esencia de Frutos Rojos","209", 10, "Esencia", 3000,None,"Frutos Rojos")

    # p30 = Producto("Esencia de Canela", "210", 10, "Esencia",3000,None,"Canela")
    
    # Serializador.Serializar()
    #LogIn.ImprimirLogIn()
    window  = MainWindow()
    window.mainloop()


