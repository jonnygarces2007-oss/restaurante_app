
class Producto:
    
    def __init__(self, codigo, nombre, precio, categoria):
        self.codigo = codigo  # Identificador único
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # Ej: Entrada, Plato fuerte, Bebida, Postre

    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria}"
