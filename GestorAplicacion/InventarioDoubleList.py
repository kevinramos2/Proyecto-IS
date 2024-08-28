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
        temp = self.inventario.first()
        while temp is not None:
            if temp.get_data().get_referencia() == referencia:
                return 1
            temp = temp.get_next()
        return -1

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
        temp = self.inventario.first()
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def mostrar_por_categoria(self, categoria):
        temp = self.inventario.first()
        while temp is not None:
            if temp.get_data().get_categoria() == categoria:
                print(temp.get_data())
            temp = temp.get_next()
