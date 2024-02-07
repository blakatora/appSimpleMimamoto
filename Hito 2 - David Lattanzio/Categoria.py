import sqlite3 as sq


class Categoria:
    def __init__(self) -> None:
        conn = sq.connect("supermercado.db")
        conn.execute(
            """
            CREATE TABLE if not exists categorias (
                id_categoria INTEGER PRIMARY KEY,
                nombre VARCHAR(50)
            );

        """
        )
        conn.commit()
        conn.close()

    def insertarCategoria(self, *datos):
        conn = sq.connect("supermercado.db")
        query = f"insert into categorias values {datos}"
        conn.execute(query)
        conn.commit()
        conn.close()

    def obtenerCategoriaTabla(self):
        conn = sq.connect("supermercado.db")
        query = "Select * from categorias"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res
