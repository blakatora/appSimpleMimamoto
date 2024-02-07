import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

VentanaReparacion = ctk.CTk()
VentanaReparacion.geometry("1200x800")

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

VentanaReparacion.title("Reparaciones Mimamoto")

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



btnInsertar = ctk.CTkButton(mainframe, text="Insertar", )
btnInsertar.grid(row=5, column=0, pady=10)

btnEliminar = ctk.CTkButton(mainframe, text="Eliminar Cliente")
btnEliminar.grid(row=5, column=1, pady=10)

VentanaReparacion.mainloop()