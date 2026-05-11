from excepciones import ClienteInvalidoError

# Clase para manejar la información de los clientes.
# Aquí se hacen algunas validaciones para evitar datos incorrectos.

class Cliente:

    def __init__(self, nombre, documento, telefono):

        # Validación del nombre
        if nombre.strip() == "":
            raise ClienteInvalidoError("El nombre no puede estar vacío")

        # Validación del documento
        if len(str(documento)) < 5:
            raise ClienteInvalidoError("El documento no es válido")

        # Validación del teléfono
        if len(telefono) < 10:
            raise ClienteInvalidoError("El teléfono no es válido")

        # Encapsulación
        self.__nombre = nombre
        self.__documento = documento
        self.__telefono = telefono

    # Método para mostrar información
    def mostrar_datos(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Teléfono: {self.__telefono}"
        )

    # Getter del nombre
    def get_nombre(self):
        return self.__nombre