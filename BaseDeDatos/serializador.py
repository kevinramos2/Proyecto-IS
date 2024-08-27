import pickle
from usuarios.Empleado import Empleado

class Serializador:

    @classmethod
    def serializarEmpleados(cls):
        with open('BaseDeDatos\\temp\\Empleados.pkl','wb') as file:
            pickle.dump(Empleado.getTodolosUsuarios(),file)