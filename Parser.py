from Lexer import * 
from Gramatica_v2 import *
from Automatas import * 



def parser(codigo_fuente):
    codigo_fuente.append(("#", "#"))
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
        'derivaciones': []  
    }

    def pni(no_terminal):
        datos_locales['error'] = False
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        lado_derecho = P[no_terminal][caracter_actual]
        if caracter_actual in P[no_terminal]:
            procesar(no_terminal, lado_derecho)
        else:
            datos_locales['error'] = True

    def procesar(no_terminal, cuerpo_produccion):
        derivacion_actual = []
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            derivacion_actual.append(simbolo)
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1
                else:
                    datos_locales['error'] = True
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
        datos_locales['derivaciones'].append((no_terminal, derivacion_actual))

    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != '#' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print("")
        print('La cadena pertenece al lenguaje')
        return True

    principal()
    return datos_locales['derivaciones'][::-1]


cadenas = ["id equal 3","mostrar x + 5"]
for cadena in cadenas: 
    derivaciones = parser(lexer(cadena))
    print(f"\nDerivaciones para '{cadena}':")
    for no_terminal, derivacion_actual in derivaciones:
        print(f"{no_terminal} --> {' '.join(derivacion_actual)}")
