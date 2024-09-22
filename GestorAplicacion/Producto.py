from GestorAplicacion.InventarioDoubleList import InventarioDoubleList


class Producto:
    inventario = InventarioDoubleList()
    contador_personalizados = 0
    def __init__(self, nombre=None, referencia=None, stock=0, categoria=None, precio=0, color=None, aroma=None, comentario = None):
        self.nombre = nombre
        self.referencia = referencia
        self.stock = stock
        self.categoria = categoria
        self.precio = precio
        self.comentario = comentario
        
        # Determinar si es un producto con color o aroma
        if categoria == "Esencia":
            self.aroma = aroma
            self.color = None  # No tiene color
        else: 
            self.color = color
            self.aroma = None  # No tiene aroma

        Producto.inventario.agregar(self)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_referencia(self):
        return self.referencia

    def set_referencia(self, referencia):
        self.referencia = referencia

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_precio(self):
        return self.precio
    
    def get_comentario(self):
        return self.comentario
    
    def set_comentario(self, comentario):
        self.comentario = comentario

    def set_precio(self, precio):
        self.precio = precio

    def get_aroma(self):
        return self.aroma

    def set_aroma(self, aroma):
        self.aroma = aroma

    def __str__(self):
        if self.categoria == "Esencia":
            return f"{self.nombre} - Aroma: {self.aroma} - Referencia: {self.referencia} - Precio: ${self.precio} - Cantidad: {self.stock} - Categoria: {self.categoria}"
        else:
            return f"{self.nombre} - Color: {self.color} - Referencia: {self.referencia} - Precio: ${self.precio} - Cantidad: {self.stock} - Categoria: {self.categoria}"
