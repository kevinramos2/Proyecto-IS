class Empleado:
    _todosLosUsuarios = []

    # CONSTRUCTOR
    def __init__(self,nombre,id,contraseña):
        self._nombre = nombre
        self._id = id
        self._contraseña = contraseña

        Empleado._todosLosUsuarios.append(self)

    # TO STRING
    def __str__(self) -> str:
        return f"{self._nombre},{self._id},{self._contraseña}"

    # GETTERS Y SETTERS
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre

    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id

    def getContraseña(self):
        return self._contraseña
    def setContraseña(self, contraseña):
        self._contraseña = contraseña

    @classmethod
    def getTodolosUsuarios(cls):
        return cls._todosLosUsuarios
    @classmethod
    def setTodoLosUsuarios(cls,lista_objetos):
        Empleado._todosLosUsuarios = lista_objetos