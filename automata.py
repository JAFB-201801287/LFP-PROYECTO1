import re

import lectorArchivos

from models import Elemento, Menu, Seccion, Restaurante, RestauranteController
from texttable import Texttable

NOMBRE_RESTAURANTE = 'NOMBRE_RESTAURANTE'
NOMBRE_SECCION = 'NOMBRE_SECCION'
NOMBRE_MENU = 'NOMBRE_MENU'
PALABRA_RESERVADA = 'PALABRA_RESERVADA'
COMILLA = 'COMILLA_SIMPLE'
PUNTO_COMA = 'PUNTO_COMA'
IGUAL = 'IGUAL  '
CADENA_VACIA = 'CADENA_VACIA'
IDENTIFICADOR = 'IDENTIFICADOR'
DESCRIPCION = 'DESCRIPCION'
PRECIO = 'PRECIO'

ERROR = 'ERROR'

PATRON_CADENA_VACIA = r'\s+'
PATRON_NOMBRE_RESTAURANTE = r'\s*(?P<error1>.*)\s*(?P<restaurante>[R|r][E|e][S|s][T|t][A|a][U|u][R|r][A|a][N|n][T|t][E|e])\s*(?P<error2>.*)\s*(?P<igual>=)\s*(?P<error3>[^\']*)\s*(?P<comilla1>\')(?P<nombre_restaurante>.+)(?P<comilla2>\')\s*(?P<error4>[^\']*)\s*'
PATRON_SECCION = r'\s*(?P<error1>.*)\s*(?P<comilla1>\')(?P<seccion>.+)(?P<comilla2>\')\s*(?P<error2>.*)\s*(?P<dos_puntos>:)\s*(?P<error3>.*)\s*'
PATRON_MENU = r'\s*(?P<error1>[^\[]*)\s*(?P<inicio_corchete>\[)(?P<identificador>[^;]+)(?P<punto_coma1>;)\s*(?P<error2>[^\']*)\s*(?P<comilla1>\')(?P<nombre>[^\']+)(?P<comilla2>\')\s*(?P<error3>[^;]*)\s*(?P<punto_coma2>;)\s*(?P<precio>[^;]+)\s*(?P<punto_coma3>;)\s*(?P<error4>[^\']*)\s*(?P<comilla3>\')(?P<descripcion>[^\']*)(?P<comilla4>\')\s*(?P<error5>[^\]]*)\s*]\s*(?P<error6>.*)\s*'

def automata():
    fila = 0
    info = lectorArchivos.leerArchivo()
    dic = {}
    restaurante = Restaurante()
    seccion = None
    for i in info:
        fila += 1
        if(re.match(PATRON_CADENA_VACIA, i) != None):
            vacio = Elemento()
            vacio.setElemento('')
            vacio.setInicio(0)
            vacio.setFin(0)
            vacio.setTipo(CADENA_VACIA)
            vacio.setLinea(fila)
            restaurante.setToken(vacio)
        elif(re.match(PATRON_NOMBRE_RESTAURANTE, i)!= None):
            match = re.match(PATRON_NOMBRE_RESTAURANTE, i)

            token_restaurante = Elemento()
            token_restaurante.setElemento(match.group('restaurante').strip())
            token_restaurante.setInicio(match.start('restaurante'))
            token_restaurante.setFin(match.end('restaurante'))
            token_restaurante.setTipo(PALABRA_RESERVADA)
            token_restaurante.setLinea(fila)
            restaurante.setToken(token_restaurante)

            token_igual = Elemento()
            token_igual.setElemento(match.group('igual').strip())
            token_igual.setInicio(match.start('igual'))
            token_igual.setFin(match.end('igual'))
            token_igual.setTipo(IGUAL)
            token_igual.setLinea(fila)
            restaurante.setToken(token_igual)

            for i in range(1,3):
                token_comilla = Elemento()
                token_comilla.setElemento(match.group('comilla' + str(i).strip()))
                token_comilla.setInicio(match.start('comilla' + str(i)))
                token_comilla.setFin(match.end('comilla' + str(i)))
                token_comilla.setTipo(COMILLA)
                token_comilla.setLinea(fila)
                restaurante.setToken(token_comilla)

            nombre = Elemento()
            nombre.setElemento(match.group('nombre_restaurante').strip())
            nombre.setInicio(match.start('nombre_restaurante'))
            nombre.setFin(match.end('nombre_restaurante'))
            nombre.setTipo(NOMBRE_RESTAURANTE)
            nombre.setLinea(fila)
            restaurante.setToken(nombre)

            for i in range(1,5):
                if(match.group('error' + str(i)) != ''):
                    error = Elemento()
                    error.setElemento(match.group('error' + str(i)).strip())
                    error.setInicio(match.start('error' + str(i)))
                    error.setFin(match.end('error' + str(i)))
                    error.setTipo(ERROR)
                    error.setLinea(fila)
                    restaurante.setError(error)

            restaurante.setNombre(match.group('nombre_restaurante').strip())

        elif(re.match(PATRON_SECCION, i)!= None):
            match = re.match(PATRON_SECCION, i)

            if(seccion != None):
                restaurante.setSeccion(seccion)

            seccion = Seccion()

            for i in range(1,3):
                token_comilla = Elemento()
                token_comilla.setElemento(match.group('comilla' + str(i).strip()))
                token_comilla.setInicio(match.start('comilla' + str(i)))
                token_comilla.setFin(match.end('comilla' + str(i)))
                token_comilla.setTipo(COMILLA)
                token_comilla.setLinea(fila)
                restaurante.setToken(token_comilla)

            nombre = Elemento()
            nombre.setElemento(match.group('seccion').strip())
            nombre.setInicio(match.start('seccion'))
            nombre.setFin(match.end('seccion'))
            nombre.setTipo(NOMBRE_SECCION)
            nombre.setLinea(fila)
            restaurante.setToken(nombre)

            for i in range(1,4):
                if(match.group('error' + str(i)) != ''):
                    error = Elemento()
                    error.setElemento(match.group('error' + str(i).strip()))
                    error.setInicio(match.start('error' + str(i)))
                    error.setFin(match.end('error' + str(i)))
                    error.setTipo(ERROR)
                    error.setLinea(fila)
                    restaurante.setError(error)

            seccion.setNombre(match.group('seccion').strip())
        elif(re.match(PATRON_MENU, i)!= None):
            match = re.match(PATRON_MENU, i)
            menu = Menu()

            for i in range(1,3):
                token_punto_coma = Elemento()
                token_punto_coma.setElemento(match.group('punto_coma' + str(i)).strip())
                token_punto_coma.setInicio(match.start('punto_coma' + str(i)))
                token_punto_coma.setFin(match.end('punto_coma' + str(i)))
                token_punto_coma.setTipo(PUNTO_COMA)
                token_punto_coma.setLinea(fila)
                restaurante.setToken(token_punto_coma)

            identificador = Elemento()
            identificador.setElemento(match.group('identificador').strip())
            identificador.setInicio(match.start('identificador'))
            identificador.setFin(match.end('identificador'))
            identificador.setTipo(IDENTIFICADOR)
            identificador.setLinea(fila)
            restaurante.setToken(identificador)

            for i in range(1,5):
                token_comilla = Elemento()
                token_comilla.setElemento(match.group('comilla' + str(i)).strip())
                token_comilla.setInicio(match.start('comilla' + str(i)))
                token_comilla.setFin(match.end('comilla' + str(i)))
                token_comilla.setTipo(COMILLA)
                token_comilla.setLinea(fila)
                restaurante.setToken(token_comilla)
            
            nombre = Elemento()
            nombre.setElemento(match.group('nombre').strip())
            nombre.setInicio(match.start('nombre'))
            nombre.setFin(match.end('nombre'))
            nombre.setTipo(NOMBRE_MENU)
            nombre.setLinea(fila)
            restaurante.setToken(nombre)

            precio = Elemento()
            precio.setElemento(match.group('precio').strip())
            precio.setInicio(match.start('precio'))
            precio.setFin(match.end('precio'))
            precio.setTipo(PRECIO)
            precio.setLinea(fila)
            restaurante.setToken(precio)

            descripcion = Elemento()
            descripcion.setElemento(match.group('descripcion').strip())
            descripcion.setInicio(match.start('descripcion'))
            descripcion.setFin(match.end('descripcion'))
            descripcion.setTipo(DESCRIPCION)
            descripcion.setLinea(fila)
            restaurante.setToken(descripcion)

            for i in range(1,7):
                if(match.group('error' + str(i)) != ''):
                    error = Elemento()
                    error.setElemento(match.group('error' + str(i)).strip())
                    error.setInicio(match.start('error' + str(i)))
                    error.setFin(match.end('error' + str(i)))
                    error.setTipo(ERROR)
                    error.setLinea(fila)
                    restaurante.setError(error)

        else:
            print(i)
    RestauranteController().add(restaurante)

    

automata()

print('\n\n')
tabla_tokens =  [['FILA', 'COLUMNA INICIO', 'COLUMNA FINAL', 'LEXEMA  ', 'TOKEN              ']]
tabla_errores = [['FILA', 'COLUMNA INICIO', 'COLUMNA FINAL', 'CARACTER', 'DESCRIPCION        ']]
for a in RestauranteController().get():
    print(a.getNombre())
    for o in a.getTokens():
        tabla_tokens.append([o.getLinea(), o.getInicio(), o.getFin(), o.getElemento(), o.getTipo()])

    for o in a.getErrores():
        tabla_errores.append([o.getLinea(), o.getInicio(), o.getFin(), o.getElemento(), o.getTipo()])

print('\n\TOKENS')
table1 = Texttable()
table1.set_cols_width([4, 14, 14, 60, 30])
table1.set_cols_align(['FILA', 'COLUMNA INICIO', 'COLUMNA FINAL', 'LEXEMA', 'TOKEN'])
table1.add_rows(tabla_tokens)
print(table1.draw())

print('\n\nERRORES')
table2 = Texttable()
table2.set_cols_width([4, 14, 14, 60, 30])
table2.set_cols_align(['FILA', 'COLUMNA INICIO', 'COLUMNA FINAL', 'CARACTER', 'DESCRIPCION'])
table2.set_cols_valign(['FILA', 'COLUMNA INICIO', 'COLUMNA FINAL', 'CARACTER', 'DESCRIPCION']) 
table2.add_rows(tabla_errores)
print(table2.draw())