import requests
from bs4 import BeautifulSoup

#URL del sitio que deseo analizar
url='https://www.bna.com.ar/'

respuesta=requests.get(url)
#si en vez de poner la varible, pongo su contenido, es lo mismo.

contenidoHTML=respuesta.content

soup=BeautifulSoup(contenidoHTML,'html.parser')

cuerpo=soup.body

#print("Contenido HTML: ",soup)

#print("Titulo: ",cuerpo)

titulo=soup.title.text

#print("Titulo: ",titulo)

divisorRH=cuerpo.find(id='rightHome')
#traigo los divisores

lista=['billetes','divisas']

for moneda in lista:
    cotizacion=cuerpo.find(id=moneda)
    #traigo cotizacion y, en este caso, moneda será billetes y, luego, divisas

    print(moneda)

    fecha=cotizacion.find(class_='fechaCot')
    print("Fecha: ",fecha.text)

    monedas=cotizacion.tbody
    #print(monedas.text)
    #acá, me trabjo la fecha de cotizacion y la moneda
    #También, si en vez de cotizacion.find(class_='tit') sería monedas=cotizacion.tbody, me traería todos
    #los datos sobre las cotizaciones

    #Si quiero cada valor cotizado en orden, debo hacerlo de la siguiente manera:

    filas=cotizacion.tbody.find_all('tr')
    #el find_all lo que hace es traer todas las filas de ese tbody

    for fila in filas:
        celdas= fila.find_all('td')
        if len(celdas)>=3:
            moneda=celdas[0].text.strip()
            compra=celdas[1].text.strip()
            venta=celdas[2].text.strip()
            print("Moneda: ",moneda)
            print("Compra: ",compra)
            print("Venta: ",venta)
            print("------------------------")
#Todo esto trae todos los billetes y todas las divisas