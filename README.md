# Sistema restaurante_app
**Estudiante:** Clay Medardo Grefa Tunay  
**Semana 8 — Programación Orientada a Objetos**


## 🧩 Responsabilidad de cada clase
- **Producto:** representa un producto general del restaurante.
- **Bebida:** hereda de Producto y agrega atributos específicos.
- **Cliente:** almacena la información de un cliente.
- **Restaurante:** administra registros y listados de productos y clientes.
- **main.py:** interacción por consola y menú principal.

## 🧠 Principios SOLID aplicados
### ✔ SRP — Responsabilidad Única
Cada clase cumple una función específica sin mezclar responsabilidades.

### ✔ OCP — Abierto/Cerrado
La clase Bebida amplía Producto sin modificar su implementación.

### ✔ LSP — Sustitución de Liskov
Bebida puede utilizarse como Producto dentro de la misma colección sin condicionales.