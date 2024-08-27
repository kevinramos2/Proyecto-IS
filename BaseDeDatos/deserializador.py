import pickle
from usuarios.Empleado import Empleado

class Deserializador:

    @classmethod
    def deserializarEmpleados(cls):
        with open('BaseDeDatos\\temp\\Empleados.pkl','rb') as file:
            lista_objetos = pickle.load(file)
            Empleado.setTodoLosUsuarios(lista_objetos)