import psycopg2
from tkinter import messagebox
import conexion as cx

def conexion():
    
    
    conn = psycopg2.connect(
        host="localhost",
        database="MIMAMOTO",
        user="postgres",
        password="Retrete33")

    # Creamos el cursor con el objeto conexion
    cur = conn.cursor()

    # Ejecutamos una consulta
    cur.execute( "SELECT * FROM cliente" )

    print(cur.fetchall())

    # Cerramos la conexión
    conn.close()
    

def ObtenerTodosLosClientes():

    conn=cx.conectar()
 
    # conn = psycopg2.connect(
    #         host="localhost",
    #         database="MIMAMOTO",
    #         user="postgres",
    #         password="Retrete33")

    # Creamos el cursor con el objeto conexion
    cur = conn.cursor()

    # Ejecutamos una consulta
    cur.execute( "SELECT id,dni,nombre_completo,correo,telefono,direccion FROM cliente order by id desc" )

    res =cur.fetchall()

    # Cerramos la conexión
    cx.cerrar_conexion(conn)
    return res

def ObtenerTodasLasMotos(cliente):
 
    conn=cx.conectar()
    

    # Creamos el cursor con el objeto conexion
    cur = conn.cursor()

    # Ejecutamos una consulta
    cur.execute( f"SELECT moto.id,moto.marca,moto.modelo,moto.año,moto.matricula,cliente.nombre_completo FROM moto inner join cliente on cliente.id=moto.propietario where moto.propietario = {cliente};" )

    res =cur.fetchall()

    # Cerramos la conexión
    cx.cerrar_conexion(conn)
    
    return res
def icono(ventana):
    ruta_icono = "favicon.ico"
    ventana.iconbitmap(ruta_icono)

def ObtenerDatosReparacion(cliente):
 
    conn=cx.conectar()
    

    # Creamos el cursor con el objeto conexion
    cur = conn.cursor()

    # Ejecutamos una consulta
    cur.execute( f"SELECT r.id,r.descripcion,TO_CHAR(r.fecha, 'DD/MM/YYYY'), r.precio_total, r.kilometros FROM reparacion r where r.cliente_id = {cliente} order by r.id desc;" )

    res =cur.fetchall()

    # Cerramos la conexión
    cx.cerrar_conexion(conn)
    
    return res
def eliminarMoto(idMoto):
    
    try:
        # Establecemos la conexión a la base de datos
        conn=cx.conectar()


        # Creamos el cursor con el objeto conexión
        cur = conn.cursor()

        # Ejecutamos la consulta DELETE
        cur.execute(f"DELETE FROM moto WHERE id = {idMoto};")
        conn.commit()

        # Cerramos la conexión
        cx.cerrar_conexion(conn)

    except psycopg2.errors.ForeignKeyViolation as e:
        # Manejamos la excepción de violación de clave foránea
        mensaje = f"Error al eliminar la moto con ID {idMoto}: {e}"
        messagebox.showerror("Esta moto tiene reparaciones Almacenadas. No se puede eliminar", mensaje)

    except Exception as e:
        # Manejamos otras excepciones generales
        mensaje = f"Error inesperado: {e}"
        messagebox.showerror("Error inesperado", mensaje)
        
def eliminarCliente(idCliente):
    
    try:
        # Establecemos la conexión a la base de datos
        conn=cx.conectar()


        # Creamos el cursor con el objeto conexión
        cur = conn.cursor()

        # Ejecutamos la consulta DELETE
        cur.execute(f"DELETE FROM cliente WHERE id = {idCliente};")
        conn.commit()

        # Cerramos la conexión
        cx.cerrar_conexion(conn)

    except psycopg2.errors.ForeignKeyViolation as e:
        # Manejamos la excepción de violación de clave foránea
        mensaje = f"Este cliente tiene motos guardadas. ID Cliente: {idCliente}: {e}"
        messagebox.showerror("Este cliente tiene motos guardadas.", mensaje)

    except Exception as e:
        # Manejamos otras excepciones generales
        mensaje = f"Error inesperado: {e}"
        messagebox.showerror("Error inesperado", mensaje)
    

def encontrarIdMotoPorMatricula(matricula):
    conn=cx.conectar()
    cur = conn.cursor()

    cur.execute(
       f"SELECT id FROM moto WHERE matricula = '{matricula}'"
        )
    res =cur.fetchone()

    cx.cerrar_conexion(conn)
    return res
    

def EjecutarConsulta(query):
    conn=cx.conectar()
    cur = conn.cursor()
    cur.execute(query)
    res =cur.fetchall()

    cx.cerrar_conexion(conn)
    print(res)
    return res


    

def insertarCliente(*datos):
    try:
        conn=cx.conectar()

        cur = conn.cursor()

        query = f"INSERT INTO cliente (nombre_completo, correo, telefono, direccion, dni) VALUES {datos}"
        cur.execute(query)
        conn.commit()

        cx.cerrar_conexion(conn)
            
    except psycopg2.errors.UniqueViolation as e:
        # Manejar la excepción UniqueViolation (clave duplicada)
        # Puedes obtener detalles específicos de la excepción desde `e`
        mensaje = "Error: Ya existe un registro con el mismo DNI."
        messagebox.showerror(message=mensaje, title="Error de inserción")
    except Exception as e:
        # Manejar cualquier otra excepción
        mensaje = "Se ha producido un error. Detalles: " + str(e)
        messagebox.showerror(message=mensaje, title="Error de inserción")
        

def insertarReparacion(*datos):
    try:
        conn=cx.conectar()

        cur = conn.cursor()

        query = f"INSERT INTO reparacion (descripcion,fecha,moto_id,cliente_id,precio_total,kilometros) VALUES {datos}"
        cur.execute(query)
        conn.commit()

        cx.cerrar_conexion(conn)
            
    except psycopg2.errors.UniqueViolation as e:
        # Manejar la excepción UniqueViolation (clave duplicada)
        # Puedes obtener detalles específicos de la excepción desde `e`
        mensaje = "Error: Ya existe un registro con el mism odato"
        messagebox.showerror(message=mensaje, title="Error de inserción")
    except Exception as e:
        # Manejar cualquier otra excepción
        mensaje = "Se ha producido un error. Detalles: " + str(e)
        messagebox.showerror(message=mensaje, title="Error de inserción")

def buscarClientePorId(clienteId):
    conn=cx.conectar()


    # Creamos el cursor con el objeto conexion
    cur = conn.cursor()

    # Ejecutamos una consulta
    cur.execute( f"SELECT nombre_completo FROM cliente where id = {clienteId}" )

    res =cur.fetchone()

    # Cerramos la conexión
    cx.cerrar_conexion(conn)
    
    return res

def insertarMoto(*datos):
    try:
        conn=cx.conectar()

        cur = conn.cursor()

        query = f"INSERT INTO moto (marca,modelo,año,matricula,propietario) VALUES {datos}"
        cur.execute(query)
        conn.commit()

        cx.cerrar_conexion(conn)




    except psycopg2.errors.UniqueViolation as e:
        # Manejar la excepción UniqueViolation (clave duplicada)
        # Puedes obtener detalles específicos de la excepción desde `e`
        mensaje = "Error: Ya existe un registro con el mismo DNI."
        messagebox.showerror(message=mensaje, title="Error de inserción")
    except Exception as e:
        # Manejar cualquier otra excepción
        mensaje = "Se ha producido un error. Detalles: " + str(e)
        messagebox.showerror(message=mensaje, title="Error de inserción")