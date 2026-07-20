from modelos.producto import Producto

class Bebida(Producto):
    """Clase que representa una bebida, especialización de Producto."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano_ml: int,
        tipo_envase: str
    ) -> None:
        # Reutilizamos el constructor de la clase base
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano_ml: int = tamano_ml
        self.tipo_envase: str = tipo_envase

    def mostrar_informacion(self) -> str:
        """Sobrescribe el método base para incluir datos específicos de la bebida."""
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self.tamano_ml}ml | Envase: {self.tipo_envase}"