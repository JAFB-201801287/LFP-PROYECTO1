import easygui

#Lector de archivox
def leerArchivo():
    archivo = easygui.fileopenbox( default="./data/*.lfp")
    data = []
    with open(archivo, "r", encoding="utf-8") as f: 
        for line in f.readlines():
            data.append(line)
    return data

#-------------------------------------------------------------------------------------------------------------------------------------

class Elemento():

# Constructor ----------------------------------------

    def __init__(self):
        self.tipo = ''
        self.elemento = ''
        self.inicio = 0
        self.fin = 0
        self.linea = 0
    
    def __str__(self):
        return self.elemento

# Metodos GET ----------------------------------------

    def getTipo(self):
        return self.tipo

    def getElemento(self):
        return self.elemento

    def getInicio(self):
        return self.inicio

    def getFin(self):
        return self.fin

    def getLinea(self):
        return self.linea

# Metodos SET ----------------------------------------

    def setTipo(self, tipo):
        self.tipo = tipo

    def setElemento(self, elemento):
        self.elemento = elemento

    def setInicio(self, inicio):
        self.inicio = inicio

    def setFin(self, fin):
        self.fin = fin

    def setLinea(self, linea):
        self.linea = linea

#-------------------------------------------------------------------------------------------------------------------------------------

class Menu():

# Constructor ----------------------------------------

    def __init__(self):
        self.id = 0
        self.identificador = ''
        self.nombre = ''
        self.precio = 0.00
        self.descripcion = 0
    
    def __str__(self):
        return self.nombre

# Metodos GET ----------------------------------------

    def getId(self):
        return self.id

    def getIdentificador(self):
        return self.identificador

    def getNombre(self):
        return self.nombre

    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion

# Metodos SET ----------------------------------------

    def setId(self, id):
        self.id = id

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

#-------------------------------------------------------------------------------------------------------------------------------------

class Seccion():

# Constructor ----------------------------------------

    def __init__(self):
        self.id = 0
        self.nombre = ''
        self.menus = []
    
    def __str__(self):
        return self.nombre

# Metodos GET ----------------------------------------

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getMenus(self):
        return self.menus

# Metodos SET ----------------------------------------

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setMenus(self, menus):
        self.menus = menus

    def setMenu(self, menu):
        self.menus.append(menu)

#-------------------------------------------------------------------------------------------------------------------------------------

class Restaurante():

# Constructor ----------------------------------------

    def __init__(self):
        self.id = 0
        self.nombre = ''
        self.secciones = []
        self.errores = []
        self.tokens = []

    def __str__(self):
        return self.nombre

# Metodos GET ----------------------------------------

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getSecciones(self):
        return self.secciones

    def getErrores(self):
        return self.errores
    
    def getTokens(self):
        return self.tokens

# Metodos SET ----------------------------------------

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSecciones(self, secciones):
        self.secciones = secciones

    def setSeccion(self, seccion):
        self.secciones.append(seccion)

    def setErrores(self, errores):
        self.errores = errores

    def setError(self, error):
        self.errores.append(error)

    def setTokens(self, tokens):
        self.tokens = tokens

    def setToken(self, token):
        self.tokens.append(token)

#-------------------------------------------------------------------------------------------------------------------------------------

class RestauranteController():
    __instance = None
    index = 0
    restaurantes = []

# Constructor ----------------------------------------

    def __str__(self):
        return self.restaurantes

    def __new__(cls):
        if RestauranteController.__instance is None:
            RestauranteController.__instance = object.__new__(cls)
        return RestauranteController.__instance

    def __init__(self):
        self.id = 0

# Metodos ---------------------------------------------

    def get(self):
        return self.restaurantes

    def add(self, restaurante):
        self.index += 1
        restaurante.setId(self.index)
        self.restaurantes.append(restaurante)

    def clean(self):
        self.index = 0
        self.estaciones = []