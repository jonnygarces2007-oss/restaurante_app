from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

mi_restaurante = Restaurante(nombre="Sabor Casero")

producto1 = Producto(codigo="P001", nombre="Ensalada César", precio=8.50, categoria="Entrada")
producto2 = Producto(codigo="P002", nombre="Lomo a la parrilla", precio=15.75, categoria="Plato fuerte")
producto3 = Producto(codigo="P003", nombre="Jugo de maracuyá", precio=3.25, categoria="Bebida")

cliente1 = Cliente(id_cliente="C001", nombre="María López", telefono="0987654321", correo="maria@ejemplo.com")
cliente2 = Cliente(id_cliente="C002", nombre="Carlos Ruiz", telefono="0991234567", correo="carlos@ejemplo.com")

print(mi_restaurante.agregar_producto(producto1))
print(mi_restaurante.agregar_producto(producto2))
print(mi_restaurante.agregar_producto(producto3))

print(mi_restaurante.registrar_cliente(cliente1))
print(mi_restaurante.registrar_cliente(cliente2))

mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()
