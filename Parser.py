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
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] #PUNTERO
        if caracter_actual in P[no_terminal]:
            lado_derecho= P[no_terminal][caracter_actual]
            procesar(lado_derecho)
        else:
            datos_locales['error']=True          

    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0] #PUNTERO
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1   #AVANZA PUNTERO                     
                else:
                    datos_locales['error'] = True #ERROR ESTA EN TRUE
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



#Cadenas que el lenguaje  debe aceptar:
w1= "mostrar x + 5"
w2= "func hello(x) hello equal 1234; mostrar hello finfunc"
w3= ""
w4= ""
w5= ""
w6= ""

#Cadenas que el lenguaje no debe aceptar:
w7= "si x > 5 entonces si"
w8= ""
w9= ""
w10= ""

print("w1")
print(parser(lexer(w1)))
print("w2")
print(parser(lexer(w2)))
print("w3")
print(parser(lexer(w3)))
print("w4")
print(parser(lexer(w4)))
print("w5")
print(parser(lexer(w5)))
print("w6")
print(parser(lexer(w6)))
print("w7")
print(parser(lexer(w7)))
print("w8")
print(parser(lexer(w8)))
print("w9")
print(parser(lexer(w9)))
print("w10")
print(parser(lexer(w10)))



