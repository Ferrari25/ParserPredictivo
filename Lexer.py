from Automatas import *

#Lexer
def lexer(codigo_fuente): 
    tokens = [] 
    posicion_actual = 0 
    
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace(): 
            posicion_actual = posicion_actual + 1 

        comienzo_lexema = posicion_actual 
        posibles_tokens = [] 
        posibles_tokens_con_un_caracter_mas = [] 
        lexema = "" 
        var_aux_todos_en_estado_trampa = False 
        
        #
        while not var_aux_todos_en_estado_trampa and posicion_actual < len (codigo_fuente)+1: 
            var_aux_todos_en_estado_trampa = True 
            lexema = codigo_fuente[comienzo_lexema:posicion_actual+1] 
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES: 
                simulacion_afd = afd(lexema) 
                if simulacion_afd == ESTADO_FINAL: 
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token) 
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False
            
            #aumenta la posicion actual en 1 
            posicion_actual = posicion_actual + 1
        
        if len(posibles_tokens) == 0:
            print("ERROR: TOKEN DESCONOCIDO - LEXER FALLO" + lexema)
        else:
            posicion_actual = posicion_actual - 1                                       
            un_tipo_de_token = posibles_tokens[0]                                       
            token= (un_tipo_de_token,codigo_fuente[comienzo_lexema:posicion_actual])    
            tokens.append(token)                                                        
        
    return tokens 


TOKENS_POSIBLES = [("SI", automata_si),
                   ("FINSI", automata_finsi),
                   ("SINO", automata_sino),
                   ("OPSUMA", automata_opsuma),
                   ("OPMULT", automata_opmult),
                   ("EQUAL", automata_equal),
                   ("LEER", automata_leer),
                   ("MOSTRAR", automata_mostrar),
                   ("REPETIR", automata_repetir),
                   ("HASTA", automata_hasta),
                   ("ENTONCES", automata_entonces),
                   ("MIENTRAS", automata_mientras),
                   ("FUNC", automata_func),
                   ("FINFUNC", automata_finfunc),
                   ("OPREL", automata_oprel),
                   ("PUNTO-COMA",automataPuntoComa),
                   ("Parentesis Cerrado",automataParenClose),
                   ("Parentesis Abierto",automataParenOpen),
                   ("NUM",automata_num),
                   ("ID", automata_id)]

#codigo_fuente1 = "x equal 98234; si 6 < 7 entonces x equal x / 4 sino x equal x / 3 finsi"
#print(lexer(codigo_fuente1))