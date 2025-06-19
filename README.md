# Proyecto de Inventario / Inventory Project

Este es un proyecto básico de Django para gestionar un inventario de productos. Está estructurado con una aplicación principal de Django y una app llamada `productos`, dedicada a la gestión de productos.

This is a basic Django project for managing a product inventory. The project is structured with a main Django application and an app named `productos` dedicated to handling product-related features.

---

## Requisitos / Requirements

- Python 3.x  
- Django 5.x  
- Pipenv para gestión de dependencias
  
---

## Instalación / Setup Instructions

### 1. Clonar el repositorio / Clone the repository

```bash
git clone https://github.com/jahurtadod/example_django.git
cd example_django
```

### 2. Crea y activa el entorno virtual, luego instala dependencias:

```bash
pipenv install      # Instala paquetes desde Pipfile
pipenv shell        # Activa el entorno virtual
```

## Migraciones de base de datos

```bash
python manage.py makemigrations     # Crea nuevas migraciones  
python manage.py migrate            # Aplica migraciones a la base de datos
```

## Ejecución del servidor

```bash
python manage.py runserver
```
