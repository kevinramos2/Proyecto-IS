from usuarios.Empleado import Empleado
from usuarios.Administrador import Administrador

class LogIn:

    @classmethod
    def verificarEntradaID(cls) -> int:
        numero = 0
        entradaValida = False

        while not entradaValida:
            try:
                inputNumero = input("ID: ")
                numero = int(inputNumero)
                entradaValida = True
            except:
                print("Entrada no válida. Por favor, ingrese un número válido:")
        
        return numero 
    
    @classmethod
    def verificarCredenciales(cls,id,contraseña) -> Empleado:
        credencialesValidas = False
        tempEmpleado = Empleado.buscarUsuario(id)
        if tempEmpleado is not None and tempEmpleado.getContraseña() == contraseña:
            credencialesValidas = True
        return credencialesValidas

    @classmethod
    def verificarAdmin(cls,empleado):
        if isinstance(empleado, Administrador):
            LogIn.MenuAdministrador(empleado)
        else:
            LogIn.MenuEmpleados(empleado)

    @classmethod
    def MenuEmpleados(cls, empleado):
        print()
        print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
        print("-------------- Empleado --------------")
        print()
        print("Seleccione alguna de las siguientes opciones: ")
        print("1) Revisar Bandeja de Entrada.")
        print("")
        print("")

    @classmethod
    def MenuAdministrador(cls, empleado):
        print()
        print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
        print("-------------- Administrador --------------")
        print()
        print("Seleccione alguna de las siguientes opciones: ")
        print("1) Revisar Bandeja de Entrada.")
        print("2) Enviar mensaje.")
        print("3) Inventario")

    
    @classmethod
    def ImprimirLogIn(cls):
        tempContraseña = None
        tempId = 0
        credencialesValidas = False

        print("-----Bienvenido al Log In de la Fabrica de Velas Manare-----")
        print("Porfavor digite su ID y contraseña:")

        while not credencialesValidas:
            tempId = LogIn.verificarEntradaID()

            tempContraseña = input("Contraseña: ")

            credencialesValidas = LogIn.verificarCredenciales(tempId,tempContraseña)

            if credencialesValidas:
                print("Credenciales Validas, Puede ingresar al sistema")

                LogIn.verificarAdmin(Empleado.buscarUsuario(tempId))

            else:
                print("Lo sentimos las credenciales no son correctas, intente nuevamente...")
        




