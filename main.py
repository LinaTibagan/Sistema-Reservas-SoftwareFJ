from cliente import Cliente
from excepciones import ClienteError

try:

    cliente1 = Cliente("Natalia", 123456, "3000000000")

    print(cliente1.mostrar_datos())

    cliente2 = Cliente("", 456, "3111111111")

except ClienteError as e:

    print("Error:", e)