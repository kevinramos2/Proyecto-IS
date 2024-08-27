from GestorAplicacion.LogIn import LogIn
from usuarios.Empleado import Empleado
from BaseDeDatos.deserializador import Deserializador
from BaseDeDatos.serializador import Serializador


if __name__ == "__main__":
    #persona1 = Empleado("Tomas",1025,"123")
    #Serializador.serializarEmpleados()
    Deserializador.deserializarEmpleados()
    LogIn.ImprimirLogIn()
