# WP-Blog-Post-Image-Scraper
Este script de Python está diseñado para extraer automáticamente imágenes destacadas e internas de los posts de un blog de WordPress. Facilita la descarga de medios asociados a los artículos del blog, simplificando la tarea de respaldar o migrar contenido. ¡Ahorra tiempo y esfuerzo en la gestión de medios en tu sitio de WordPress!

# Extractor de Imágenes de Post en Blog de WordPress

Este script de Python descarga las imágenes destacadas y las imágenes internas de los posts de un blog de WordPress.

## Instrucciones de Uso

### Requisitos Previos

Asegúrate de tener instalado Python en tu sistema. Puedes descargar Python desde [el sitio web oficial de Python](https://www.python.org/).

### Instalación de Dependencias

Antes de ejecutar el script, instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install requests beautifulsoup4

## Configuración del Script
Abre el archivo main.py en un editor de texto.

En la sección de configuración (al principio del archivo), modifica las variables según tus necesidades:

# Configuración de la URL del sitio
wordpress_url = 'https://thefinngroup.com.au/finn-blog/'

# Ruta local para guardar las imágenes
image_folder = os.path.join(os.getcwd(), 'export', 'images')

## Ejecutar el Script

## 1. Clona este repositorio:
git clone https://github.com/TU_USUARIO/tu-repositorio.git

## 2. Navega al directorio del script:
cd tu-repositorio

## 3. Ejecuta el script:
python main.py

El script comenzará a descargar las imágenes del blog de WordPress.

## Configuración Adicional
Si necesitas personalizar la configuración del script, como la URL del blog de WordPress o la carpeta de destino de las imágenes, puedes hacerlo en el archivo main.py.

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes mejoras sugeridas, abre un problema o envía una solicitud de extracción.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.


Este README proporciona instrucciones detalladas sobre cómo configurar y ejecutar el script, así como información sobre la configuración adicional y cómo contribuir al proyecto. Recuerda ajustar los enlaces y detalles específicos según tu situación. ¡Espero que sea útil para tu proyecto!

## by @ingnrcs
