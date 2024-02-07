import customtkinter as ctk
from Detalle import Detalle

import VentanaPedidos
import VentanaClientes
import VentanaProductos
import VentanaCategorias
from tkinter import ttk
import Main


def mostrar_VentanaDetalles():
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = ctk.CTk()  # create CTk window like you do with the Tk window
    # app.geometry("700x480")
    app.geometry("1000x800")

    def button_function():
        print("button pressed")

    def mostrar_VentanaPrincipal():
        app.destroy()
        Main.ventanaPrincipal()

    def mostrar_VentanaPedidos():
        app.destroy()
        VentanaPedidos.mostrar_VentanaPedidos()

    def mostrar_VentanaClientes():
        app.destroy()
        VentanaClientes.mostrar_VentanaClientes()

    def mostrar_VentanaProductos():
        app.destroy()
        VentanaProductos.mostrar_VentanaProductos()

    def mostrar_VentanaCategorias():
        app.destroy()
        VentanaCategorias.mostrar_VentanaCategorias()

    sidebar = ctk.CTkFrame(master=app, width=200, height=480)
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    # Botón de Principal
    btnPrincipal = ctk.CTkButton(
        master=sidebar, text="Principal", command=mostrar_VentanaPrincipal
    )
    btnPrincipal.grid(row=0, column=0, padx=15, pady=(40, 5))

    # Botón de categoría
    btnCategoria = ctk.CTkButton(
        master=sidebar, text="Categoría", command=mostrar_VentanaCategorias
    )
    btnCategoria.grid(row=1, column=0, padx=15, pady=(15, 5))

    # Botón de clientes
    btnClientes = ctk.CTkButton(
        master=sidebar, text="Clientes", command=mostrar_VentanaClientes
    )
    btnClientes.grid(row=2, column=0, padx=15, pady=(15, 5))

    # Botón de productos
    btnProductos = ctk.CTkButton(
        master=sidebar, text="Productos", command=mostrar_VentanaProductos
    )
    btnProductos.grid(row=3, column=0, padx=15, pady=(15, 5))

    # Botón de Pedidos
    btnPedidos = ctk.CTkButton(
        master=sidebar, text="Pedidos", command=mostrar_VentanaPedidos
    )
    btnPedidos.grid(row=4, column=0, padx=15, pady=(15, 5))

    # Botón de Detalles
    btnDetalles = ctk.CTkButton(master=sidebar, text="Detalles")
    btnDetalles.grid(row=5, column=0, padx=15, pady=(15, 5))

    mainframe = ctk.CTkFrame(master=app, width=400, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    # PADIZQ, PADYDRC = 100,100

    PADIZQ, PADYDRC = 200, 200

    labelId_detalle = ctk.CTkLabel(mainframe, text="Id_detalle")
    labelId_detalle.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryId_detalle = ctk.CTkEntry(mainframe, placeholder_text="Id_detalle")
    entryId_detalle.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labelId_pedido = ctk.CTkLabel(mainframe, text="Id_pedido")
    labelId_pedido.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryId_pedido = ctk.CTkEntry(mainframe, placeholder_text="Id_pedido")
    entryId_pedido.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelId_producto = ctk.CTkLabel(mainframe, text="Id_producto")
    labelId_producto.grid(row=2, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryId_producto = ctk.CTkEntry(mainframe, placeholder_text="Id_producto")
    entryId_producto.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelCantidad = ctk.CTkLabel(mainframe, text="Cantidad")
    labelCantidad.grid(row=3, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryCantidad = ctk.CTkEntry(mainframe, placeholder_text="Cantidad")
    entryCantidad.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))

    detalle = Detalle()

    def insertarDatos():
        Id_detalle = entryId_detalle.get()
        Id_pedido = entryId_pedido.get()
        Id_producto = entryId_producto.get()
        Cantidad = entryCantidad.get()

        detalle.insertarDetalles(Id_detalle, Id_pedido, Id_producto, Cantidad)

    treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    def buscarDatosTabla():
        treeview.config(columns=("dniCliente", "fecha_pedido", "Producto", "PrecioTotal"))

        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=2, sticky="w")
        treeview.heading("dniCliente", text="dniCliente")
        treeview.heading("fecha_pedido", text="fecha_pedido")
        treeview.heading("Producto", text="Producto")
        treeview.heading("PrecioTotal", text="PrecioTotal")

        treeview.column("dniCliente", width=80)
        treeview.column("fecha_pedido", width=80)
        treeview.column("Producto", width=80)
        treeview.column("PrecioTotal", width=80)

        for resultado in detalle.obtenerDetalles():
            treeview.insert("", "end", values=resultado)

    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnBuscar = ctk.CTkButton(mainframe, text="Buscar", command=buscarDatosTabla)
    btnBuscar.grid(row=5, column=1, pady=10)

    app.mainloop()
