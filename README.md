# 🛒 Urban Grocers API - Pruebas Automatizadas


## Descripción

Este proyecto tiene como objetivo automatizar las pruebas de la API de Urban Grocers. La aplicación Urban Grocers permite a los usuarios realizar compras de productos de almacenes registrados, crear kits con varios productos, verificar la existencia de productos en almacenes específicos y buscar kits predeterminados de productos.

## Tabla de Contenido

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución de las Pruebas](#ejecución-de-las-pruebas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contacto](#contacto)

## Características

- **Pruebas Automatizadas**: Validación de la creación de kits de productos mediante pruebas automatizadas que verifican el campo `name` en las solicitudes de creación de kits.
- **Cobertura de Casos**: Incluye pruebas positivas y negativas para asegurar el correcto funcionamiento de la API en diversos escenarios.
- **Tecnologías Utilizadas**: Implementación en Python utilizando las librerías `pytest` y `requests` para la ejecución y gestión de las pruebas.

## Requisitos

- **Python**: Asegúrate de tener Python instalado en tu sistema.
- **Librerías Necesarias**: Instala las librerías `pytest` y `requests` utilizando pip:
  ```bash
  pip install pytest requests
  ```

## Instalación

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/GarayOcs/qa-project-Urban-Grocers-app-es.git
   ```
2. **Instalar Dependencias**: Navega al directorio del proyecto e instala las dependencias requeridas:
   ```bash
   cd qa-project-Urban-Grocers-app-es
   pip install -r requirements.txt
   ```

## Ejecución de las Pruebas

1. **Iniciar el Servidor**: Asegúrate de que el servidor de la API de Urban Grocers esté en funcionamiento.
2. **Ejecutar Pruebas**: Utiliza `pytest` para ejecutar las pruebas automatizadas:
   ```bash
   pytest create_kit_name_kit_test.py
   ```

## Estructura del Proyecto

- `configuration.py`: Almacena las rutas y configuraciones necesarias para las pruebas.
- `data.py`: Contiene los datos utilizados en las solicitudes de prueba.
- `sender_stand_request.py`: Gestiona las solicitudes HTTP hacia la API.
- `create_kit_name_kit_test.py`: Incluye los casos de prueba automatizados para la creación de kits.
- `.gitignore`: Especifica los archivos y directorios que Git debe ignorar.
- `README.md`: Proporciona información detallada sobre el proyecto.

## Contacto

- **GitHub**: [GarayOcs](https://github.com/GarayOcs)
- **LinkedIn**: [Ingrid Santana Garay](https://www.linkedin.com/in/ingrid-santana-garay-459a2a31b/)
