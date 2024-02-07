import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt



class Productos:
    def __init__(self) -> None:
        conn = sq.connect("supermercado.db")
        conn.execute(
            """
            CREATE TABLE if not exists productos (
                id_producto INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                precio DECIMAL(10, 2),
                cantidad INTEGER,
                id_categoria INTEGER,
                FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
            );

        """
        )
        conn.commit()
        conn.close()

    def insertarProductos(self, *datos):
        conn = sq.connect("supermercado.db")
        query = f"insert into productos values {datos}"
        conn.execute(query)
        conn.commit()
        conn.close()

    def obtenerProductosTabla(self):
        conn = sq.connect("supermercado.db")
        query = "Select * from productos"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res

    def obtenerProductosMasVendidos(self):
        conn = sq.connect("supermercado.db")
        query = "select prod.nombre as Producto, sum(d.cantidad) as cantidad_total from productos prod inner join detalles d on d.id_producto = prod.id_producto inner join pedidos p on p.id_pedido = d.id_pedido where p.fecha_pedido between '2023-01-01' and '2023-12-31' group by prod.nombre order by cantidad_total desc limit 5"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res
    
    def graficoProductsoMasVendidos(self):
        conn = sq.connect("supermercado.db")
        query = "select prod.nombre as Producto, sum(d.cantidad) as cantidad_total from productos prod inner join detalles d on d.id_producto = prod.id_producto inner join pedidos p on p.id_pedido = d.id_pedido where p.fecha_pedido between '2023-01-01' and '2023-12-31' group by prod.nombre order by cantidad_total desc limit 5"
        df = pd.read_sql_query(query, conn)         
        conn.close()
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(df['Producto'], df['cantidad_total'])
        ax.set_xlabel('Producto')
        ax.set_ylabel('Cantidad_total')
        ax.set_title('Productos más vendidos')
        # ax.tick_params(axis='x', rotation=45, ha='right')
        plt.tight_layout()
        return fig

    