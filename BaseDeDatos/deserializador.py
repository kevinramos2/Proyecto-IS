import pickle
from usuarios.Empleado import Empleado
from GestorAplicacion.Producto import Producto

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
    def Deserializar(cls):
        Deserializador.deserializarEmpleados()
        Deserializador.deserializarProductos()