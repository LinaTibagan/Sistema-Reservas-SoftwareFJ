from excepciones import ReservaError

# Clase para manejar reservas

class Reserva:

    def __init__(self, cliente, servicio):

        if cliente is None:
            raise ReservaError("La reserva necesita un cliente")

        if servicio is None:
            raise ReservaError("La reserva necesita un servicio")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"

    # Mostrar información
    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.descripcion()} | "
            f"Estado: {self.estado}"
        )
