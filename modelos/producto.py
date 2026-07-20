class Producto:
    """Clase base que representa un producto general dentro del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def mostrar_informacion(self) -> str:
        """Devuelve una representación en texto con los datos del producto."""
        return (
            f"Código: {self.codigo:<6} | Nombre: {self.nombre:<18} | "
            f"Categoría: {self.categoria:<12} | Precio: ${self.precio:.2f}"
        )