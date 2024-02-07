import customtkinter as ctk
from tkinter import ttk
import FuncionesConexion
from tkinter import messagebox
import tkinter as tk


def obtenerClienteReparacion(id_seleccionadoMoto):
    # obtener cliente por id de moto
    res=FuncionesConexion.EjecutarConsulta(f"select moto.propietario from moto where moto.id={id_seleccionadoMoto};")
    return res[0][0]
    # print(res[0])

def mostrarDatosReparaciones(id_seleccionadoMoto):  
    
    treeviewReparaciones.delete(*treeviewReparaciones.get_children())        

    treeviewReparaciones.config(
        columns=("ID","Descripción", "Fecha", "Precio Total","Kilometros")
    )
    treeviewReparaciones.grid(row=9, column=0, rowspan=6, columnspan=7, sticky="w",padx=(20,100))


    treeviewReparaciones.heading("ID", text="ID")
    treeviewReparaciones.heading("Descripción", text="Descripción")
    treeviewReparaciones.heading("Fecha", text="Fecha")
    treeviewReparaciones.heading("Precio Total", text="Precio Total")
    treeviewReparaciones.heading("Kilometros", text="Kilometros")



    # Ajustar anchos de columna después de la creación del Treeview
    treeviewReparaciones.column("ID", width=60)
    treeviewReparaciones.column("Descripción", width=100)
    treeviewReparaciones.column("Fecha", width=200)
    treeviewReparaciones.column("Precio Total", width=200)
    treeviewReparaciones.column("Kilometros", width=200)




    for resultado in FuncionesConexion.ObtenerDatosReparacion(obtenerClienteReparacion(id_seleccionadoMoto)):
            treeviewReparaciones.insert("", "end", values=resultado)
   
    
    
def creaVentanaReparacion(appClientes, id_seleccionadoMoto):
    def insertarReparacion():
        descripcionReparacion = entryDescripcion.get()
        fechaReparacion = entryFecha.get()
        cliente_idReparacion = obtenerClienteReparacion(id_seleccionadoMoto)
        precio_totalReparacion = entryPrecio.get()
        kilometrosReparacion = entryKilometros.get()

        cliente_idReparacion = obtenerClienteReparacion(id_seleccionadoMoto)

        FuncionesConexion.insertarReparacion(
            descripcionReparacion,
            fechaReparacion,
            id_seleccionadoMoto,
            cliente_idReparacion,
            precio_totalReparacion,
            kilometrosReparacion
        )

        mostrarDatosReparaciones(id_seleccionadoMoto)

    VentanaReparacion = ctk.CTkToplevel(appClientes)
    VentanaReparacion.geometry("1200x800")

    ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    VentanaReparacion.title("Reparaciones Mimamoto")
    FuncionesConexion.icono(VentanaReparacion)

    mainframe = ctk.CTkFrame(master=VentanaReparacion, width=100, height=480)
    mainframe.pack(fill=ctk.BOTH, expand=True)

    global treeviewReparaciones
    treeviewReparaciones = ttk.Treeview(mainframe, show="headings", selectmode="browse")

    PADIZQ, PADYDRC = 400, 200

    labelDescripcion = ctk.CTkLabel(mainframe, text="Descripción")
    labelDescripcion.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

    entryDescripcion = ctk.CTkEntry(mainframe, placeholder_text="Descripción")
    entryDescripcion.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

    labelFecha = ctk.CTkLabel(mainframe, text="Fecha")
    labelFecha.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryFecha = ctk.CTkEntry(mainframe, placeholder_text="Fecha")
    entryFecha.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelPrecio = ctk.CTkLabel(mainframe, text="Precio")
    labelPrecio.grid(row=2, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryPrecio = ctk.CTkEntry(mainframe, placeholder_text="Precio")
    entryPrecio.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

    labelKilometros = ctk.CTkLabel(mainframe, text="Kilómetros")
    labelKilometros.grid(row=3, column=0, padx=(PADIZQ, 50), pady=(15, 5))

    entryKilometros = ctk.CTkEntry(mainframe, placeholder_text="Kilómetros")
    entryKilometros.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))



    btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarReparacion)
    btnInsertar.grid(row=5, column=0, pady=10)

    btnEliminar = ctk.CTkButton(mainframe, text="Eliminar Cliente")
    btnEliminar.grid(row=5, column=1, pady=10)

    mostrarDatosReparaciones(id_seleccionadoMoto)

        
        
