# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, codigo, nombre, valor_compra, valor_venta, stock_actual):
        producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_actual)
        self.productos.append(producto)
        print("Producto registrado exitosamente.")
        
    def mostrar_productos(self):
        if self.productos:
            print("\nListado de Productos:")
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos registrados.")

    def actualizar_stock(self, codigo, cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.stock_actual += cantidad
                print(f"Stock actualizado para {producto.nombre}. Nuevo stock: {producto.stock_actual}")
                break
        else:
            print("Producto no encontrado.")

    def mostrar_productos_criticos(self):
        productos_criticos = [producto for producto in self.productos if producto.stock_actual < 10]
        if productos_criticos:
            print("\nProductos Críticos:")
            for producto in productos_criticos:
                print(producto)
        else:
            print("No hay productos críticos.")

    def calcular_ganancia_potencial(self):
        ganancia_potencial = sum((producto.valor_venta - producto.valor_compra) * producto.stock_actual for producto in self.productos)
        print(f"Ganancia potencial total: ${ganancia_potencial:.2f}")
