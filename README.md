# Gestor de Inventario

## Descripción

Gestor de Inventario es una aplicación de línea de comandos para gestionar un inventario de productos. Esta aplicación permite agregar, eliminar y actualizar productos, sus precios y sus existencias. Está construida usando Python y está estructurada en varios módulos para mejorar el mantenimiento y la legibilidad del código.

## Funcionalidades

- **Agregar Productos**: Añadir nuevos productos al inventario.
- **Eliminar Productos**: Eliminar productos existentes del inventario.
- **Actualizar Productos**: Actualizar los detalles de los productos existentes.
- **Ver Productos**: Mostrar una lista de todos los productos con sus precios y niveles de stock.

## Estructura del Proyecto


### Archivos y Directorios

- **main.py**: El punto de entrada de la aplicación.
- **inventory/**: Contiene módulos para gestionar productos, precios y existencias.
  - **manager.py**: La clase principal que maneja las operaciones del inventario.
  - **products.py**: Módulo para gestionar los nombres de los productos.
  - **prices.py**: Módulo para gestionar los precios de los productos.
  - **stock.py**: Módulo para gestionar el stock de los productos.
- **utils/**: Contiene funciones utilitarias.
  - **display.py**: Módulo para mostrar el menú y otros elementos de la interfaz de usuario.

## Uso

1. **Clonar el repositorio**:

```bash
git clone https://github.com/tuusuario/gestor_inventario.git
cd gestor_inventario
```


2. **Ejecutar la aplicación**:

```bash
python main.py
```






