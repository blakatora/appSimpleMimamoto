import psycopg2
# postgresql://rodriguez.alv23:xVNsGfY8U0bl@ep-soft-field-45352543.eu-central-1.aws.neon.tech/mimamoto?sslmode=requiredef conectar():
def conectar():
    
    try:
        conn = psycopg2.connect(
            host="ep-soft-field-45352543.eu-central-1.aws.neon.tech",
            database="mimamoto",
            user="rodriguez.alv23",
            password="xVNsGfY8U0bl"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# def conectar():
    
    
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="MIMAMOTO",
#             user="postgres",
#             password="Retrete33"
#         )
#         return conn
#     except psycopg2.Error as e:
#         print(f"Error al conectar a la base de datos: {e}")
#         return None

def cerrar_conexion(conn):
    if conn:
        conn.close()