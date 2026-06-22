
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre  
        self.lista_productos = []  
        self.lista_clientes = []   

    
    def agregar_producto(self, producto: Producto):
        if isinstance(producto, Producto):
            self.lista_productos.append(producto)
            return f"Producto '{producto.nombre}' agregado correctamente."
        return "Error: El objeto no es un tipo Producto."

    
    def registrar_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.lista_clientes.append(cliente)
            return f"Cliente '{cliente.nombre}' registrado correctamente."
        return "Error: El objeto no es un tipo Cliente."

    
    def mostrar_productos(self):
        print(f"\n--- Menú de {self.nombre} ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        for producto in self.lista_productos:
            print(producto)


    def mostrar_clientes(self):
        print(f"\n--- Clientes registrados en {self.nombre} ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.lista_clientes:
            print(cliente)
