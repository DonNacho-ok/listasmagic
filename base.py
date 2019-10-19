from tkinter import *
from tkinter import ttk
from io import open
class App ():

    def __init__(self):
        self.root= Tk()
        self.root.title('Generador de listas')
        self.root.resizable(0,0)
        self.root.geometry('300x200')

        self.lista_carta=''

        self.etiq_bienve = ttk.Label(self.root, text='Bienvenido a la Generadora de Listas')
        self.etiq_opcion = ttk.Label(self.root, text='Elija la opcion a realizar')
        self.bott_crear = ttk.Button(self.root, text='Crear Lista', command=self.crear_lista)
        self.bott_generar = ttk.Button(self.root, text='Generar Lista', command=self.generar_lista)
        #agregar modificar lista

        self.etiq_bienve.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.etiq_opcion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.bott_crear.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.bott_generar.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.root.mainloop()

    def crear_lista(self):
        self.crear =Toplevel()
        self.crear.resizable(0,0)
        self.crear.title('Crear Lista')

        self.lista_cartas=[]
        self.nombre_carta=StringVar()
        self.cantidad_carta=IntVar(value=1)
        self.expansion_carta=StringVar()
        self.rareza_carta=StringVar()
        self.codigo_carta=StringVar()
        self.foil_carta=BooleanVar()
        self.promo_carta=BooleanVar()
        #necesito nombre(listo), cantidad(listo), expansion(listo), codigo de carta(listo), si es foil o no(listo), si es promo o no, rareza(listo)
        self.nombre= ttk.Label(self.crear, text='Nombre de la Carta', )
        self.nombre_entry= ttk.Entry(self.crear, textvariable=self.nombre_carta, width=10)
        self.cantidad= ttk.Label(self.crear, text='Cantidad de copias')
        self.cantidad_entry = ttk.Spinbox(self.crear, from_=1, to=100, wrap=True, textvariable=self.cantidad_carta, state='readonly')
        self.expansion= ttk.Label(self.crear, text='Expansion')
        self.expansion_entry= ttk.Entry(self.crear, textvariable=self.expansion_carta, width=5)
        self.codigo= ttk.Label(self.crear, text='Codigo de la Carta (XXX/XXX)')
        self.codigo_entry= ttk.Entry(self.crear, textvariable=self.codigo_carta, width=5)
        self.rareza= ttk.Label(self.crear, text='Rareza')
        #rarezas Mítica, raras(R), infrecuentes(u),comunes(C), tierra basica(l)
        self.rareza_radio1=ttk.Radiobutton(self.crear, text='Mítica(M)', variable=self.rareza_carta, value='m')
        self.rareza_radio2= ttk.Radiobutton(self.crear, text='Rara(R)', variable=self.rareza_carta, value='r')
        self.rareza_radio3= ttk.Radiobutton(self.crear, text='Infrecuente(U)', variable=self.rareza_carta, value='u')
        self.rareza_radio4= ttk.Radiobutton(self.crear, text='Comun(C)', variable=self.rareza_carta, value='c')
        self.rareza_radio5= ttk.Radiobutton(self.crear, text='Tierra Básica(L)', variable=self.rareza_carta, value='l')
        self.foil_check= ttk.Checkbutton(self.crear, text='Foil', variable=self.foil_carta, onvalue=True, offvalue=False)
        self.promo_check= ttk.Checkbutton(self.crear, text='Promo', variable=self.promo_carta, onvalue=True, offvalue=False)
        self.separador= ttk.Separator(self.crear, orient=HORIZONTAL)
        self.add= ttk.Button(self.crear, text='Añadir carta a lista', command=self.add_card)
        self.lista= ttk.Label(self.crear, textvariable=self.lista_cartas)

        self.nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.nombre_entry.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.cantidad.pack(side=TOP, fill=BOTH, expand=True, padx=100, pady=5)
        self.cantidad_entry.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.rareza.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.rareza_radio1.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.rareza_radio2.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.rareza_radio3.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.rareza_radio4.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.rareza_radio5.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.foil_check.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.promo_check.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.expansion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.expansion_entry.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.codigo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.codigo_entry.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
        self.separador.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.add.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.lista.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.crear.transient(master=self.root)
        self.crear.grab_set()
        self.root.wait_window(self.crear)


    def add_card(self):
        error_dato= False
        try:
            nombre=self.nombre_carta.get()
            cantidad=self.cantidad_carta.get()
            expansion=self.expansion_carta.get()
            rareza=self.rareza_carta.get()
            codigo=self.codigo_carta.get()
            foil=self.foil_carta.get()
            promo=self.promo_carta.get()
        except:
            error_dato=True
        if not error_dato:
            #detectar rarezas
            if rareza == 'm':
                cad_rareza='Mítica'
            elif rareza == 'r':
                cad_rareza='Rara'
            elif rareza == 'u':
                cad_rareza='Infrecuente'
            elif rareza == 'c':
                cad_rareza='Común'
            elif rareza == 'l':
                cad_rareza='Tierra Básica'
            #detectar foil
            if foil:
                cad_foil='Foil'
            else:
                cad_foil=','
            #detectar promo
            if promo:
                cad_promo='Promo'
            else:
                cad_promo=','
            #crear cadena
            cadena_carta=('{}, x{}, {}, {}, {}, {}, {}.\n'.format(nombre, cantidad, cad_rareza, cad_foil, cad_promo, expansion, codigo))
            #append lista
            self.lista_carta.add(cadena_carta)
            #resetear variables (probar despues)



    def generar_lista(self):
        self.generar = Toplevel()
        self.generar.resizable(0,0)
        self.generar.title('Generar lista')



        self.generar.transient(master=self.root)
        self.generar.grab_set()
        self.root.wait_window(self.generar)

def ejec ():
    ejec = App()
    return 0

ejec()
