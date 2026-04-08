# -------------------------------
# Programa de gestión de inventario
# -------------------------------

# Lista para almacenar los productos
inventario = []

# Función para mostrar el menú al usuario
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

# Función para agregar productos al inventario
def agregar_producto():
    while True:
        # Pedimos el nombre del producto
        nombre = input("Ingresa el nombre del producto (o 'salir' para volver al menú): ")
        if nombre.lower() == "salir":
            break  # Salir del bucle si el usuario escribe 'salir'
        try:
            # Validamos que precio y cantidad sean números
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad: "))
        except ValueError:
            print("Precio o cantidad inválidos. Intenta nuevamente.")
            continue  # Volver a pedir datos si hay error
        
        # Creamos un diccionario con los datos del producto
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)  # Agregamos el producto a la lista
        print(f"Producto '{nombre}' agregado al inventario.")

# Función para mostrar todos los productos del inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")  # Mensaje si no hay productos
    else:
        print("\nInventario:")
        # Recorremos el inventario con un bucle for
        for producto in inventario:
            # Mostramos cada producto en un formato claro
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# Función para calcular estadísticas del inventario
def calcular_estadisticas():
    if not inventario:
        print("No hay productos para calcular estadísticas.")  # Mensaje si no hay productos
        return

    total_cantidad = 0
    valor_total = 0

    # Recorremos cada producto y sumamos cantidad y valor total
    for producto in inventario:
        total_cantidad += producto['cantidad']
        valor_total += producto['precio'] * producto['cantidad']

    # Mostramos los resultados de forma clara
    print("\n--- Estadísticas del Inventario ---")
    print(f"Cantidad total de productos registrados: {total_cantidad}")
    print(f"Valor total del inventario: {valor_total:.2f}")

# -------------------------------
# Bucle principal del programa
# -------------------------------
while True:
    mostrar_menu()  # Mostramos las opciones
    opcion = input("Elige una opción (1-4): ")

    # Validamos la opción ingresada por el usuario
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Salimos del bucle y terminamos el programa
    else:
        print("Opción inválida. Por favor ingresa un número del 1 al 4.")  # Mensaje si la opción es incorrecta 
       -------------------------------
# Objetivo de la semana:
# Practicar estructuras de control (if/elif/else), bucles (while, for), manejo de listas y diccionarios,
# y organización del código en funciones para crear un programa interactivo de inventario.
# -------------------------------


# -------------------------------
# Objetivo de la semana:
# Practicar estructuras de control (if/elif/else), bucles (while, for), manejo de listas y diccionarios,
# y organización del código en funciones para crear un programa interactivo de inventario.
# -------------------------------
