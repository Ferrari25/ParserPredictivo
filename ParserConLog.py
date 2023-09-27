import logging
from Gramatica import *
from Lexer import *
from Automatas import *

# Configura el registro
logging.basicConfig(
    filename='LogParser.log',  # Nombre del archivo de registro
    level=logging.DEBUG,         # Nivel mínimo de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del registro con marca de tiempo y nivel
)
logging.info("####")
logging.info("####")
logging.info("####")
logging.info("####")
logging.info("####")
logging.info("####")
logging.info("######################################### COMIENZO DE EJECUCION #######################################################")

def parser(codigo_fuente):
    codigo_fuente.append(("#", "#"))
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }

    # Intento de PNI general predictivo
    def pni(no_terminal):
        logging.info("----FUNCION PNI")
        logging.debug("----NO TERMINAL EN PNI")
        logging.debug(no_terminal)
        
        datos_locales['error'] = False
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]  # PUNTERO
        if caracter_actual in dicSD[no_terminal]:
            logging.debug("----CARACTER ACTUAL")
            logging.debug(caracter_actual)
            logging.debug("el caracter actual ESTA en los SD del no terminal")
            lado_derecho = dicSD[no_terminal][caracter_actual]
            logging.debug(lado_derecho,"se mando a procesar")
            procesar(lado_derecho)
        else:
            logging.debug("el caracter actual  NO -- ESTA en los SD del no terminal")
            logging.debug(caracter_actual)
            datos_locales['error'] = True
            logging.error(f'Error en pni: No se encontro {caracter_actual} en {no_terminal}')

    def procesar(cuerpo_produccion):
        logging.info("----FUNCION PROCESAR")
        logging.debug("----CUERPO DE PRODUCCION EN PROCESAR")
        logging.debug(cuerpo_produccion)
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]  
            logging.debug(caracter_actual)
            datos_locales['error'] = False
            if simbolo in VT:
                logging.debug("---- SIMBOLO EN VT")
                logging.debug(simbolo)
                if simbolo == caracter_actual:
                    logging.debug("---- SIMBOLO == CARACTER ACTUAL")
                    logging.debug(caracter_actual)
                    datos_locales['index'] += 1  
                    logging.info("El puntero avanzo")
                else:
                    datos_locales['error'] = True
                    logging.error(f'Error en procesar: Se esperaba {simbolo}, se encontró {caracter_actual}')
                    break
            elif simbolo in VN:
                logging.debug("---- SIMBOLO EN VN")
                logging.debug(simbolo)
                logging.debug("mando simbolo a pni()")
                pni(simbolo)
                if datos_locales['error']:
                    break

    def principal():
        logging.info("----FUNCION PRINCIPAL")
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != '#' or datos_locales['error']:
            logging.error('La cadena no pertenece al lenguaje')
            logging.info("######################################### NO - PERTENECE #######################################################")
            return False
        logging.info('La cadena pertenece al lenguaje')
        logging.info("######################################### PERTENECE #######################################################")
        return True

    return principal()

codigo_fuente = "mostrar x + 5"
w = lexer(codigo_fuente)
print(w)
print(parser(w))