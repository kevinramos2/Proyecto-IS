from GestorAplicacion.DoubleList import DoubleList


class InventarioDoubleList:
    def __init__(self):
        self.inventario = DoubleList()

    def agregar(self, producto):
        if self.inventario.is_empty():
            self.inventario.add_first(producto)
        else:
            self.inventario.add_last(producto)

    def buscar_producto(self, referencia):
        encontrado = None
        temp = self.inventario.first()
        while temp is not None:
            if temp.get_data().get_referencia() == referencia:
                encontrado = temp.get_data()
                break  # Detener la búsqueda una vez encontrado
            temp = temp.get_next()
        return encontrado

    def eliminar_producto(self, referencia):
        temp = self.inventario.first()
        while temp is not None and temp.get_data().get_referencia() != referencia:
            temp = temp.get_next()
        if temp is not None:
            self.inventario.remove(temp)

    def imprimir_datos(self, referencia):
        temp = self.inventario.first()
        while temp is not None and temp.get_data().get_referencia() != referencia:
            temp = temp.get_next()
        if temp is not None:
            print(temp.get_data())

    def mostrar_completo(self):
        productos = []  # Crear una lista para almacenar los productos
        temp = self.inventario.first()
        while temp is not None:
            productos.append(temp.get_data().__str__())  # Agregar cada producto como cadena a la lista
            temp = temp.get_next()
        return productos  # Retornar la lista de productos

    def mostrar_por_categoria(self, categoria):
        productos_filtrados = []
        temp = self.inventario.first()
        while temp is not None:
            if temp.get_data().get_categoria() == categoria:
                productos_filtrados.append(temp.get_data().__str__())
            temp = temp.get_next()
        return productos_filtrados #se lleva el inventario filtrado
    
    def actualizar_existencias(self, producto, cantidad_comprada):
        referencia = producto.referencia  # Guardar referencia antes de buscar
        producto_en_inventario = self.buscar_producto(referencia)
        if producto_en_inventario is not None:
            producto_en_inventario.set_stock(producto_en_inventario.get_stock() - cantidad_comprada)
        else:
            print(f"Producto con referencia {referencia} no encontrado.")
