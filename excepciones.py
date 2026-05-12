from datetime import datetime
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


     # Obtiene la fecha y hora actual
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Abre el archivo logs.txt para guardar errores
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        # Guarda la fecha, hora y mensaje del error
        archivo.write(f"[{fecha_hora}] {error}\n")
