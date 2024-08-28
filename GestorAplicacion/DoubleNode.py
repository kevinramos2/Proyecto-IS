class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev
