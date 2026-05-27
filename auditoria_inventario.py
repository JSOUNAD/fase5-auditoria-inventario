# ================================================
# FUNDAMENTOS DE PROGRAMACIÓN - Fase 5
# Problema 3: Auditoría de Inventario
# Autor: [Jeltsin Sarasty]
# ================================================

def calcular_pedido_inventario(matriz):
    """
    Calcula la cantidad a pedir de cada artículo según stock actual y mínimo.
    Retorna una lista de tuplas: (Nombre, Cantidad a pedir)
    """
    pedidos = []
    for articulo in matriz:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        if stock_actual < stock_minimo:
            cantidad_pedir = stock_minimo - stock_actual
            pedidos.append((nombre, cantidad_pedir))
        # Si no se necesita pedido, no se incluye en la lista
    
    return pedidos


# ==================== DATOS DE PRUEBA ====================
inventario = [
    ["A001", "Laptop Dell",          8,  15],
    ["A002", "Mouse Inalámbrico",   25,  30],
    ["A003", "Teclado Mecánico",    12,  20],
    ["A004", "Monitor 27 pulgadas",  5,  10],
    ["A005", "Memoria RAM 16GB",    18,  15],
    ["A006", "Disco SSD 512GB",      7,  12]
]

# ==================== EJECUCIÓN PRINCIPAL ====================
print("=== AUDITORÍA DE INVENTARIO - REABASTECIMIENTO ===\n")

pedidos = calcular_pedido_inventario(inventario)

if not pedidos:
    print("Todos los artículos tienen stock suficiente.")
else:
    print("Artículos que requieren pedido:\n")
    for nombre, cantidad in pedidos:
        print(f"Artículo: {nombre}")
        print(f"  Cantidad a pedir: {cantidad} unidades")
        print("-" * 45)

print(f"\nTotal de artículos a reabastecer: {len(pedidos)}")
