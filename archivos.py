"""
Módulo para manejo de archivos CSV.
"""

import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
    inventario (list)
    ruta (str)
    incluir_header (bool)

    Retorna:
    None
    """
    if not inventario:
        print("El inventario está vacío. No se puede guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print(f"Error al guardar archivo: {e}")


def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV.

    Parámetros:
    ruta (str)

    Retorna:
    list
    """
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return []

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"{errores} filas inválidas omitidas.")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación.")
    except Exception as e:
        print(f"Error: {e}")

    return []
