from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE        ")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("========================================")

def solicitar_datos_producto_base() -> tuple[str, str, str, float]:
    """Solicita e ingresa los datos comunes para Producto y Bebida."""
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    
    while True:
        try:
            precio = float(input("Ingrese el precio ($): "))
            if precio <= 0:
                print("[!] El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("[!] Entrada inválida. Ingrese un valor numérico.")

    return codigo, nombre, categoria, precio

def registrar_producto_ui(servicio: Restaurante) -> None:
    print("\n--- REGISTRO DE PRODUCTO ---")
    codigo, nombre, categoria, precio = solicitar_datos_producto_base()
    
    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    exito = servicio.registrar_producto(nuevo_producto)
    
    if exito:
        print("[✓] Producto registrado con éxito.")
    else:
        print(f"[!] Error: Ya existe un producto registrado con el código '{codigo}'.")

def registrar_bebida_ui(servicio: Restaurante) -> None:
    print("\n--- REGISTRO DE BEBIDA ---")
    codigo, nombre, categoria, precio = solicitar_datos_producto_base()
    
    while True:
        try:
            tamano_ml = int(input("Ingrese el tamaño en mililitros (ml): "))
            if tamano_ml <= 0:
                print("[!] El tamaño debe ser un valor entero positivo.")
                continue
            break
        except ValueError:
            print("[!] Entrada inválida. Ingrese un número entero.")

    tipo_envase = input("Ingrese el tipo de envase (Ej: Vidrio, Plástico, Lata): ").strip()
    
    nueva_bebida = Bebida(codigo, nombre, categoria, precio, tamano_ml, tipo_envase)
    exito = servicio.registrar_producto(nueva_bebida)
    
    if exito:
        print("[✓] Bebida registrada con éxito.")
    else:
        print(f"[!] Error: Ya existe un producto registrado con el código '{codigo}'.")

def registrar_cliente_ui(servicio: Restaurante) -> None:
    print("\n--- REGISTRO DE CLIENTE ---")
    identificacion = input("Ingrese el documento de identidad / ID: ").strip()
    nombre = input("Ingrese el nombre completo del cliente: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()

    nuevo_cliente = Cliente(identificacion, nombre, correo)
    exito = servicio.registrar_cliente(nuevo_cliente)

    if exito:
        print("[✓] Cliente registrado con éxito.")
    else:
        print(f"[!] Error: Ya existe un cliente con la identificación '{identificacion}'.")

def listar_productos_ui(servicio: Restaurante) -> None:
    print("\n--- LISTADO DE PRODUCTOS Y BEBIDAS ---")
    productos = servicio.obtener_productos()

    if not productos:
        print("No hay productos o bebidas registrados en el sistema.")
        return

    # Polimorfismo en acción:
    # Se ejecuta mostrar_informacion() dinámicamente sin 'if/isinstance'
    for pos, prod in enumerate(productos, 1):
        print(f"{pos}. {prod.mostrar_informacion()}")

def listar_clientes_ui(servicio: Restaurante) -> None:
    print("\n--- LISTADO DE CLIENTES ---")
    clientes = servicio.obtener_clientes()

    if not clientes:
        print("No hay clientes registrados en el sistema.")
        return

    for pos, cli in enumerate(clientes, 1):
        print(f"{pos}. {cli.mostrar_informacion()}")

def main() -> None:
    # Instanciamos el servicio principal
    mi_restaurante = Restaurante("Sabor & Polimorfismo")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_producto_ui(mi_restaurante)
        elif opcion == "2":
            registrar_bebida_ui(mi_restaurante)
        elif opcion == "3":
            registrar_cliente_ui(mi_restaurante)
        elif opcion == "4":
            listar_productos_ui(mi_restaurante)
        elif opcion == "5":
            listar_clientes_ui(mi_restaurante)
        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema del restaurante! Hasta luego.")
            break
        else:
            print("\n[!] Opción no válida. Por favor, seleccione un número entre 1 y 6.")

if __name__ == "__main__":
    main()