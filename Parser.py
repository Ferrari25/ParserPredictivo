from Gramatica import *           
from Lexer import * 
from Automatas import * 



def parser(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
    #INTENTO DE PNI GENERAL PREDICTIVO        
    def pni(no_terminal):
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual in SD[no_terminal].keys():
            lado_derecho= SD[no_terminal][caracter_actual]
            for lado_derecho in SD[no_terminal]:
                procesar(lado_derecho)
    
    
    ############## NOTAS PNI GENERICO ####################
    """
    LADO_DERECHO
    lado_derecho guarda las producciones que se puede usar dado un no-terminal
    ej: si el no-Terminal es 'ListaSentencias' y el caracter actual (lo q se esta aputando) es "ID"
    entonce lado_derecho almacenara la produccion "['Sentencia' ,'ListaSentencia2']"
    ya que la definición de la gramática indica que 'ListaSentencias' puede derivar en 'Sentencia' ,'ListaSentencia2' cuando el símbolo actual es "ID".
    
    
    CARACTER_ACTUAL
    caracter_actual en tu código se refiere al símbolo actual que se está analizando en la lista de tokens.
    Este símbolo se extrae de la lista de tokens en función del valor del índice actual 
    
    SD[NO_TERMINAL].KEYS()
    es una lista de los simbolos directrices para el no terminal que se esta recorriendo 
    
    
    """
    ##########################################
                    

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()


### PRUEBA PASER CON LEXER ###

""" 
PARSER
ejemplo de derivacion: 
SI ID EQUAL NUM PUNTO-COMA LEER ID PUNTO-COMA FUNC ID Parentensis Abierto ID PUNTO-COMA Parentensis Cerrado SI NUM OPEREL NUM ENTONCES ID PUNTO-COMA SINO ID PUNTO-COMA FIN-SI REPETIR ID EQUAL NUM PUNTO-COMA LEER ID PUNTO-COMA MOSTRAR ID PUNTO-COMA HASTA NUM PUNTO-COMA FINFUNC

cadena resultante: 
SI A = 8 ; LEER B ; FUNC C ( D ; ) SI 8 > 7 ENTONCES E ; SINO F ; FIN-SI REPETIR G = 9 ; LEER H ; MOSTRAR L ; HASTA 8 ; FIN-FUNC

##############################################
Lexer Devuelve ante esa cadena de arriba 
[
    ('ID', 'SI'),
    ('ID', 'A'),
    ('OPEREL', '='),
    ('NUM', '8'),
    ('PUNTO-COMA', ';'),
    ('ID', 'LEER'),
    ('ID', 'B'),
    ('PUNTO-COMA', ';'),
    ('ID', 'FUNC'),
    ('ID', 'C'),
    ('Parentensis Abierto',
    '('), ('ID', 'D'),
    ('PUNTO-COMA', ';'),
    ('Parentensis Cerrado', ')'),
    ('ID', 'SI'),
    ('NUM', '8'),
    ('OPEREL', '>'),
    ('NUM', '7'),
    ('ID', 'ENTONCES'),
    ('ID', 'E'),
    ('PUNTO-COMA', ';'),
    ('ID', 'SINO'),
    ('ID', 'F'),
    ('PUNTO-COMA', ';'),
    ('ID', 'FIN'),
    ('OPSUM', '-'),
    ('ID', 'SI'),
    ('ID', 'REPETIR'),
    ('ID', 'G'),
    ('OPEREL', '='),
    ('NUM', '9'),
    ('PUNTO-COMA', ';'),
    ('ID', 'LEER'),
    ('ID', 'H'),
    ('PUNTO-COMA', ';'),
    ('ID', 'MOSTRAR'),
    ('ID', 'L'),
    ('PUNTO-COMA', ';'),
    ('ID', 'HASTA'),
    ('NUM', '8'),
    ('PUNTO-COMA', ';'),
    ('ID', 'FIN'),
    ('OPSUM', '-'),
    ('ID', 'FUNC')
]


"""
codigo_fuente = "SI A = 8 ; LEER B ; FUNC C ( D ; ) SI 8 > 7 ENTONCES E ; SINO F ; FIN-SI REPETIR G = 9 ; LEER H ; MOSTRAR L ; HASTA 8 ; FIN-FUNC"
print(parser(lexer(codigo_fuente)))