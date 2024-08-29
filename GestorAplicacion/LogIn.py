from GestorAplicacion.Caja import Caja
from GestorAplicacion.Producto import Producto
from usuarios.Empleado import Empleado
from usuarios.Administrador import Administrador
from usuarios.Decoradora import Decoradora
from usuarios.Despachadora import Despachadora
from usuarios.Fabricador import Fabricador
from GestorAplicacion.Venta import Venta
from BaseDeDatos.serializador import Serializador
from BaseDeDatos.deserializador import Deserializador

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
        elif isinstance(empleado, Decoradora):
            LogIn.MenuDecoradora(empleado)
        elif isinstance(empleado, Fabricador):
            LogIn.MenuFabricador(empleado)
        else:
            LogIn.MenuDespachadora(empleado)
    
    @classmethod
    def MenuDecoradora(cls,empleado):
        while True:
            print()
            print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
            print("-------------- Decoradora --------------")
            print()
            print("Seleccione alguna de las siguientes opciones: ")
            print("1) Revisar Bandeja de Entrada.")
            print("2) Enviar mensaje.")
            print("3) Cerrar Sesión")
            opcion = input("Ingrese una opción: ")

            if(opcion == "1"):
                print("WORK IN PROGRESS...")
            if(opcion == "2"):
                print("WORK IN PROGRESS...")
            if(opcion == "3"):
                print("Cerrando Sesión...")
                break
        LogIn.ImprimirLogIn()

    @classmethod
    def MenuFabricador(cls,empleado):
        while True:
            print()
            print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
            print("-------------- Fabricador --------------")
            print()
            print("Seleccione alguna de las siguientes opciones: ")
            print("1) Revisar Bandeja de Entrada.")
            print("2) Enviar mensaje.")
            print("3) Cerrar Sesión")
            opcion = input("Ingrese una opción: ")

            if(opcion == "1"):
                print("WORK IN PROGRESS...")
            if(opcion == "2"):
                print("WORK IN PROGRESS...")
            if(opcion == "3"):
                print("Cerrando Sesión...")
                break
        LogIn.ImprimirLogIn()

            
    @classmethod
    def MenuDespachadora(cls, empleado):
        caja = Caja() #Instancia de Caja
       
        while True:
            print()
            print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
            print("-------------- Despachadora --------------")
            print()
            print("Seleccione alguna de las siguientes opciones: ")
            print("1) Revisar Bandeja de Entrada.")
            print("2) Enviar mensaje")
            print("3) Registrar venta")
            print("4) Abrir Caja")
            print("5) Cerrar Caja")
            print("6) Consultar Estado De La Caja")
            print("7) Cerrar Sesión")
            opcion = input("Ingresa una opción: ")

            if(opcion == "1"):
                print("WORK IN PROGRESS...")

            if(opcion == "2"):
                print("WORK IN PROGRESS...")
    
            if(opcion == '3'):
                if caja.estado_caja() == True:
                    venta = Venta()
                    venta.registrar_venta(empleado)
                else:
                    print("===============================================================")
                    print("+ No se puede registrar la venta porque la caja esta cerrada. +")
                    print("===============================================================")
            elif (opcion == "4"):
            
                if caja.abrir_caja(empleado) == True:
                    print()
                    print("=================")
                    print("+ Caja Abierta. +")
                    print("=================")
                else:
                    print()
                    print("=================")
                    print("+ Caja Cerrada. +")
                    print("=================")
    
            elif (opcion == "5"):
            
                if caja.cerrar_caja() == False:
                    print()
                    print("=================")
                    print("+ Caja Cerrada. +")
                    print("=================")
                else:
                    print()
                    print("============================")
                    print("+ La caja ya esta cerrada. +")
                    print("============================")
            
            elif (opcion == "6"):
            
                if caja.estado_caja() == True:
                    print()
                    print("=========================")
                    print("+ La Caja está abierta. +")
                    print("=========================")
                else:
                    print("=========================")
                    print("+ La caja está cerrada. +")
                    print("=========================")
            
            elif (opcion == "7"):
                print("=========================")
                print("+   Cerrando Sesión...  +")
                print("=========================")
                Serializador.Serializar()
                break
        LogIn.ImprimirLogIn()
                
    @classmethod
    def MenuAdministrador(cls, empleado):
        while True:
            print()
            print(f"--------- Bienvenido de nuevo {empleado.getNombre().upper()} ---------")
            print("-------------- Administrador --------------")
            print()
            print("Seleccione alguna de las siguientes opciones: ")
            print("1) Inventario")
            print("2) Enviar mensaje.")
            print("3) Revisar Bandeja")
            print("4) Reportes de ventas")
            print("5) Cerrar Sesión")

            opcion = input("Ingresa una opción: ")

            if(opcion == "1"):
            
                    print("Bienvenido al inventario de Fábrica de Velas Manare")
                    filtro = input("¿Deseas ver los productos por categoría? (Si/No)\n---> ")

                    if filtro.lower() == "si":
                        categoria_filtro = input("Escribe la categoría\n---> ")
                        Producto.inventario.mostrar_por_categoria(categoria_filtro)
                    else:
                        Producto.inventario.mostrar_completo()

            elif (opcion == "2"):
            
                print("WORK IN PROGRESS...")

            elif (opcion == "3"):
            
                print("WORK IN PROGRESS...")

            elif (opcion == "4"):
            
                print("WORK IN PROGRESS...")

            elif (opcion == "5"):
                print("=========================")
                print("+   Cerrando Sesión...  +")
                print("=========================")
                Serializador.Serializar()
                break
        LogIn.ImprimirLogIn()
        
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
        




