# inventario.py 

# Solicitar al usuario el nombre del producto
nombre = input("Ingrese el nombre del producto: ")


# Solicitar el precio del producto y validar que sea un número decimal
while True:
   try:
       precio = float(input("Ingrese el precio del producto: "))
       break
   except ValueError:
       print("Valor inválido. Ingrese un número válido para el precio.")


# Solicitar la cantidad del producto y validar que sea un número entero
while True:
   try:
       cantidad = int(input("Ingrese la cantidad del producto: "))
       break
   except ValueError:
       print("Valor inválido. Ingrese un número entero para la cantidad.")


# Calcular el costo total multiplicando el precio por la cantidad
costo_total = precio * cantidad


# Mostrar en pantalla la información del producto y el costo total
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)