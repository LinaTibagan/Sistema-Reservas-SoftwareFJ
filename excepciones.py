# excepcion.py

# Excepción cuando hay errores con clientes
class ClienteError(Exception):
    pass


# Excepción para reservas
class ReservaError(Exception):
    pass


# Función para guardar errores
def guardar_error(error):

    archivo = open("registros.txt", "a")

    archivo.write(str(error) + "\n")

    archivo.close()
