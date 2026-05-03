# Clase para manejar la información de los clientes.
# Aquí se hacen algunas validaciones para evitar datos incorrectos.
class Cliente:

    def __init__(self, nombre, documento, telefono):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono

    def mostrar_datos(self):
        return f"Cliente: {self.__nombre}"
