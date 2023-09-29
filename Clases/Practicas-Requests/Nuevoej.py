#Ejercicio del 28/09

import tkinter as tk
import requests as rq
from bs4 import BeautifulSoup as bs

url="https://quinielanacional1.com.ar/"
pagina=rq.get(url)
sopa=bs(pagina.text,'html.parser')
columna=sopa.find('div', class_='columna')
titulo=columna.find('p')
veitenas=columna.find_all('div',class_='veintena')
# Crear una instancia de la ventana
ventana = tk.Tk()

# Crear un label
etiqueta = tk.Label(ventana, text=titulo.text)
etiqueta.grid(row=0, column=0)
i=0
for veitena in veitenas:
    cantidadDiv=veitena.find_all('div')
    
    for cantidad in cantidadDiv:
        if i%2 == 0:
            etiqueta = tk.Label(ventana, text="p:" + cantidad.text)
            etiqueta.grid(row=1+i, column=0)
        else:
            etiqueta = tk.Label(ventana, text=" - " + cantidad. text)
            etiqueta.grid(row=1+i-1, column=1)
            
    
        i=i+1

# Empacar (colocar) el label en la ventana


# Iniciar el bucle principal de la aplicación
ventana.mainloop()