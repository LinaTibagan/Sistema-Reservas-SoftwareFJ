# Excepción cuando hay errores con clientes
class ClienteInvalidoError(Exception):
    pass


# Excepción cuando hay problemas con servicios
class ServicioNoDisponibleError(Exception):
    pass


# Excepción para reservas
class ReservaError(Exception):
    pass


# Función para guardar errores
def guardar_error(error):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(str(error) + "\n")
