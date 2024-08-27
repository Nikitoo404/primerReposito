import cv2
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tkinter import *
import numpy as np

#--------------------------- Función para el Login Facial --------------------------------------------
def login_facial():
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()
        kpa, descr_a = orb.detectAndCompute(img1, None)
        kpb, descr_b = orb.detectAndCompute(img2, None)
        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = comp.match(descr_a, descr_b)
        regiones_similares = [i for i in matches if i.distance < 70]
        if len(matches) == 0:
            return 0
        return len(regiones_similares) / len(matches)

    # Limpiar los mensajes anteriores
    label_resultado.config(text="")
    pantalla.update()

    # Mostrar mensaje de iniciando
    label_iniciando.config(text="Iniciando reconocimiento facial...")
    pantalla.update()

    # Capturar la imagen
    cap = cv2.VideoCapture(0)
    
    # Eliminar el mensaje de "Iniciando" después de iniciar la cámara
    label_iniciando.config(text="")
    pantalla.update()
    
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('Login Facial', frame)
        if cv2.waitKey(1) == 27:  # Presionar "Esc" para romper el bucle
            break
    cv2.imwrite("captura.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()

    # Obtener la ruta del directorio donde se encuentra el script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Leer la captura
    rostro_log = cv2.imread("captura.jpg", 0)

    # Inicializar variables para determinar la mejor coincidencia
    mejor_similitud = 0
    mejor_carpeta = None
    resultados = []

    # Recorrer las carpetas y comparar las imágenes
    for carpeta in os.listdir(current_dir):
        carpeta_path = os.path.join(current_dir, carpeta)
        if os.path.isdir(carpeta_path):
            # Obtener la imagen dentro de la carpeta
            for archivo in os.listdir(carpeta_path):
                image_path = os.path.join(carpeta_path, archivo)
                if os.path.isfile(image_path):
                    rostro_reg = cv2.imread(image_path, 0)
                    similitud = orb_sim(rostro_log, rostro_reg)
                    resultados.append((carpeta, similitud))
                    if similitud > mejor_similitud:
                        mejor_similitud = similitud
                        mejor_carpeta = carpeta

    # Mostrar el resultado en la interfaz
    if mejor_carpeta and mejor_similitud >= 0.90:  # Umbral de similitud
        label_resultado.config(text=f"Reconocimiento exitoso: {mejor_carpeta}", fg="green")
        print(f"Registro correcto: {mejor_carpeta}")
        print(f"Compatibilidad con la foto del registro: {mejor_similitud:.2f}")
    else:
        label_resultado.config(text="No se reconoció ningún rostro con suficiente similitud.", fg="red")

    # Mostrar los resultados de las carpetas en la terminal
    for carpeta, similitud in resultados:
        if carpeta != mejor_carpeta or mejor_similitud < 0.90:
            print(f"Incompatibilidad con {carpeta}: {similitud:.2f}")

#------------------------- Función de nuestra pantalla principal ------------------------------------------------
def pantalla_principal():
    global pantalla, label_iniciando, label_resultado
    pantalla = Tk()
    pantalla.title("Reconocimiento facial")

    # Centramos la ventana en la pantalla
    window_width = 350
    window_height = 200
    screen_width = pantalla.winfo_screenwidth()
    screen_height = pantalla.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    pantalla.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    Label(text="Registro automático", bg="gray", width="300", height="2", font=("Verdana", 13)).pack()

    Label(text="").pack()  # Espacio entre el título y el primer botón
    Button(text="Iniciar reconocimiento facial", height="2", width="30", command=login_facial).pack()
    
    Label(text="").pack # Espacio entre el primer botón y el segundo
    Button(text="")

    # Etiqueta para mostrar "Iniciando reconocimiento facial..."
    label_iniciando = Label(pantalla, text="", font=("Calibri", 11))
    label_iniciando.pack()

    # Etiqueta para mostrar el resultado del reconocimiento
    label_resultado = Label(pantalla, text="", font=("Calibri", 11))
    label_resultado.pack()

    pantalla.mainloop()

pantalla_principal()
