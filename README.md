# restaurante_app
# Sistema de Gestión de Restaurante

**Nombre completo del estudiante:** [jonny javier garces almeida]

## Descripción del sistema
Este proyecto es un sistema básico de gestión para un restaurante, desarrollado en Python aplicando los principios de la Programación Orientada a Objetos (POO). Su objetivo es administrar la información de los productos disponibles en el menú y los clientes registrados, permitiendo agregar nuevos elementos y visualizar la información de forma organizada. Está diseñado para demostrar la correcta organización modular del código, la separación de responsabilidades y el uso de clases, objetos, constructores y métodos especiales.

## Estructura del proyecto
El proyecto sigue la estructura obligatoria solicitada, organizada en carpetas y archivos con responsabilidades definidas:

restaurante_app/├── modelos/│ ├── producto.py # Define la entidad Producto (platos, bebidas, etc.)│ └── cliente.py # Define la entidad Cliente (datos de los usuarios)├── servicios/│ └── restaurante.py # Clase de servicio: gestiona productos, clientes y operaciones└── main.py # Archivo principal: creación de objetos y ejecución


### Explicación de cada parte
- **`modelos/`**: Contiene las clases que representan las entidades o datos del sistema. Aquí solo se definen atributos y la forma de representar la información, sin lógica de negocio.
  - `Producto`: Almacena código, nombre, precio y categoría. Incluye el método `__str__()` para mostrar sus datos.
  - `Cliente`: Almacena ID, nombre, teléfono y correo. También usa `__str__()` para visualización.

- **`servicios/`**: Contiene la lógica y gestión del sistema.
  - `Restaurante`: Es la clase principal de gestión. Tiene listas para guardar productos y clientes, y métodos para agregar nuevos registros y mostrar toda la información almacenada. Se encarga de coordinar las operaciones.

- **`main.py`**: Es el punto de inicio del programa. Aquí se importan las clases necesarias, se crean los objetos, se llaman a los métodos de gestión y se muestran los resultados en consola. Es el archivo que conecta todos los módulos.

## Reflexión sobre la importancia de modularizar y separar responsabilidades
Modularizar un software significa dividir el código en archivos o módulos independientes, donde cada uno cumple una función específica. Separar responsabilidades consiste en que cada parte del programa se dedique solo a lo que le corresponde: los modelos guardan datos, los servicios gestionan operaciones y el archivo principal coordina la ejecución.

Esta práctica es fundamental porque:
1. **Facilita la comprensión**: El código es más ordenado y fácil de leer, ya que cada archivo tiene un propósito claro.
2. **Simplifica el mantenimiento**: Si hay un error o se requiere modificar algo, se sabe exactamente en qué archivo está, sin afectar el resto del sistema.
3. **Permite reutilización**: Las clases o módulos pueden usarse en otros proyectos o partes del programa sin tener que reescribir el código.
4. **Favorece el trabajo en equipo**: Varias personas pueden trabajar en diferentes módulos al mismo tiempo sin generar conflictos.
5. **Escalabilidad**: Es más fácil agregar nuevas funcionalidades o entidades sin desorganizar lo que ya está hecho.

En resumen, un software modular y con responsabilidades separadas es de mejor calidad, más robusto y mucho más fácil de evolucionar con el tiempo.
