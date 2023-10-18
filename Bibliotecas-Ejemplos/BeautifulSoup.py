import requests
from bs4 import BeautifulSoup

#URL del sitio que deseo analizar
url='https://es.wikipedia.org/wiki/Wikipedia:Portada'

respuesta=requests.get(url)
#si en vez de poner la varible, pongo su contenido, es lo mismo.

contenidoHTML=respuesta.content

soup=BeautifulSoup(contenidoHTML,'html.parser')

titulo=soup.title.text

print("Título: ",titulo)
#imprime el título de la página web