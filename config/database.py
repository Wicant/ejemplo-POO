import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase que gestiona la conexión a la base de datos implementando 
    el patrón Singleton para evitar múltiples instancias innecesarias
    """
    _instance = None
    _db_path = "ecotech.db"

    def __new__(cls): #cls clase en si
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls) #del padre llamamos pasamos la clase
        return cls._instance

    def get_connection(self) -> Connection: #conectarse y devolver la conexion y capacidad de consultar
        """
        Retorna una conexión a la base de datos SQLite
        """
        conn=sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row #Permite acceder a las columnas por nombre
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def init_db(self) -> None:
        """
        Inicializa la base de datos creando las tablas necesarias
        """
        conn = self.get_connection() #inicializa
        try:
            cursor: Cursor = conn.cursor()

            #cambiar la creación de tablas
            #persona
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleado ( --persona, empleado, administrador
                rut TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                correo TEXT NOT NULL,
                user TEXT NOT NULL,
                password TEXT NOT NULL,
                id_departamento INTEGER NOT NULL, --area de trabajo = departamento --area_trabajo
                sueldo INTEGER NOT NULL,
                inicio_contrato DATE NOT NULL,
                rol_admin BOOLEAN NOT NULL,
                estado TEXT NOT NULL,
                FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
            )
            """)

            #tabla informe (id_informe, fecha, tipo, formato)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS informe (
                id_informe INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha DATE NOT NULL,
                tipo TEXT NOT NULL,
                formato TEXT NOT NULL,
                id_usuario INTEGER NOT NULL, --aqui si o si debe ser un administrador
                FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE SET NULL
                    
            )
            """)

            # tabla departamento (id_departamento, nombre, gerente, presupuesto)
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    gerente TEXT,
                    presupuesto INTEGER NOT NULL,
                    FOREIGN KEY (gerente) REFERENCES empleado(rut) ON DELETE SET NULL
                )
                """
            )

            # tabla tiempo (id_tiempo, fecha, hora_entrada, hora_salida)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tiempo (
                    id_tiempo INTEGER PRIMARY KEY,
                    fecha DATE NOT NULL,
                    hora_entrada TIME NOT NULL,
                    hora_salida TIME NOT NULL,
                    id_empleado TEXT NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    FOREIGN KEY (id_empleado) REFERENCES empleado(rut) ON DELETE SET NULL,
                    FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE SET NULL
                )
                """
            )
            # tabla proyecto (id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin) /revisar diagramas
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    fecha_inicio DATE NOT NULL,
                    fecha_fin DATE NOT NULL,
                    ubicacion text NOT NULL
                )
                """
            )
            
            #cursor.execute(
                #"""
                #CREATE TABLE IF NOT EXISTS clima(
                    #id_clima                        INTEGER PRIMARY KEY AUTOINCREMENT,
                    #id_proyecto                     INTEGER,
                    #ubicacion                       TEXT, 
                    #temperatura_minima              REAL NOT NULL,
                    #temperatura_maxima              REAL NOT NULL, 
                    #humedad                         INTEGER NOT NULL,
                    #condicion                       TEXT NOT NULL,
                    #probabilidad_lluvia             INTEGER,
                    #fecha_consulta                  DATETIME NOT NULL,
                    #fecha_pronostico                DATETIME NOT NULL,
                    #FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE SET NULL                   
                #)
                #""
            #)
            conn.commit()
        except sqlite3.Error as e: 
            print(f"Error al inicializar la base de datos: {e}")
        finally:#pasa independientemente si falla o no el programa
            conn.close() #cierra conexión

if __name__ == "__main__":
    Database().init_db()
    print("Base de datos inicializada correctamente.")

            

    