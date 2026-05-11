from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError

# Clase abstracta de servicios

class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio 1
class ReservaSala(Servicio):

    def __init__(self, horas):

        if horas <= 0:
            raise ServicioNoDisponibleError(
                "Las horas deben ser mayores a cero"
            )

        super().__init__("Reserva de Sala", 50000)

        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


# Servicio 2
class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        if dias <= 0:
            raise ServicioNoDisponibleError(
                "Los días deben ser mayores a cero"
            )

        super().__init__("Alquiler de Equipos", 30000)

        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Alquiler de equipos por {self.dias} días"


# Servicio 3
class AsesoriaEspecializada(Servicio):

    def __init__(self, sesiones):

        if sesiones <= 0:
            raise ServicioNoDisponibleError(
                "Las sesiones deben ser mayores a cero"
            )

        super().__init__("Asesoría Especializada", 80000)

        self.sesiones = sesiones

    def calcular_costo(self):
        return self.precio_base * self.sesiones

    def descripcion(self):
        return (
            f"Asesoría especializada de "
            f"{self.sesiones} sesiones"
        )