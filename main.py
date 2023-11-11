import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote

# Configuración de la URL del sitio
wordpress_url = 'https://webdestino.com/blog/'

# Ruta local para guardar las imágenes
image_folder = os.path.join(os.getcwd(), 'export', 'images')

# Crear directorio de imágenes si no existe
os.makedirs(image_folder, exist_ok=True)

# Obtener el contenido HTML de la página con el archive de posts
page_number = 1
while True:
    current_page_url = f'{wordpress_url}?page={page_number}'
    response = requests.get(current_page_url)

    if response.status_code != 200:
        break  # Salir del bucle si la página no devuelve un código 200

    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar enlaces a las páginas de cada post
    post_links = [a['href'] for a in soup.find_all('a', class_='link-to-post')]

    # Iterar sobre los enlaces de los posts
    for post_link in post_links:
        full_post_url = urljoin(wordpress_url, post_link)

        post_response = requests.get(full_post_url)
        post_html_content = post_response.content
        post_soup = BeautifulSoup(post_html_content, 'html.parser')

        # Obtener la imagen destacada
        featured_image = post_soup.find('img', class_='link-to-post')

        if featured_image:
            featured_image_url = featured_image['src']
            # Verificar si la URL contiene "/collect/" antes de continuar
            if "/collect/" in featured_image_url:
                print(f'Se omite la imagen destacada: {featured_image_url}')
            else:
                # Descargar y guardar la imagen destacada
                featured_image_filename = os.path.join(image_folder, os.path.basename(urlparse(featured_image_url).path))
                os.makedirs(os.path.dirname(featured_image_filename), exist_ok=True)  # Crear carpetas si no existen
                featured_image_data = requests.get(featured_image_url).content
                with open(featured_image_filename, 'wb') as img_file:
                    img_file.write(featured_image_data)
                    print(f'Imagen destacada guardada: {featured_image_filename}')

        # Obtener las imágenes internas
        internal_images = post_soup.find_all('img')

        for internal_image in internal_images:
            internal_image_url = internal_image['src']
            # Verificar si la URL contiene "/collect/" antes de continuar ""OPCIONAL SOLO PARA IGNORAR ALGUNAS IMAGENES VISIBLES DENTRO DE LOS POST Y QUE NO CORRESPONDAN A LA ENTRADA""
            if "/collect/" in internal_image_url:
                print(f'Se omite la imagen interna: {internal_image_url}')
            else:
                # Verificar si la URL es relativa y unirla con la URL del post actual
                if not urlparse(internal_image_url).scheme:
                    internal_image_url = urljoin(full_post_url, internal_image_url)

                # Construir la ruta de la imagen interna
                image_path = urlparse(internal_image_url).path
                image_path = unquote(image_path)  # Decodificar caracteres especiales en la URL
                image_path = image_path.lstrip('/').rstrip('/')  # Eliminar barras iniciales y finales

                # Crear las carpetas necesarias
                image_folder_path = os.path.join(image_folder, image_path)
                os.makedirs(os.path.dirname(image_folder_path), exist_ok=True)  # Crear carpetas si no existen

                # Descargar y guardar la imagen interna
                internal_image_filename = os.path.join(image_folder, image_path.replace('/', '\\'))
                internal_image_data = requests.get(internal_image_url).content
                with open(internal_image_filename, 'wb') as img_file:
                    img_file.write(internal_image_data)
                    print(f'Imagen interna guardada: {internal_image_filename}')

    page_number += 1

print('Proceso completado.')
