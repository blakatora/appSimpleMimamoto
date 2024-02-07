import customtkinter as ctk
from Productos import Productos
import VentanaPedidos
import VentanaClientes
import VentanaCategorias
import VentanaProductos
import VentanaDetalles
from tkinter import ttk
import Main


def mostrar_VentanaProductos():
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

    def mostrar_VentanaCategorias():
        app.destroy()
        VentanaCategorias.mostrar_VentanaCategorias()

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
        master=sidebar, text="Productos")
    btnProductos.grid(row=3, column=0, padx=15, pady=(15, 5))

    # Botón de Pedidos
    btnPedidos = ctk.CTkButton(
        master=sidebar, text="Pedidos", command=mostrar_VentanaPedidos
    )
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

    labelId_producto = ctk.CTkLabel(mainframe, text="Id_producto")
    labelId_producto.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryId_producto = ctk.CTkEntry(mainframe, placeholder_text="Id_producto")
    entryId_producto.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labelNombre = ctk.CTkLabel(mainframe, text="Nombre")
    labelNombre.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryNombre = ctk.CTkEntry(mainframe, placeholder_text="Nombre")
    entryNombre.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelPrecio = ctk.CTkLabel(mainframe, text="Precio")
    labelPrecio.grid(row=2, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryPrecio = ctk.CTkEntry(mainframe, placeholder_text="Precio")
    entryPrecio.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelCantidad = ctk.CTkLabel(mainframe, text="Cantidad")
    labelCantidad.grid(row=3, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryCantidad = ctk.CTkEntry(mainframe, placeholder_text="Cantidad")
    entryCantidad.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelId_Categoria = ctk.CTkLabel(mainframe, text="Id_Categoria")
    labelId_Categoria.grid(row=4, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryId_Categoria = ctk.CTkEntry(mainframe, placeholder_text="Id_Categoria")
    entryId_Categoria.grid(row=4, column=1, pady=(15, 5), padx=(0, PADYDRC))

    productos = Productos()

    def insertarDatos():
        Id_producto = entryId_producto.get()
        Nombre = entryNombre.get()
        Precio = entryPrecio.get()
        Cantidad = entryCantidad.get()
        Id_Categoria = entryId_Categoria.get()

        productos.insertarProductos(Id_producto, Nombre, Precio, Cantidad, Id_Categoria)

    treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    def buscarDatosTabla():
        treeview.config(
            columns=("Id_producto", "Nombre", "Precio", "Cantidad", "Id_Categoria")
        )

        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=5, sticky="w")
        treeview.heading("Id_producto", text="Id_producto")
        treeview.heading("Nombre", text="Nombre")
        treeview.heading("Precio", text="Precio")
        treeview.heading("Cantidad", text="Cantidad")
        treeview.heading("Id_Categoria", text="Id_Categoria")

        treeview.column("Id_producto", width=80)
        treeview.column("Nombre", width=120)
        treeview.column("Precio", width=80)
        treeview.column("Cantidad", width=80)
        treeview.column("Id_Categoria", width=80)

        for resultado in productos.obtenerProductosTabla():
            treeview.insert("", "end", values=resultado)

    def buscarDatosProductosMasVendidos():
        treeview.config(
            columns=("Producto", "Cantidad_total", "Cliente")
        )
        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=5, sticky="w")
        treeview.heading("Producto", text="Producto")
        treeview.heading("Cantidad_total", text="Cantidad_total")
        treeview.heading("Cliente", text="Cliente")
        
        treeview.column("Producto", width=80)
        treeview.column("Cantidad_total", width=120)
        treeview.column("Cliente", width=120)
        
        for resultado in productos.obtenerProductosMasVendidos():
            treeview.insert("", "end", values=resultado)
        
        
    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnBuscar = ctk.CTkButton(mainframe, text="Buscar", command=buscarDatosTabla)
    btnBuscar.grid(row=5, column=1, pady=10)
    
    btnBuscarProductosMasVendidos = ctk.CTkButton(mainframe, text="BuscarProductosMásVendidos", command=buscarDatosProductosMasVendidos)
    btnBuscarProductosMasVendidos.grid(row=6, column=0, pady=10)

    app.mainloop()
