"""
Módulo de servicios para gestionar el inventario.
Contiene funciones CRUD y estadísticas.
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Parámetros:
    inventario (list): Lista de productos.
    nombre (str): Nombre del producto.
    precio (float): Precio del producto.
    cantidad (int): Cantidad disponible.

    Retorna:
    None
    """
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.

    Parámetros:
    inventario (list)

    Retorna:
    None
    """
    if not inventario:
        print("Inventario vacío.")
        return

    for p in inventario:
        print(f"{p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Parámetros:
    inventario (list)
    nombre (str)

    Retorna:
    dict o None
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.

    Parámetros:
    inventario (list)
    nombre (str)
    nuevo_precio (float, opcional)
    nueva_cantidad (int, opcional)

    Retorna:
    bool (True si se actualizó, False si no existe)
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
    inventario (list)
    nombre (str)

    Retorna:
    bool
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Parámetros:
    inventario (list)

    Retorna:
    dict con métricas
    """
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }
