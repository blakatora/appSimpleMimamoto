import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as sq


class Pedido:
    def __init__(self) -> None:
        conn = sq.connect("supermercado.db")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pedidos (
                id_pedido INTEGER PRIMARY KEY,
                dniCliente INTEGER,
                fecha_pedido datetime,
                estado varchar(30),
                foreign key (dniCliente) REFERENCES Clientes(DNI)
            )
        """
        )
        conn.commit()
        conn.close()

    def insertarPedido(self, *datos):
        conn = sq.connect("supermercado.db")
        query = f"insert into pedidos values {datos}"
        conn.execute(query)
        conn.commit()
        conn.close()

    def obtenerPedido(self, **kwargs):
        conn = sq.connect("supermercado.db")
        query = "SELECT * FROM pedidos"
        if kwargs:  # Verificar si se proporcionaron argumentos de búsqueda
            query += " WHERE " + " AND ".join(
                f"{key}='{value}'" for key, value in kwargs.items()
            )
        query += ";"
        res = conn.execute(query)
        resultados = [fila for fila in res]  # Almacenar los resultados en una lista
        conn.close()
        return resultados

    def obtenerPedidoConCliente(self):
        conn = sq.connect("supermercado.db")
        query = "SELECT p.id_pedido, p.dniCliente, c.nombreCliente, c.ApellidoCliente, p.fecha_pedido, p.estado FROM pedidos p inner join clientes c on p.dniCliente = c.DNI"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res

    def obtenerPedidoTabla(self):
        conn = sq.connect("supermercado.db")
        query = "Select * from pedidos"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res

    def obtenerClienteMasActivo(self):
        conn = sq.connect("supermercado.db")
        query = "SELECT c.nombreCliente AS cliente, c.ApellidoCliente as Apellido, COUNT(*) AS total_pedidos FROM clientes c inner JOIN pedidos p ON c.DNI = p.dniCliente GROUP BY c.DNI ORDER BY total_pedidos DESC LIMIT 5"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res

    def graficoClienteMasActivo(self):
        conn = sq.connect("supermercado.db")
        query = "SELECT c.nombreCliente AS cliente, c.ApellidoCliente as Apellido, COUNT(*) AS total_pedidos FROM clientes c inner JOIN pedidos p ON c.DNI = p.dniCliente GROUP BY c.DNI ORDER BY total_pedidos DESC LIMIT 5"
        df = pd.read_sql_query(query, conn)         
        conn.close()
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(df['cliente'] + ' ' + df['Apellido'], df['total_pedidos'])
        ax.set_xlabel('Cliente')
        ax.set_ylabel('Total de Pedidos')
        ax.set_title('Top 5 Clientes con más Pedidos')
        # ax.tick_params(axis='x', rotation=45, ha='right')
        plt.tight_layout()
    
        return fig

        