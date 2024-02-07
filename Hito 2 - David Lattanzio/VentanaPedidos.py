import customtkinter as ctk
from tkinter import ttk
from Cliente import Cliente
from Pedido import Pedido
import VentanaClientes
import VentanaCategorias
import VentanaProductos
import VentanaDetalles
import Main


def mostrar_VentanaPedidos():
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

    def mostrar_ventanaClientes():
        app.destroy()
        VentanaClientes.mostrar_VentanaClientes()

    def mostrar_ventanaCategorias():
        app.destroy()
        VentanaCategorias.mostrar_VentanaCategorias()

    def mostrar_VentanaProductos():
        app.destroy()
        VentanaProductos.mostrar_VentanaProductos()

    def mostrar_VentanaDetalles():
        app.destroy()
        VentanaDetalles.mostrar_VentanaDetalles()

    sidebar = ctk.CTkFrame(master=app, width=200, height=480)
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    # Botón de Principal
    btnPrincipal = ctk.CTkButton(
        master=sidebar, text="Principal", command=mostrar_VentanaPrincipal
    )
    btnPrincipal.grid(row=0, column=0, padx=15, pady=(40, 5))

    # Botón de categoría
    btnCategoria = ctk.CTkButton(
        master=sidebar, text="Categoría", command=mostrar_ventanaCategorias
    )
    btnCategoria.grid(row=1, column=0, padx=15, pady=(15, 5))

    # Botón de clientes
    btnClientes = ctk.CTkButton(
        master=sidebar, text="Clientes", command=mostrar_ventanaClientes
    )
    btnClientes.grid(row=2, column=0, padx=15, pady=(15, 5))

    # Botón de productos
    btnProductos = ctk.CTkButton(
        master=sidebar, text="Productos", command=mostrar_VentanaProductos
    )
    btnProductos.grid(row=3, column=0, padx=15, pady=(15, 5))

    # Botón de Pedidos
    btnPedidos = ctk.CTkButton(master=sidebar, text="Pedidos")
    btnPedidos.grid(row=4, column=0, padx=15, pady=(15, 5))

    # Botón de Detalles
    btnDetalles = ctk.CTkButton(
        master=sidebar, text="Detalles", command=mostrar_VentanaDetalles
    )
    btnDetalles.grid(row=5, column=0, padx=15, pady=(15, 5))

    mainframe = ctk.CTkFrame(master=app, width=400, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    # PADIZQ, PADYDRC = 100,100

    PADIZQ, PADYDRC = 200, 200

    labelId_pedido = ctk.CTkLabel(mainframe, text="Id_pedido")
    labelId_pedido.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryId_pedido = ctk.CTkEntry(mainframe, placeholder_text="Id_pedido")
    entryId_pedido.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labeldniCliente = ctk.CTkLabel(mainframe, text="dniCliente")
    labeldniCliente.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entrydniCliente = ctk.CTkEntry(mainframe, placeholder_text="dniCliente")
    entrydniCliente.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelFecha_pedido = ctk.CTkLabel(mainframe, text="Fecha_pedido")
    labelFecha_pedido.grid(row=2, column=0, pady=(15, 5), padx=(PADIZQ, 50))

    entryFecha_pedido = ctk.CTkEntry(mainframe, placeholder_text="Fecha_pedido")
    entryFecha_pedido.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelEstado = ctk.CTkLabel(mainframe, text="Estado")
    labelEstado.grid(row=3, column=0, pady=(15, 5), padx=(PADIZQ, 50))

    entryEstado = ctk.CTkEntry(mainframe, placeholder_text="Estado")
    entryEstado.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))

    botonesFrame = ctk.CTkFrame(master=app, width=700, height=480)
    botonesFrame.pack(fill=ctk.BOTH, expand=True)

    pedido = Pedido()

    def insertarDatos():
        id_pedido = entryId_pedido.get()
        dniCliente = entrydniCliente.get()
        fecha_pedido = entryFecha_pedido.get()
        estado = entryEstado.get()

        pedido.insertarPedido(id_pedido, dniCliente, fecha_pedido, estado)

    treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    def buscarDatosConCliente():
        treeview.config(
            columns=("ID", "DNICliente", "Nombre", "Apellido", "Fecha_pedido", "Estado")
        )

        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=6, sticky="w")
        treeview.heading("ID", text="ID")
        treeview.heading("DNICliente", text="DNICliente")
        treeview.heading("Nombre", text="Nombre")
        treeview.heading("Apellido", text="Apellido")
        treeview.heading("Fecha_pedido", text="Fecha_pedido")
        treeview.heading("Estado", text="Estado")

        treeview.column("ID", width=50)
        treeview.column("DNICliente", width=80)
        treeview.column("Nombre", width=80)
        treeview.column("Apellido", width=80)
        treeview.column("Fecha_pedido", width=80)
        treeview.column("Estado", width=80)

        for resultado in pedido.obtenerPedidoConCliente():
            treeview.insert("", "end", values=resultado)

    def buscarDatosTabla():
        treeview.config(columns=("ID", "DNICliente", "Fecha_pedido", "Estado"))
        treeview.delete(*treeview.get_children())

        treeview.grid(row=8, column=0, rowspan=6, columnspan=4, sticky="w")
        treeview.heading("ID", text="ID")
        treeview.heading("DNICliente", text="DNICliente")
        treeview.heading("Fecha_pedido", text="Fecha_pedido")
        treeview.heading("Estado", text="Estado")
        treeview.column("ID", width=50)
        treeview.column("DNICliente", width=80)
        treeview.column("Fecha_pedido", width=80)
        treeview.column("Estado", width=80)

        for resultado in pedido.obtenerPedidoTabla():
            treeview.insert("", "end", values=resultado)

    def buscarDatosClienteMasActivo():
        treeview.config(columns=("cliente", "Apellido", "total_pedidos"))
        treeview.delete(*treeview.get_children())

        treeview.grid(row=8, column=0, rowspan=6, columnspan=2, sticky="w")
        treeview.heading("cliente", text="cliente")
        treeview.heading("total_pedidos", text="total_pedidos")
        treeview.heading("Apellido", text="Apellido")

        treeview.column("cliente", width=80)
        treeview.column("Apellido", width=80)
        treeview.column("total_pedidos", width=80)

        for resultado in pedido.obtenerClienteMasActivo():
            treeview.insert("", "end", values=resultado)

    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnListar = ctk.CTkButton(mainframe, text="Listar", command=buscarDatosTabla)
    btnListar.grid(row=5, column=1, pady=10)

    btnListarConCliente = ctk.CTkButton(
        mainframe, text="ListarConCliente", command=buscarDatosConCliente
    )
    btnListarConCliente.grid(row=6, column=0, pady=10)

    btnClienteActivo = ctk.CTkButton(
        mainframe, text="ClienteMásActivo", command=buscarDatosClienteMasActivo
    )
    btnClienteActivo.grid(row=6, column=1, pady=10)

    app.mainloop()
