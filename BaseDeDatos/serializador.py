import pickle
from usuarios.Empleado import Empleado
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta
from GestorAplicacion.Gasto import Gasto

class Serializador:

    @classmethod
    def serializarEmpleados(cls,lista_objetos):
        with open('BaseDeDatos/temp/Empleados.pkl','wb') as file:
            pickle.dump(lista_objetos,file)
    
    @classmethod
    def serializarProductos(cls,lista_objetos):
        with open('BaseDeDatos/temp/Productos.pkl','wb') as file:
            pickle.dump(lista_objetos,file)
    @classmethod
    def serializarVentas(cls,lista_objetos):
        with open('BaseDeDatos/temp/Ventas.pkl','wb') as file:
            pickle.dump(lista_objetos,file)

    @classmethod
    def serializarGastos(cls, lista_objetos):
        with open('BaseDeDatos/temp/Gastos.pkl','wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def Serializar(cls):
        Serializador.serializarEmpleados(Empleado.getTodolosUsuarios())
        Serializador.serializarProductos(Producto.inventario)
        Serializador.serializarVentas(Venta._todas_las_ventas)
        Serializador.serializarGastos(Gasto._todos_los_gastos)