from datetime import datetime
from GestorAplicacion.Producto import Producto

class Venta:
    _todas_las_ventas = []
    PREFIJO_ID = 'V'  # Prefijo para los IDs de venta
    contador_id = 0  # Contador estático para IDs únicos

    def __init__(self, id_venta=None, id_cliente=None, productos=None, fecha=None, total=None, estado=True):
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_cliente = id_cliente
        self.productos = productos
        self.fecha = fecha
        self.total = total
        self.estado = True

        Venta._todas_las_ventas.append(self)

    @classmethod
    def crear_id_venta(cls):
        # Incrementa el contador y genera el ID con el prefijo
        cls.contador_id += 1
        id_venta = f"{cls.PREFIJO_ID}{cls.contador_id}"
        return id_venta
    
    def total_venta(self, productos):
        suma_total = 0
        for producto in productos:
            suma_total += producto[0].get_precio()*producto[1]
        return suma_total
    
    def actualizar_estado(self, estado):
        self.estado = estado
    
    def registrar_venta(self, despachadora):
        
        print("Registro de nueva venta")
        print("-----------------------")

        productos = []

        # Registrar el producto
        while True:
            id_producto = input("Ingrese el código de referencia del producto: ")
 
            producto = Producto.inventario.buscar_producto(id_producto)

            if(producto):
                cantidad_producto_requerido = input("Ingrese la cantidad del producto: ")
                if cantidad_producto_requerido.isdigit() and int(cantidad_producto_requerido) > 0:
                    cantidad_producto_requerido = int(cantidad_producto_requerido)
                    if producto.stock >= cantidad_producto_requerido:
                        productos.append((producto, cantidad_producto_requerido))
                        print("Producto agregado correctamente.")
                
                        # Preguntar si desea agregar más productos
                        agregar_mas = input("¿Desea agregar más productos? (Si/No): ")
                
                        if agregar_mas.lower() != "si":
                            break
                    else:
                        print(f"Solo hay {cantidad_producto_requerido - producto.exitencias} exitencias de este producto")
                else:
                    print("La cantidad de el producto debe ser un valor mayor a 0")
            else:
                print("El ID del producto no es valido")
        
        # Solicitar y validar ID del cliente
        while True:
            id_cliente = input("Ingrese el ID del cliente: ")
            if id_cliente.isdigit() and int(id_cliente) > 0:
                id_cliente = int(id_cliente)
                break
            else:
                print("El ID ingresado debe ser un número entero positivo.")
        
        # Seleccionar metodo de pago
        opciones_pago = {
            "1": "Transferencia",
            '2': 'Efectivo'
        }
        
        print("Seleccione el método de pago:")
        for clave, valor in opciones_pago.items():
            print(f"{clave}) {valor}")
        
        while True:
            seleccion = input("Ingrese el número de la opción deseada: ")
            if seleccion in opciones_pago:
                metodo_pago = opciones_pago[seleccion]
                break
            else:
                print("Opción no válida. Por favor, elija una opción del menú.")
        
        # Fecha de la venta realizada
        fecha_actual = datetime.now()

        # Generar id venta
        id_venta = self.crear_id_venta()
        
        # Total venta
        total_venta = self.total_venta(productos)

        #Confirmar pedido
        print("Confirmacion de venta")
        print("---------------------")
        print(f"atendido por: {despachadora.getNombre()}")
        print(f"ID venta: {id_venta}")
        print(f"ID Cliente: {id_cliente}")
        print(f"Fecha: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total: ${total_venta:.2f} COP")
        print("Productos: ")

        for producto, cantidad in productos:
            print(f"- {producto.nombre} (Cantidad: {cantidad})")
            
            
        while True:
            respuesta = input("¿Desea confirmar el pedido? (S/N): ").strip().upper()
            if respuesta == 'S':
                self.estado = 'confirmada'
                print("Pedido confirmado.")
                for producto, cantidad in productos:
                    Producto.inventario.actualizar_existencias(producto, cantidad)
                Venta(id_venta, id_cliente, productos, fecha_actual, total_venta)
                break
            elif respuesta == 'N':
                self.estado = 'cancelada'
                print("Pedido cancelado.")
                break
            else:
                print("Opción no válida. Por favor, responda con 'S' para sí o 'N' para no.")