from usuarios.Empleado import Empleado

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
    def verificarCredenciales(cls,id,contraseña) -> bool:
        credencialesValidas = False
        for usuario in Empleado.getTodolosUsuarios():
            if usuario.getContraseña() == contraseña and usuario.getId() == id:
                credencialesValidas = True
            
            return credencialesValidas

    
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
            else:
                print("Lo sentimos las credenciales no son correctas, intente nuevamente...")
        




