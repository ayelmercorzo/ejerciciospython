class Producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_actual):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_actual = stock_actual

    def __str__(self):
        return f"{self.codigo} - {self.nombre} (Cantidad: {self.stock_actual})"
