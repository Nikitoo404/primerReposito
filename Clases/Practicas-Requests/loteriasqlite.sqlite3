import requests as rq
from bs4 import BeautifulSoup as bs
import sqlite3

con=sqlite3.connect('BaseQuinela.sqlite')
cursor=con.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS quinela
                (id INTEGER PRIMARY KEY,
                nombre TEXT)
                """)
con.commit()


url="https://quinielanacional1.com.ar/"
pagina=rq.get(url)
sopa=bs(pagina.text,'html.parser')
columnas=sopa.find_all('div', class_='columna')

for columna in columnas:
    print("-----------------------------")
    titulo=columna.find('p')
    print(titulo.text)
    veitenas=columna.find_all('div',class_='veintena')
    for veitena in veitenas:
        cantidadDiv=veitena.find_all('div')
        i=0
        for cantidad in cantidadDiv:
            if i%2 == 0:
                print("")
                print("posicion: " + cantidad.text) 
            else:
                print("numero:" + cantidad. text)
        
            i=i+1