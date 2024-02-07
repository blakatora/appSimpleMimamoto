import sqlite3 as sq


class Detalle:
    def __init__(self) -> None:
        conn = sq.connect("supermercado.db")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS detalles (
                id_detalle INTEGER PRIMARY KEY,
                id_pedido INTEGER,
                id_producto INTEGER,
                cantidad INTEGER,
                foreign key (id_pedido) REFERENCES pedidos(id_pedido),
                foreign key (id_producto) REFERENCES productos(id_producto)
            )
        """
        )
        conn.commit()
        conn.close()

    def insertarDetalles(self, id_detalle,id_pedido, id_producto, cantidad):
        conn = sq.connect("supermercado.db")
        query = f"insert into detalles values ({id_detalle},{id_pedido},{id_producto}, {cantidad})"
        conn.execute(query)
        conn.commit()
        conn.close()

    def obtenerDetalles(self):
        conn = sq.connect("supermercado.db")
        query = "select p.dniCliente, p.fecha_pedido, prod.nombre, (prod.precio * det.cantidad) as precioTotal from detalles det inner join pedidos p on p.id_pedido = det.id_pedido inner join productos prod on prod.id_producto = det.id_producto"
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetchall()
        return res
