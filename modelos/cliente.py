
class Cliente:
    
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente  
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Teléfono: {self.telefono} | Correo: {self.correo}"
