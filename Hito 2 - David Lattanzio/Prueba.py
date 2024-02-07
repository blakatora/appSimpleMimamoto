import sqlite3 as sq
from Pedido import Pedido

conn = sq.connect("prueba.db")


def insertar(tabla, *datos):
    query = f"insert into {tabla} values {datos}"
    conn.execute(query)
    conn.commit()
    conn.close()


# insertar("tabla",3,"adios")


def modificar(tabla, columna, dato, id):
    query = f'update {tabla} set "{columna}" = "{dato}" where id = {id}'
    conn.execute(query)
    conn.commit()
    conn.close()


# modificar("tabla", "nombre", "DATO", 1)


# Con  kwargs se puede pasar muchos argumentos como clave-valor
def select(tabla, **kwargs):
    query = f"SELECT * FROM {tabla}"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    res = conn.execute(query)
    for fila in res:
        for dato in fila:
            print(dato, end=" ")


# select("tabla",nombre="DATO")

pedido = Pedido()
print(pedido.obtenerPedidoTabla())
print(pedido.obtenerClienteMasActivo())
