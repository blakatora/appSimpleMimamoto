import customtkinter as ctk
from tkinter import ttk
import FuncionesConexion
from tkinter import messagebox
import tkinter as tk
import reparacion

def vaciar_entry(entry):
    entry.delete(0, 'end')
    
def verMotos():
    anadirmoto_dobleClick(None)

# ventana moto  
def anadirmoto_dobleClick(event):


    
    
    def eliminarMoto():
        motoSeleccionada = treeviewMoto.selection() #trae el elemento que tenemos clicado en la lista_registri
        if motoSeleccionada:
            '''
            siempre que tengamos un elemento seleccionado,obtenemos el valor de la primera columna del elemento seleccionado de la lista. 
            Este valor es el ID del registro que se va a eliminar.
                    '''
            global id_seleccionadoMoto
            id_seleccionadoMoto = treeviewMoto.item(motoSeleccionada, "values")[0]
            
            print(id_seleccionadoMoto)
            FuncionesConexion.eliminarMoto(id_seleccionadoMoto)
            mostrarDatosMotosDeCLientes()
            
    
    def insertarReparacion():
        
        motoSeleccionada = treeviewMoto.selection() #trae el elemento que tenemos clicado en la lista_registri
        if motoSeleccionada:
            '''
            siempre que tengamos un elemento seleccionado,obtenemos el valor de la primera columna del elemento seleccionado de la lista. 
            Este valor es el ID del registro que se va a eliminar.
                    '''
            
            id_seleccionadoMotoParaVerReparacion = treeviewMoto.item(motoSeleccionada, "values")[0]
        
            
            reparacion.creaVentanaReparacion(ventanaMoto,id_seleccionadoMotoParaVerReparacion)
 
    def insertarMoto():
        marca=entryMarca.get()
        modelo=entryModelo.get()
        año=entryAño.get()
        matricula=entryMatricula.get()
        propietario=idClienteSeleccionadoTreeviewMoto
        
        FuncionesConexion.insertarMoto(marca,modelo,año,matricula,propietario)
        listaEntrys= [entryMarca,entryModelo,entryAño,entryMatricula]
        for i in listaEntrys:
            vaciar_entry(i)
            
        mostrarDatosMotosDeCLientes()
        

    def mostrarDatosMotosDeCLientes():
        
        # coger id de moto y guardarlo en una global para enviarlo a la ventana reparacion
        

        treeviewMoto.delete(*treeviewMoto.get_children())        

        treeviewMoto.config(
            columns=("ID","MARCA", "MODELO", "AÑO", "MATRICULA","PROPIETARIO")
        )
        treeviewMoto.grid(row=6, column=0, rowspan=6, columnspan=7, sticky="w",padx=(10,0))


        treeviewMoto.heading("ID", text="ID")
        treeviewMoto.heading("MARCA", text="MARCA")
        treeviewMoto.heading("MODELO", text="MODELO")
        treeviewMoto.heading("AÑO", text="AÑO")
        treeviewMoto.heading("MATRICULA", text="MATRICULA")
        treeviewMoto.heading("PROPIETARIO", text="PROPIETARIO")

        # Ajustar anchos de columna después de la creación del Treeview
        treeviewMoto.column("ID", width=60)
        treeviewMoto.column("MARCA", width=100)
        treeviewMoto.column("MODELO", width=200)
        treeviewMoto.column("AÑO", width=200)
        treeviewMoto.column("MATRICULA", width=200)
        treeviewMoto.column("PROPIETARIO", width=400)


        for resultado in FuncionesConexion.ObtenerTodasLasMotos(idClienteSeleccionadoTreeviewMoto):
                treeviewMoto.insert("", "end", values=resultado)
    
   
    
    selected_item = treeview.selection()
    
    if selected_item:

        # Obtener datos del elemento seleccionado
        item_id = selected_item[0]
     
        # selecciona el valor de la primera columna del registro seleccionado
        global idClienteSeleccionadoTreeviewMoto
        idClienteSeleccionadoTreeviewMoto = treeview.item(item_id, 'values')[0]
        
        # obtener las motos de cada cliente
        # print(FuncionesConexion.ObtenerTodasLasMotos(idClienteSeleccionadoTreeviewMoto))

        # busca cliente por id        
        # print(FuncionesConexion.buscarClientePorId(idClienteSeleccionadoTreeviewMoto))
        
        ventanaMoto = ctk.CTkToplevel(appClientes)
        ventanaMoto.geometry("1200x800")


        ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # me devuelve una tupla y tengo que quedarme con el primer valor
        nombreClienteSeleccionado=FuncionesConexion.buscarClientePorId(idClienteSeleccionadoTreeviewMoto)[0]

        ventanaMoto.title(f'Moto/s de {nombreClienteSeleccionado}')
        
        # imprimir nombre de cliente
        # print(f'Moto/s de {nombreClienteSeleccionado}')
       
            
        # poner ventana delante de todo
        # ventanaMoto.attributes("-topmost", True)

        PADIZQ, PADYDRC = 400, 200
        
        labelCliente=ctk.CTkLabel(ventanaMoto, text=f"Moto de {nombreClienteSeleccionado} ", font=("Arial", 20))
        labelCliente.grid(row=0, column=0, columnspan=2, padx=(PADIZQ, 200), pady=(30, 5))

        
        labelMarca = ctk.CTkLabel(ventanaMoto, text="MARCA")
        labelMarca.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(40, 5))

        entryMarca = ctk.CTkEntry(ventanaMoto, placeholder_text="MARCA")
        entryMarca.grid(row=1, column=1, pady=(40, 5), padx=(0, PADYDRC))

        labelModelo = ctk.CTkLabel(ventanaMoto, text="Modelo")
        labelModelo.grid(row=2, column=0, padx=(PADIZQ, 50), pady=(15, 5))

        entryModelo = ctk.CTkEntry(ventanaMoto, placeholder_text="Modelo")
        entryModelo.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

        labelAño = ctk.CTkLabel(ventanaMoto, text="Año")
        labelAño.grid(row=3, column=0, pady=(15, 5), padx=(PADIZQ, 50))

        entryAño= ctk.CTkEntry(ventanaMoto, placeholder_text="Año")
        entryAño.grid(row=3, column=1, pady=(15, 5), padx=(0, PADYDRC))

        labelMatricula = ctk.CTkLabel(ventanaMoto, text="Matricula")
        labelMatricula.grid(row=4, column=0, pady=(15, 5), padx=(PADIZQ, 50))

        entryMatricula = ctk.CTkEntry(ventanaMoto, placeholder_text="Matricula")
        entryMatricula.grid(row=4, column=1, pady=(15, 5), padx=(0, 200))    

        # labelDireccion = ctk.CTkLabel(mainframe, text="Dirección")
        # labelDireccion.grid(row=4, column=0, pady=(15, 5), padx=(PADIZQ, 50))

        # entryDireccion = ctk.CTkEntry(mainframe, placeholder_text="Dirección")
        # entryDireccion.grid(row=4, column=1, pady=(15, 5), padx=(0, PADYDRC))
       
        global treeviewMoto
        treeviewMoto = ttk.Treeview(ventanaMoto, show="headings", selectmode="browse")
        
        mostrarDatosMotosDeCLientes()
        btnInsertar = ctk.CTkButton(ventanaMoto, text="Insertar", command=insertarMoto)
        btnInsertar.grid(row=5, column=0, pady=10)
        
        btnBorrar = ctk.CTkButton(ventanaMoto, text="Eliminar Moto", command=eliminarMoto)
        btnBorrar.grid(row=5, column=1, pady=10)
        
        btnInsertarReparacion = ctk.CTkButton(ventanaMoto, text="Reparación", command=insertarReparacion)
        btnInsertarReparacion.grid(row=16, column=0, pady=10)

        # evento de doble click para abrir la ventana de reparacion de la moto
        def dobleclickReparacion(event):
            motoseleccionada = treeviewMoto.selection()
            if motoseleccionada:
                insertarReparacion()

        treeviewMoto.bind('<Double-1>', dobleclickReparacion)

                
     
        

    
def buscarPorMatricula():

    matricula=entryMatriculaBusqueda.get()
    if(matricula !='' ):
        try:
            idMoto=FuncionesConexion.encontrarIdMotoPorMatricula(matricula)[0]
            print("el tipo de dato es", type(idMoto))
            reparacion.creaVentanaReparacion(appClientes,idMoto)  

        except Exception as e:
            mensaje = "Se ha producido un error. Detalles: " + str(e)
            messagebox.showerror(message=mensaje, title="Error de busqueda")




def insertarDatos():
    dni = entryDNI.get()
    nombre = entryNombre.get()
    email = entryEmail.get()
    telefono = entryTelefono.get()
    
def eliminarCliente():
    
    selected_item = treeview.selection()
    
    if selected_item:

        # Obtener datos del elemento seleccionado
        item_id = selected_item[0]
     
        # selecciona el valor de la primera columna del registro seleccionado
        global idClienteSeleccionadoTreeviewCliente
        idClienteSeleccionadoTreeviewCliente = treeview.item(item_id, 'values')[0]

        # me devuelve una tupla y tengo que quedarme con el primer valor
        nombreClienteSeleccionado=FuncionesConexion.buscarClientePorId(idClienteSeleccionadoTreeviewCliente)[0]

    print(f"cliente a eliminat {nombreClienteSeleccionado}")    
    FuncionesConexion.eliminarCliente(idClienteSeleccionadoTreeviewCliente)
    mostrarDatosClientesEnTabla()
    
    
def mostrarDatosClientesEnTabla():
    treeview.delete(*treeview.get_children())        

    treeview.config(
        columns=("ID","DNI", "Nombre Completo", "Correo", "Teléfono Cliente","Direccion")
    )
    treeview.grid(row=9, column=0, rowspan=6, columnspan=7, sticky="w",padx=(20,100))

    treeview.heading("ID", text="ID")
    treeview.heading("DNI", text="DNI")
    treeview.heading("Nombre Completo", text="Nombre Completo")
    treeview.heading("Correo", text="Correo")
    treeview.heading("Teléfono Cliente", text="Teléfono Cliente")
    treeview.heading("Direccion", text="Direccion")

    # Ajustar anchos de columna después de la creación del Treeview
    treeview.column("ID", width=60)
    treeview.column("DNI", width=100)
    treeview.column("Nombre Completo", width=200)
    treeview.column("Correo", width=200)
    treeview.column("Teléfono Cliente", width=200)
    treeview.column("Direccion", width=400)


    for resultado in FuncionesConexion.ObtenerTodosLosClientes():
            treeview.insert("", "end", values=resultado)
   
def buscarDatosTabla():
    
    dni = entryDNI.get()
    nombre_completo = entryNombre.get()
    correo = entryEmail.get()
    telefono = entryTelefono.get()
    direccion = entryDireccion.get()
   

    query = "SELECT id,dni,nombre_completo,correo,telefono,direccion FROM cliente WHERE 1=1"
    
    if dni:
        query += f" AND dni = '{dni}'"
    if nombre_completo:
        query += f" AND nombre_completo ILIKE '%{nombre_completo}%'"
    if correo:
        query += f" AND correo ILIKE '%{correo}%'"
    if telefono:
        query += f" AND telefono = '{telefono}'"
    if direccion:
        query += f" AND direccion ILIKE '%{direccion}%'"     
    
    treeview.delete(*treeview.get_children())        
    for resultado in FuncionesConexion.EjecutarConsulta(query):
        treeview.insert("", "end", values=resultado)
    
    
def insertarDatos():
        nombreCompleto = entryNombre.get()
        email = entryEmail.get()
        telefono = entryTelefono.get()
        direccion = entryDireccion.get()
        dni = entryDNI.get()
        FuncionesConexion.insertarCliente(nombreCompleto, email, telefono, direccion,dni)
        mostrarDatosClientesEnTabla()
        
        vaciar_entry(entryNombre)
        vaciar_entry(entryDireccion)
        vaciar_entry(entryEmail)

        vaciar_entry(entryDNI)
        vaciar_entry(entryTelefono)

        

        
def hacer_ventana_completa(ventana):
    # Obtenemos las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Establecemos las dimensiones de la ventana
    ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

def ventanaAlMedio(root):
    ancho_ventana = 1200
    alto_ventana = 800

    x = (root.winfo_screenwidth() - ancho_ventana) // 2
    y = (root.winfo_screenheight() - alto_ventana) // 2

    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")



ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

appClientes = ctk.CTk()  # create CTk window like you do with the Tk window

# hacer_ventana_completa(appClientes)

appClientes.geometry('1200x800')
appClientes.title("Clientes Mimamoto")


# Establecer el ícono de la ventana
# appClientes.attributes("-topmost", True)
ventanaAlMedio(appClientes)

FuncionesConexion.icono(appClientes)

mainframe = ctk.CTkFrame(master=appClientes, width=100, height=480)
mainframe.pack(fill=ctk.BOTH, expand=True)

global treeview
treeview = ttk.Treeview(mainframe, show="headings", selectmode="browse")

PADIZQ, PADYDRC = 400, 200

labelDNI = ctk.CTkLabel(mainframe, text="DNI")
labelDNI.grid(row=0, column=0, padx=(PADIZQ, 50), pady=(40, 5))

entryDNI = ctk.CTkEntry(mainframe, placeholder_text="DNI")
entryDNI.grid(row=0, column=1, pady=(40, 5), padx=(0, PADYDRC))

labelNombre = ctk.CTkLabel(mainframe, text="Nombre Completo")
labelNombre.grid(row=1, column=0, padx=(PADIZQ, 50), pady=(15, 5))

entryNombre = ctk.CTkEntry(mainframe, placeholder_text="Nombre Completo")
entryNombre.grid(row=1, column=1, pady=(15, 5), padx=(0, PADYDRC))





labelEmail = ctk.CTkLabel(mainframe, text="Email")
labelEmail.grid(row=2, column=0, pady=(15, 5), padx=(PADIZQ, 50))

entryEmail = ctk.CTkEntry(mainframe, placeholder_text="Email")
entryEmail.grid(row=2, column=1, pady=(15, 5), padx=(0, PADYDRC))

labelTelefono = ctk.CTkLabel(mainframe, text="Telefono")
labelTelefono.grid(row=3, column=0, pady=(15, 5), padx=(PADIZQ, 50))

entryTelefono = ctk.CTkEntry(mainframe, placeholder_text="Telefono")
entryTelefono.grid(row=3, column=1, pady=(15, 5), padx=(0, 200))    

labelDireccion = ctk.CTkLabel(mainframe, text="Dirección")
labelDireccion.grid(row=4, column=0, pady=(15, 5), padx=(PADIZQ, 50))

entryDireccion = ctk.CTkEntry(mainframe, placeholder_text="Dirección")
entryDireccion.grid(row=4, column=1, pady=(15, 5), padx=(0, PADYDRC))





botonesFrame = ctk.CTkFrame(master=appClientes, width=700, height=480)
botonesFrame.pack(fill=ctk.BOTH, expand=True)

btnInsertar = ctk.CTkButton(mainframe, text="Insertar", command=insertarDatos)
btnInsertar.grid(row=5, column=0, pady=10)

btnBuscar = ctk.CTkButton(mainframe, text="Buscar", command=buscarDatosTabla)
btnBuscar.grid(row=5, column=1, pady=10)

btnEliminar = ctk.CTkButton(mainframe, text="Eliminar Cliente", command=eliminarCliente)
btnEliminar.grid(row=6, column=1, pady=10)

btnVerMotos = ctk.CTkButton(mainframe, text="Ver motos", command=verMotos)
btnVerMotos.grid(row=17, column=0, pady=10)

btnLimpiarBusqueda = ctk.CTkButton(mainframe, text="Limpiar Busqueda", command=mostrarDatosClientesEnTabla)
btnLimpiarBusqueda.grid(row=17, column=1, pady=10)

btnLimpiarBusqueda = ctk.CTkButton(mainframe, text="prueba", command=mostrarDatosClientesEnTabla)
btnLimpiarBusqueda.grid(row=18, column=1, pady=10)





entryMatriculaBusqueda = ctk.CTkEntry(mainframe, placeholder_text="Matrícula")
entryMatriculaBusqueda.grid(row=19, column=0, pady=(15, 5), padx=(PADIZQ, 50))

# # Agregar botón de búsqueda por matrícula
btnBuscarMatricula = ctk.CTkButton(mainframe, text=" Buscar por Matrícula ", command=buscarPorMatricula,fg_color="#808080",width=90)
btnBuscarMatricula.grid(row=19, column=1, pady=10 ,padx=(0, PADYDRC))


# ... (código posterior)

mostrarDatosClientesEnTabla()
treeview.bind('<Double-1>', anadirmoto_dobleClick)


appClientes.mainloop()
