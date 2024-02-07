import sqlite3 as sq


class Cliente:
    def __init__(self) -> None:
        conn = sq.connect("supermercado.db")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                DNI INTEGER PRIMARY KEY,
                nombreCliente VARCHAR(15),
                ApellidoCliente VARCHAR(20),
                emailCliente varchar(50),
                telefonoCliente varchar(10)
            )
        """
        )
        conn.commit()
        conn.close()

    # def inicializarCliente(self):
    #     conn = sq.connect('supermercado.db')
    #     conn.execute('''
    #         CREATE TABLE IF NOT EXISTS clientes (
    #             DNI INTEGER PRIMARY KEY,
    #             nombreCliente VARCHAR(15),
    #             ApellidoCliente VARCHAR(20),
    #             emailCliente varchar(50),
    #             telefonoCliente varchar(10)
    #         )
    #     ''')
    #     conn.commit()
    #     conn.close()

    def insertarCliente(self, *datos):
        conn = sq.connect("supermercado.db")
        query = f"insert into clientes values {datos}"
        conn.execute(query)
        conn.commit()
        conn.close()

    # def obtenerClientes(self, **kwargs):
    #     conn = sq.connect("supermercado.db")
    #     query = f"SELECT * FROM clientes"
    #     i = 0
    #     for key, value in kwargs.items():
    #         if i == 0:
    #             query += " WHERE "
    #         else:
    #             query += " AND "
    #         query += "{}='{}'".format(key, value)
    #         i += 1
    #     query += ";"
    #     res = conn.execute(query)
    #     resultados = []
    #     for fila in res:
    #         resultados.append(fila)
    #         conn.close()
    #         return resultados
    def obtenerClientes(self, **kwargs):
        conn = sq.connect("supermercado.db")
        query = "SELECT * FROM clientes"
        if kwargs:  # Verificar si se proporcionaron argumentos de búsqueda
            query += " WHERE " + " AND ".join(
                f"{key}='{value}'" for key, value in kwargs.items()
            )
        query += ";"
        res = conn.execute(query)
        resultados = [fila for fila in res]  # Almacenar los resultados en una lista
        conn.close()
        return resultados

    def obtenerClienteTabla(self):
        conn = sq.connect("supermercado.db")
        query = "Select * from clientes"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res


