from GestorAplicacion.LogIn import LogIn
from usuarios.Administrador import Administrador
from usuarios.Decoradora import Decoradora
from usuarios.Despachadora import Despachadora
from usuarios.Fabricador import Fabricador
from BaseDeDatos.deserializador import Deserializador
from BaseDeDatos.serializador import Serializador


if __name__ == "__main__":
    #despachadora1 = Despachadora("Tomas",1025,"123")
    #admin1 = Administrador("Kevin",1036,"987")
    #fabricador1 = Fabricador("Alejandro", 1098, "hola")
    #decoradora1 = Decoradora("Juan", 6785, "kkkk")
    #Serializador.serializarEmpleados()
    Deserializador.deserializarEmpleados()
    LogIn.ImprimirLogIn()
