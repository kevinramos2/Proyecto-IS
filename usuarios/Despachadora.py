from usuarios.Empleado import Empleado
class Despachadora(Empleado):

    # CONSTRUCTOR
    def __init__(self, nombre, id, contraseña):
        super().__init__(nombre, id, contraseña)