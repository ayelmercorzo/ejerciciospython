from inventario import Inventario

def mostrar_menu():
    print("\n \t**Menú Principal**")
    print(" 1. Ingresa un producto")
    print(" 2. Revise los productos registrados")
    print(" 3. Actualizar la cantidad de un producto")
    print(" 4. Productos Críticos")
    print(" 5. Ganancia potencial general")
    print(" 6. Salir")

def obtener_datos_producto():
    codigoProducto = input("Escribe el código del producto: ")
    nombreProducto = input("Escribe el nombre del producto: ")
    precioDeProducto = float(input("Escribe el precio de compra del producto: "))
    precioDeVenta = float(input("Escribe el precio a vender: "))
    cantidadProductos = int(input("Escribe la cantidad actual de productos: "))
    return codigoProducto, nombreProducto, precioDeProducto, precioDeVenta, cantidadProductos

def main():
    inventario = Inventario()

    while True:
        
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            
            codigoProducto, nombreProducto, precioDeProducto, precioDeVenta, cantidadProductos = obtener_datos_producto()
            inventario.registrar_producto(codigoProducto, nombreProducto, precioDeProducto, precioDeVenta, cantidadProductos)

        elif opcion == "2":
            
            inventario.mostrar_productos()

        elif opcion == "3":
            
            codigoProducto = input("Escribe el código del producto a actualizar: ")
            cantidad = int(input("Escribe (+) o (-) mas la cantidad vendida o comprada para actualizar su cantidad: "))
            inventario.actualizar_stock(codigoProducto, cantidad)

        elif opcion == "4":
            
            inventario.mostrar_productos_criticos()

        elif opcion == "5":
            
            inventario.calcular_ganancia_potencial()

        elif opcion == "6":
            
            print("Saliendo del programa...")
            break

        else:
            print("Esa opcion no existe, seleccione una opción válida (1-6).")

if __name__ == "__main__":
    main()

