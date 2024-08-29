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





if __name__ == "__main__":
    #despachadora1 = Despachadora("Tomas",1025,"123")
    #admin1 = Administrador("Kevin",1036,"987")
    #fabricador1 = Fabricador("Alejandro", 1098, "hola")
    #decoradora1 = Decoradora("Juan", 6785, "kkkk")
    #Serializador.serializarEmpleados()
    Deserializador.deserializarEmpleados()
    LogIn.ImprimirLogIn()

    inventario = InventarioDoubleList()

    # Crear productos
    p1 = Producto("Velón #6", 123, 10, "Velon", 2500, "Blanco",None)
    inventario.agregar(p1)
    p2 = Producto("Velón #6", 123, 10, "Velon", 2500, "Azul",None)
    inventario.agregar(p2)
    p3 =  Producto("Velón #6", 123, 10, "Velon", 2500, "Rojo",None)
    inventario.agregar(p3)
    p4 =  Producto("Velón #6", 123, 10, "Velon",  2500,"Amarillo",None)
    inventario.agregar(p4)
    p5 =  Producto("Velón #15", 123, 10, "Velon", 6000,"Blanco",None)
    inventario.agregar(p5)
    p6 =  Producto("Velón #15", 123, 10, "Velon",  6000,"Azul",None)
    inventario.agregar(p6)
    p7 =  Producto("Velón #15", 123, 10, "Velon",  6000,"Rojo",None)
    inventario.agregar(p7)
    p8 =  Producto("Velón #15", 123, 10, "Velon", 6000,"Amarillo",None )
    inventario.agregar(p8)
    p9 =  Producto("Velón #25", 123, 10, "Velon",  15000,"Blanco",None)
    inventario.agregar(p9)
    p10 = Producto("Velón #25", 123, 10, "Velon",  15000,"Azul",None)
    inventario.agregar(p10)
    p11 = Producto("Velón #25", 123, 10, "Velon",  15000,"Rojo",None)
    inventario.agregar(p11)
    p12 = Producto("Velón #25", 123, 10, "Velon",  15000,"Amarillo",None)
    inventario.agregar(p12)
    p13 = Producto("Vela Lisa Blanca", 123, 10, "Vela Lisa",  6000,"Blanco",None)
    inventario.agregar(p13)
    p14 = Producto("Vela Lisa Azul", 123, 10, "Vela Lisa", 6000,"Azul",None)
    inventario.agregar(p14)
    p15 = Producto("Vela Lisa Roja", 123, 10, "Vela Lisa", 6000, "Rojo",None)
    inventario.agregar(p15)
    p16 = Producto("Vela Lisa Amarilla", 123, 10, "Vela Lisa", 6000, "Amarillo",None)
    inventario.agregar(p16)
    p17 = Producto("Vela Lisa Baby Blanca", 123, 10, "Vela Lisa Baby",  9000,"Blanco",None)
    inventario.agregar(p17)
    p18 = Producto("Vela Lisa Baby Azul", 123, 10, "Vela Lisa Baby",  9000,"Azul",None)
    inventario.agregar(p18)
    p19 = Producto("Vela Lisa Baby Roja", 123, 10, "Vela Lisa Baby",  9000,"Rojo",None)
    inventario.agregar(p19)
    p20 = Producto("Vela Lisa Baby Amarilla", 123, 10, "Vela Lisa Baby", 9000,"Amarillo",None)
    inventario.agregar(p20)
    p21 = Producto("Esencia de Maracuyá", 123, 10, "Esencia",3000,None,"Maracuyá")
    inventario.agregar(p21)
    p22 = Producto("Esencia de Mandarina", 123, 10, "Esencia",3000,None,"Mandarina",)
    inventario.agregar(p22)
    p23 = Producto("Esencia de Kiwi", 123, 10, "Esencia",3000,None,"Kiwi")
    inventario.agregar(p23)
    p24 = Producto("Esencia de Naranja", 123, 10, "Esencia",3000,None,"Naranja")
    inventario.agregar(p24)
    p25 = Producto("Esencia de Coco", 123, 10, "Esencia",3000,None,"Coco")
    inventario.agregar(p25)
    p26 = Producto("Esencia de Talco", 123, 10, "Esencia",3000,None,"Talco")
    inventario.agregar(p26)
    p27 = Producto("Esencia Chicle", 123, 10, "Esencia",3000,None,"Chicle")
    inventario.agregar(p27)
    p28 = Producto("Esencia de Tutti Frutti", 123, 10, "Esencia",3000,None,"Tutti Frutti")
    inventario.agregar(p28)
    p29 = Producto("Esencia de Frutos Rojos",123, 10, "Esencia", 3000,None,"Frutos Rojos")
    inventario.agregar(p29)
    p30 = Producto("Esencia de Canela", 123, 10, "Esencia",3000,None,"Canela")
    inventario.agregar(p30)

    print("Bienvenido al inventario de Fábrica de Velas Manare")
    filtro = input("¿Deseas ver los productos por categoría? (Si/No)\n---> ")

    if filtro.lower() == "si":
        categoria_filtro = input("Escribe la categoría\n---> ")
        inventario.mostrar_por_categoria(categoria_filtro)
    else:
        inventario.mostrar_completo()
