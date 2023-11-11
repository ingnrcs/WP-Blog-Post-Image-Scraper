import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote

# Configuración de la URL del sitio
wordpress_url = 'https://tuweb.com/blog/'

# Ruta local para guardar las imágenes
image_folder = os.path.join(os.getcwd(), 'export', 'imagenes')

# Crear directorio de imágenes si no existe
os.makedirs(image_folder, exist_ok=True)

# Obtener el contenido HTML de la página con el archive de posts
page_number = 1
while True:
    current_page_url = f'{wordpress_url}page/{page_number}/'
    response = requests.get(current_page_url)

    if response.status_code != 200:
        break  # Salir del bucle si la página no devuelve un código 200

    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    print(f'Procesando la página {page_number}...')

    # Encontrar enlaces a las páginas de cada post
    post_links = [a['href'] for a in soup.find_all('a', class_='finn-btn')]

    # Contador de posts procesados en la página actual
    posts_processed = 0

    # Iterar sobre los enlaces de los posts
    for post_link in post_links:
        full_post_url = urljoin(wordpress_url, post_link)

        post_response = requests.get(full_post_url)
        post_html_content = post_response.content
        post_soup = BeautifulSoup(post_html_content, 'html.parser')

        # Obtener el título del post
        post_title_element = post_soup.find('h1', class_='wp-block-post-title')
        post_title = post_title_element.text.strip() if post_title_element else 'Título no encontrado'

        print(f'Título del post: {post_title}')

        # Resto del código para procesar imágenes...

        # Obtener la imagen destacada
        featured_image = post_soup.find('img', class_='link-to-post')

        if featured_image:
            featured_image_url = featured_image['src']
            # Resto del código para procesar la imagen destacada...

        # Obtener las imágenes internas
        internal_images = post_soup.find_all('img')

        for internal_image in internal_images:
            internal_image_url = internal_image['src']
            # Resto del código para procesar las imágenes internas...

        posts_processed += 1

    print(f'Página {page_number} procesada. Total de posts procesados: {posts_processed}')

    page_number += 1

print('Proceso completado.')
