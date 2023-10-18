import requests

#URL del sitio que deseo analizar
url='https://www.youtube.com/'

respuesta=requests.get(url)
#si en vez de poner la varible, pongo su contenido, es lo mismo.
if respuesta.status_code==200:
    print(respuesta.content)
else:
    print("Error. Revise su conexión a Internet, o si la dirección que proporcionó es la correcta.")