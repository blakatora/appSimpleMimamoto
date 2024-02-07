import customtkinter as ctk
from Cliente import Cliente
from Categoria import Categoria
import VentanaPedidos
import VentanaClientes
import VentanaProductos
import VentanaDetalles
from tkinter import ttk
import Main


def mostrar_VentanaCategorias():
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
    btnCategoria = ctk.CTkButton(master=sidebar, text="Categoría")
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
    btnDetalles = ctk.CTkButton(
        master=sidebar, text="Detalles", command=mostrar_VentanaDetalles
    )
    btnDetalles.grid(row=5, column=0, padx=15, pady=(15, 5))

    mainframe = ctk.CTkFrame(master=app, width=400, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    # PADIZQ, PADYDRC = 100,100

    PADIZQ, PADYDRC = 200, 200

    labelId_categoria = ctk.CTkLabel(mainframe, text="Id_categoria")
    labelId_categoria.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryId_categoria = ctk.CTkEntry(mainframe, placeholder_text="Id_categoria")
    entryId_categoria.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labelCategoria = ctk.CTkLabel(mainframe, text="Categoria")
    labelCategoria.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryCategoria = ctk.CTkEntry(mainframe, placeholder_text="Categoria")
    entryCategoria.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    categoria = Categoria()

    def insertarDatos():
        Id_categoria = entryId_categoria.get()
        Categoria = entryCategoria.get()

        categoria.insertarCategoria(Id_categoria, Categoria)

    treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    def buscarDatosTabla():
        treeview.config(columns=("Id_categoria", "Categoria"))

        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=2, sticky="w")
        treeview.heading("Id_categoria", text="Id_categoria")
        treeview.heading("Categoria", text="Categoria")

        treeview.column("Id_categoria", width=80)
        treeview.column("Categoria", width=80)

        for resultado in categoria.obtenerCategoriaTabla():
            treeview.insert("", "end", values=resultado)

    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnBuscar = ctk.CTkButton(mainframe, text="Buscar", command=buscarDatosTabla)
    btnBuscar.grid(row=5, column=1, pady=10)

    app.mainloop()
