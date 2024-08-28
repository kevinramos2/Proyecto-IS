from GestorAplicacion.DoubleNode import DoubleNode


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def add_first(self, data):
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        self.size += 1

    def add_last(self, data):
        node = DoubleNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = temp.get_next()
        if self.head is not None:
            self.head.set_prev(None)
        self.size -= 1
        return temp.get_data()

    def remove_last(self):
        if self.is_empty():
            return None
        temp = self.tail
        self.tail = temp.get_prev()
        if self.tail is not None:
            self.tail.set_next(None)
        self.size -= 1
        return temp.get_data()

    def remove(self, node):
        if node is None:
            return None
        if node == self.head:
            return self.remove_first()
        elif node == self.tail:
            return self.remove_last()
        else:
            data = node.get_data()
            prev_node = node.get_prev()
            next_node = node.get_next()
            if prev_node:
                prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)
            self.size -= 1
            return data

    def add_before(self, node, data):
        if node == self.head:
            self.add_first(data)
        else:
            new_node = DoubleNode(data)
            prev_node = node.get_prev()
            if prev_node:
                prev_node.set_next(new_node)
            new_node.set_prev(prev_node)
            new_node.set_next(node)
            node.set_prev(new_node)
            self.size += 1

    def add_after(self, node, data):
        if node == self.tail:
            self.add_last(data)
        else:
            new_node = DoubleNode(data)
            next_node = node.get_next()
            node.set_next(new_node)
            new_node.set_prev(node)
            new_node.set_next(next_node)
            if next_node:
                next_node.set_prev(new_node)
            self.size += 1

    @staticmethod
    def imprimir_datos(lista):
        temp = lista.head
        while temp:
            # Aquí puedes personalizar la impresión de datos según sea necesario
            print(temp.get_data())
            temp = temp.get_next()
