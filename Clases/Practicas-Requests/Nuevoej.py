#Ejercicio del 28/09

import requests
from bs4 import BeautifulSoup
import sqlite3

url='https://quinielanacional1.com.ar/'

respuesta=requests.get(url)

contenidoHTML=respuesta.content

soup=BeautifulSoup(contenidoHTML,'html.parser')

titulo=soup.title.text

cuerpo=soup.body

divisorRH=cuerpo.find(id='principal')

#print("Título:",titulo)
print(divisorRH)