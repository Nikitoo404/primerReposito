import requests 

url="https://mantistec.com.ar/recursos/WebScraping.pdf"
peticion= requests.get(url)
if peticion.status_code == 200:
    # Acceder al contenido de la respuesta
    contenido_binario=peticion.content
    ruta_guardado = "WebScraping.pdf"

    # Abre el archivo en modo escritura y guarda el contenido de la respuesta en él
    with open(ruta_guardado, "wb") as archivo:
        archivo.write(contenido_binario)
    #el archivo descargado me aparece en la columna izquierda
