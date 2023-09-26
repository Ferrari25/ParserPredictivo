from Gramatica import *           
from Lexer import * 
from Automatas import * 



def parser(codigo_fuente):
    codigo_fuente.append(("#","#"))
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
    
    
          
    #INTENTO DE PNI GENERAL PREDICTIVO        
    def pni(no_terminal):
        datos_locales['error']=False
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] #PUNTERO
        if caracter_actual in dicSD[no_terminal]:
            lado_derecho= dicSD[no_terminal][caracter_actual]
            procesar(lado_derecho)
        else:
            datos_locales['error']=True
            print(caracter_actual)
            print(no_terminal)
                    

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] #PUNTERO
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1   #AVANZA PUNTERO                     
                else:
                    datos_locales['error'] = True #ERROR ESTA EN TRUE
                    print(caracter_actual)
                    print(simbolo)
                    print(cuerpo_produccion)
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != '#' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()



codigo_fuente = "mostrar x+5" # FUNC C ( D ; ) SI 8 > 7 ENTONCES E ; SINO F ; FIN-SI REPETIR G = 9 ; LEER H ; MOSTRAR L ; HASTA 8 ; FIN-FUNC"
w = lexer(codigo_fuente)
print(w)
print(parser(w))