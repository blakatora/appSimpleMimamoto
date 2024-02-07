import customtkinter as ctk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import VentanaPedidos
import VentanaCategorias
import VentanaDetalles
import VentanaProductos
from Pedido import Pedido
from Productos import Productos


def ventanaPrincipal():
   
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = ctk.CTk()  # create CTk window like you do with the Tk window
    app.geometry("1000x800")
    app.title("ventanaPrincipal")

    def button_function():
        print("button pressed")

    def ventanaClientes():
        app.destroy()
        import VentanaClientes
        VentanaClientes.mostrar_VentanaClientes()

    def ventanaPedidos():
        app.destroy()
        VentanaPedidos.mostrar_VentanaPedidos()

    def ventanaCategorias():
        app.destroy()
        VentanaCategorias.mostrar_VentanaCategorias()

    def ventanaProductos():
        app.destroy()
        VentanaProductos.mostrar_VentanaProductos()

    def mostrar_VentanaDetalles():
        app.destroy()
        VentanaDetalles.mostrar_VentanaDetalles()

    sidebar = ctk.CTkFrame(master=app, width=200, height=480)
    sidebar.pack(side=ctk.LEFT, fill=ctk.Y)

    # Botón de Principal
    btnPrincipal = ctk.CTkButton(
        master=sidebar, text="Principal")
    btnPrincipal.grid(row=0, column=0, padx=15, pady=(40, 5))

    # Botón de categoría
    btnCategoria = ctk.CTkButton(
        master=sidebar, text="Categoría", command=ventanaCategorias
    )
    btnCategoria.grid(row=1, column=0, padx=15, pady=(15, 5))

    # Botón de clientes
    btnClientes = ctk.CTkButton(
        master=sidebar, text="Clientes", command=ventanaClientes
    )
    btnClientes.grid(row=2, column=0, padx=15, pady=(15, 5))

    # Botón de productos
    btnProductos = ctk.CTkButton(
        master=sidebar, text="Productos", command=ventanaProductos
    )
    btnProductos.grid(row=3, column=0, padx=15, pady=(15, 5))

    # Botón de Pedidos
    btnPedidos = ctk.CTkButton(master=sidebar, text="Pedidos", command=ventanaPedidos)
    btnPedidos.grid(row=4, column=0, padx=15, pady=(15, 5))

    # Botón de Detalles
    btnDetalles = ctk.CTkButton(
        master=sidebar, text="Detalles", command=mostrar_VentanaDetalles
    )
    btnDetalles.grid(row=5, column=0, padx=15, pady=(15, 5))

    mainframe = ctk.CTkFrame(master=app, width=400, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    pedido = Pedido()
    producto = Productos()
    def mostrarGraficoClienteMasActivo():
        grafico = pedido.graficoClienteMasActivo()
        canvas = FigureCanvasTkAgg(grafico, master= mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, padx=15, pady=(10, 5))
        
    def mostrarGraficoProductosMasVendidos():
        grafico = producto.graficoProductsoMasVendidos()
        canvas = FigureCanvasTkAgg(grafico, master= mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, padx=15, pady=(10, 5))
        
    btnGraficoClienteMasPedidos = ctk.CTkButton(master=mainframe, text="Gráfico clientes más activos", command=mostrarGraficoClienteMasActivo)
    btnGraficoClienteMasPedidos.grid(row=0, column=0, padx=15, pady=(40, 5))
    
    btnGraficoClienteMasPedidos = ctk.CTkButton(master=mainframe, text="Gráfico productos más vendidos", command=mostrarGraficoProductosMasVendidos)
    btnGraficoClienteMasPedidos.grid(row=0, column=1, padx=15, pady=(40, 5))



    app.mainloop()


ventanaPrincipal()
