import customtkinter as ctk
from tkinter import ttk
from Cliente import Cliente
import VentanaPedidos
import VentanaCategorias
import VentanaDetalles
import VentanaProductos



def mostrar_VentanaClientes():
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    appClientes = ctk.CTk()  # create CTk window like you do with the Tk window
    # appClientes.geometry("700x480")
    appClientes.geometry("1000x800")

    def button_function():
        print("button pressed")

    def mostrar_VentanaPrincipal():
        appClientes.destroy()
        import Main
        Main.ventanaPrincipal()

    def mostrar_VentanaPedidos():
        appClientes.destroy()
        VentanaPedidos.mostrar_VentanaPedidos()

    def mostrar_VentanaCategorias():
        appClientes.destroy()
        VentanaCategorias.mostrar_VentanaCategorias()

    def mostrar_VentanaProductos():
        appClientes.destroy()
        VentanaProductos.mostrar_VentanaProductos()

    def mostrar_VentanaDetalles():
        appClientes.destroy()
        VentanaDetalles.mostrar_VentanaDetalles()

    sidebar = ctk.CTkFrame(master=appClientes, width=200, height=480)
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
    btnClientes = ctk.CTkButton(master=sidebar, text="Clientes")
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

    mainframe = ctk.CTkFrame(master=appClientes, width=400, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    # PADIZQ, PADYDRC = 100,100

    PADIZQ, PADYDRC = 200, 200

    labelDNI = ctk.CTkLabel(mainframe, text="DNI")
    labelDNI.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryDNI = ctk.CTkEntry(mainframe, placeholder_text="DNI")
    entryDNI.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labelNombre = ctk.CTkLabel(mainframe, text="Nombre")
    labelNombre.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryNombre = ctk.CTkEntry(mainframe, placeholder_text="Nombre")
    entryNombre.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelApellido = ctk.CTkLabel(mainframe, text="Apellido")
    labelApellido.grid(row=2, column=0, pady=(15, 5), padx=(PADIZQ, 50))

    entryApellido = ctk.CTkEntry(mainframe, placeholder_text="Apellido")
    entryApellido.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelEmail = ctk.CTkLabel(mainframe, text="Email")
    labelEmail.grid(row=3, column=0, pady=(15, 5), padx=(PADIZQ, 50))

    entryEmail = ctk.CTkEntry(mainframe, placeholder_text="Email")
    entryEmail.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelTelefono = ctk.CTkLabel(mainframe, text="Telefono")
    labelTelefono.grid(row=4, column=0, pady=(15, 5), padx=(PADIZQ, 50))

    entryTelefono = ctk.CTkEntry(mainframe, placeholder_text="Telefono")
    entryTelefono.grid(row=4, column=1, pady=(15, 5), padx=(0, PADYDRC))

    botonesFrame = ctk.CTkFrame(master=appClientes, width=700, height=480)
    botonesFrame.pack(fill=ctk.BOTH, expand=True)

    cliente = Cliente()

    def insertarDatos():
        dni = entryDNI.get()
        nombre = entryNombre.get()
        apellido = entryApellido.get()
        email = entryEmail.get()
        telefono = entryTelefono.get()

        cliente.insertarCliente(dni, nombre, apellido, email, telefono)

    treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    def buscarDatosTabla():
        treeview.config(
            columns=(
                "DNI",
                "nombreCliente",
                "ApellidoCliente",
                "emailCliente",
                "telefonoCliente",
            )
        )

        treeview.delete(*treeview.get_children())
        treeview.grid(row=8, column=0, rowspan=6, columnspan=6, sticky="w")
        treeview.heading("DNI", text="DNI")
        treeview.heading("nombreCliente", text="nombreCliente")
        treeview.heading("ApellidoCliente", text="ApellidoCliente")
        treeview.heading("emailCliente", text="emailCliente")
        treeview.heading("telefonoCliente", text="telefonoCliente")

        treeview.column("DNI", width=50)
        treeview.column("nombreCliente", width=80)
        treeview.column("ApellidoCliente", width=80)
        treeview.column("emailCliente", width=80)
        treeview.column("telefonoCliente", width=80)

        for resultado in cliente.obtenerClienteTabla():
            treeview.insert("", "end", values=resultado)

    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnBuscar = ctk.CTkButton(mainframe, text="Buscar", command=buscarDatosTabla)
    btnBuscar.grid(row=5, column=1, pady=10)

    appClientes.mainloop()
