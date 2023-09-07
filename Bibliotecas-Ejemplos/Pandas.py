import pandas

data = {'Nombre': ['Juan', 'María', 'Pedro', 'Lucía'],
        'Edad': [25, 32, 18, 27],
        'Ciudad': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza']}
df = pandas.DataFrame(data)

print(df)
#acá muestra una tabla que contiene de columnas: nombre, edad y ciudad en X, y en Y tiene enumerado cada fila
#cada fila tiene, por ej: Juan 25 Buenos Aires. Y así...

#Para hacer un cálculo:
edad_promedio = df['Edad'].mean()
#saca la media de todos los valores que contienen la lista 'Edad'
print("La edad promedio es:", edad_promedio)
