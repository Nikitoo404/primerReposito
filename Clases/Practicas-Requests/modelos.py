import requests as rq
from bs4 import BeautifulSoup as bs
import sqlite3
from modelobase import * 



bd=BaseDatos()
bd.generarTablas()

url="https://quinielanacional1.com.ar/"
pagina=rq.get(url)
sopa=bs(pagina.text,'html.parser')
menuFecha=sopa.find(id='menu')
fechaAproxi=menuFecha.find('h2')
fechaAproxi=fechaAproxi.text
fechaCortada=fechaAproxi.split(" ") #divide nombre del dia, la fecha y la flecha en una lista
fechaReal=fechaCortada[1][:8]  #busca el elemento 1 que es la fecha y muestra solo 8 char porque el resto es la flecha
print(fechaReal.split("/"))


columnas=sopa.find_all('div', class_='columna')

for columna in columnas:
    #print("-----------------------------")
    titulo=columna.find('p')

    tituloEncontrado=bd.consultar(f"""
               SELECT * FROM quinela WHERE nombre = '{titulo.text}'
                """,cantidad=1)



    if not tituloEncontrado:
        bd.actualizarBD(f"""
                INSERT INTO quinela (nombre) VALUES ('{titulo.text}') 
                """)
        tituloEncontrado=bd.consultar(f"""
               SELECT * FROM quinela WHERE nombre = '{titulo.text}'
                """,cantidad=1)


    print(tituloEncontrado[0])



    #print(titulo.text)
    veitenas=columna.find_all('div',class_='veintena')
    for veitena in veitenas:
        cantidadDiv=veitena.find_all('div')
        i=0
        for cantidad in cantidadDiv:
            if i%2 == 0:
            #print("")
            #print("posicion: " + cantidad.text) 
                pass
            else:
            #print("numero:" + cantidad. text)
                pass
                i=i+1