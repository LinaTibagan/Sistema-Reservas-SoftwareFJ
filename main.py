from cliente import Cliente

try:
    cliente1 = Cliente("Natalia", 123, "3000000000")
    print(cliente1.mostrar_datos())

    cliente2 = Cliente("", 456, "3111111111")

except ValueError as e:
    print("Error:", e)