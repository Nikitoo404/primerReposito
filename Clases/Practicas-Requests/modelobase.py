import sqlite3
class BaseDatos():
    def __init__(self):
        self.bd="BaseQuinela.sqlite" 
        self.conexion=""
        self.cursor=""
        
    def conectar(self):
        self.conexion=sqlite3.connect(self.bd)
        self.cursor = self.conexion.cursor() 
    
    def actualizarBD(self,argumento):
        self.conectar()
        self.cursor.execute(argumento)
        self.conexion.commit()
        self.conexion.close()
    
    def consultar(self,argumento,cantidad=0):
        self.conectar()
        datos=self.cursor.execute(argumento)
        if cantidad ==1:
            fila=datos.fetchone()
            return fila
        else:
            fila=datos.fetchall()
            return fila
            
    def generarTablas(self):
        self.actualizarBD("""
                CREATE TABLE IF NOT EXISTS quinela
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT)
                """)

        self.actualizarBD("""
                    CREATE TABLE IF NOT EXISTS fecha
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha DATE)
                    """)

        self.actualizarBD("""
                    CREATE TABLE IF NOT EXISTS posicion
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        posicion INTEGER)
                    """)

        self.actualizarBD("""
                    CREATE TABLE IF NOT EXISTS Numeros
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_fecha INTEGER,
                        id_posicion INTEGER,
                        id_quinela INTEGER,
                        valor INTEGER
                        )
                    """)
    def encontrarTitulo(self,titulo):
        tituloEncontrado=self.consultar(f"""
                SELECT id FROM quinela WHERE nombre = '{titulo}'
                """,cantidad=1)



        if not tituloEncontrado:
            self.actualizarBD(f"""
                    INSERT INTO quinela (nombre) VALUES ('{titulo}') 
                    """)
            tituloEncontrado=self.consultar(f"""
                    SELECT id FROM quinela WHERE nombre = '{titulo}'
                    """,cantidad=1)
            
        return tituloEncontrado
    
    def encontrarFecha(self,fecha):
        fechaEncontrada=self.consultar(f"""
                                       SELECT * FROM fecha WHERE fecha = {fecha}
                                        """)
        if not fechaEncontrada:
            return False
        
        return True
    
    def crearFecha(self,fecha):
        self.actualizarBD(f"""
                                INSERT INTO fecha (fecha) VALUES ('{fecha}')
                                """)
        ultimaFecha=self.consultar(f"""
                            SELECT id FROM fecha ORDER BY id DESC
                        """,1)
        
        
        return ultimaFecha
    
        
    def encontrarPosicion(self,posicion):
        tituloPosicion=self.consultar(f"""
                SELECT id FROM posicion WHERE posicion = '{posicion}'
                """,cantidad=1)



        if not tituloPosicion:
            self.actualizarBD(f"""
                    INSERT INTO posicion (posicion) VALUES ('{posicion}') 
                    """)
            tituloPosicion=self.consultar(f"""
                    SELECT id FROM posicion WHERE posicion = '{posicion}'
                    """,cantidad=1)
            
        return tituloPosicion    
    
    def guardarNumero(self,id_fecha, id_posicion, id_quinela,numero):
        self.actualizarBD(f"""
                    INSERT INTO Numeros (id_fecha, id_posicion, id_quinela, valor)
                    VALUES ('{id_fecha}','{id_posicion}','{id_quinela}','{numero}') 
                    """)