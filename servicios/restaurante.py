from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio encargada de administrar las colecciones y reglas de negocio."""

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        # Lista única para almacenar tanto Producto como Bebida (Polimorfismo)
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    # --- Métodos de Búsqueda y Validación ---
    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código único."""
        for p in self.productos:
            if p.codigo.lower() == codigo.lower():
                return p
        return None

    def buscar_cliente_por_id(self, identificacion: str) -> Optional[Cliente]:
        """Busca un cliente por su documento/ID único."""
        for c in self.clientes:
            if c.identificacion.lower() == identificacion.lower():
                return c
        return None

    # --- Métodos de Registro ---
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un objeto Producto o Bebida en la colección si el código no se repite."""
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self.productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        """Registra un cliente si su identificación no se encuentra duplicada."""
        if self.buscar_cliente_por_id(cliente.identificacion) is not None:
            return False
        self.clientes.append(cliente)
        return True

    # --- Métodos de Consulta ---
    def obtener_productos(self) -> List[Producto]:
        """Devuelve la lista general de productos registrados."""
        return self.productos

    def obtener_clientes(self) -> List[Cliente]:
        """Devuelve la lista general de clientes registrados."""
        return self.clientes