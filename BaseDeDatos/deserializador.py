import pickle
from usuarios.Empleado import Empleado
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta
from GestorAplicacion.Gasto import Gasto

class Deserializador:

    @classmethod
    def deserializarEmpleados(cls):
        with open('BaseDeDatos/temp/Empleados.pkl','rb') as file:
            lista_objetos = pickle.load(file)
            Empleado.setTodoLosUsuarios(lista_objetos)
    
    @classmethod
    def deserializarProductos(cls):
        with open('BaseDeDatos/temp/Productos.pkl','rb') as file:
            lista_objetos = pickle.load(file)
            Producto.inventario = lista_objetos

    @classmethod
    def deserializarVentas(cls):
        with open('BaseDeDatos/temp/Ventas.pkl','rb') as file:
            lista_objetos = pickle.load(file)
            Venta._todas_las_ventas = lista_objetos

    @classmethod
    def deserializarGastos(cls):
        with open('BaseDeDatos/temp/Gastos.pkl','rb') as file:
            lista_objetos = pickle.load(file)
            Gasto._todos_los_gastos = lista_objetos
    
    @classmethod
    def Deserializar(cls):
        Deserializador.deserializarEmpleados()
        Deserializador.deserializarProductos()
        Deserializador.deserializarVentas()
        Deserializador.deserializarGastos()