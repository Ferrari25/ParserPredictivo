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
           
    def pni(no_terminal):
        datos_locales['error']=False
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] 
        if caracter_actual in P[no_terminal]:
            lado_derecho= P[no_terminal][caracter_actual]
            procesar(lado_derecho)
        else:
            datos_locales['error']=True          

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] 
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True 
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



w1= "si x<10 entonces mostrar x finsi"

print("w1")
print(parser(lexer(w1)))




