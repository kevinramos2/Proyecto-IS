from GestorAplicacion.Venta import Venta
from usuarios.Empleado import Empleado
from usuarios.Despachadora import Despachadora

class Caja:

    def __init__(self):
        self.estadocaja = False

    def abrir_caja(self, empleado):
        #Abre la caja solo si es la esclava de la despachadora.
        if isinstance(empleado, Despachadora):
            self.estadocaja = True
            return True
        else:
            return False

    def cerrar_caja(self):
        if self.estadocaja == True:
            self.estadocaja = False
            return True
        else:
            return False
    
    def estado_caja(self):
        return self.estadocaja

