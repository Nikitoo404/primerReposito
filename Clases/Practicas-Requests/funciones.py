from datetime import datetime
def formatearFecha(fecha):
    fechaCortada=fecha.split(" ") #divide nombre del dia, la fecha y la flecha en una lista
    fechaReal=fechaCortada[1][:8]  #busca el elemento 1 que es la fecha y muestra solo 8 char porque el resto es la flecha
    fecha_date = datetime.strptime(fechaReal, "%d/%m/%y").date()
    fechareal=str(fecha_date.day)+"/"+str(fecha_date.month)+"/"+str(fecha_date.year)
    return fechareal