class Cliente:
    """Clase que representa la información de un cliente del restaurante."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        """Devuelve una representación en texto con los datos del cliente."""
        return (
            f"ID: {self.identificacion:<10} | Nombre: {self.nombre:<20} | "
            f"Correo: {self.correo}"
        )