import requests

#URL del sitio que deseo analizar
url='https://www.youtube.com/'

respuesta=requests.get(url)
#si en vez de poner la varible, pongo su contenido, es lo mismo.

print(respuesta.content)