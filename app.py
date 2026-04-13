"""
Aplicación principal del sistema de inventario.
"""

from servicios import *
from archivos import *


def menu():
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


def main():
    inventario = []

    while True:
        menu()

        try:
            opcion = int(input("Seleccione opción: "))

            if opcion == 1:
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(inventario, nombre, precio, cantidad)

            elif opcion == 2:
                mostrar_inventario(inventario)

            elif opcion == 3:
                nombre = input("Nombre: ")
                p = buscar_producto(inventario, nombre)
                print(p if p else "No encontrado")

            elif opcion == 4:
                nombre = input("Nombre: ")
                precio = input("Nuevo precio (enter para omitir): ")
                cantidad = input("Nueva cantidad (enter para omitir): ")

                actualizar_producto(
                    inventario,
                    nombre,
                    float(precio) if precio else None,
                    int(cantidad) if cantidad else None
                )

            elif opcion == 5:
                nombre = input("Nombre: ")
                eliminar_producto(inventario, nombre)

            elif opcion == 6:
                stats = calcular_estadisticas(inventario)
                if stats:
                    print(stats)
                else:
                    print("Inventario vacío.")

            elif opcion == 7:
                ruta = input("Ruta archivo: ")
                guardar_csv(inventario, ruta)

            elif opcion == 8:
                ruta = input("Ruta archivo: ")
                nuevo = cargar_csv(ruta)

                if nuevo:
                    decision = input("¿Sobrescribir inventario? (S/N): ").upper()

                    if decision == "S":
                        inventario = nuevo
                    else:
                        # Fusión
                        for p in nuevo:
                            existente = buscar_producto(inventario, p["nombre"])
                            if existente:
                                existente["cantidad"] += p["cantidad"]
                                existente["precio"] = p["precio"]
                            else:
                                inventario.append(p)

            elif opcion == 9:
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Entrada inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
