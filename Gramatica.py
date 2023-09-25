VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                    'Termino','ListaSentencias2','ListaPar2','Expresion2','Termino2'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID"]
""""
P = {
    #'NOTERMINAL' : [{"produccion":['alfa1','alfa2',], "SD" :['beta1','beta2']}],
    'Program': [{"produccion": ['ListaSentencias'],"SD": ["a","b","c"],}], 
    
    'ListaSentencias' : [{"produccion" : ['Sentencia','ListaSentencias2'] , "SD" : ['SI','REPETIR','ID','LEER','MOSTRAR','FUNC']}],
    'ListaSentencias2' : [{"produccion":['PUNTO-COMA','Sentencias','ListaSentencias2'], "SD" :['PUNTO-COMA']}],
    'ListaSentencias2' : [{"produccion":[], "SD" :['#', 'FIN-FUNC',  'FIN-SI' ,'SINO' ,'HASTA']}],
    
    'Sentencia' : [{"produccion":['SentenciaSi'], "SD" :['SI']}],
    'Sentencia' : [{"produccion":['SentenciaRepetir'], "SD" :['REPETIR']}],
    'Sentencia' : [{"produccion":['SentenciaAsig'], "SD" :['ID']}], 
    'Sentencia' : [{"produccion":['SentenciaLeer'], "SD" :['LEER']}],
    'Sentencia' : [{"produccion":['SentenciaMostrar'], "SD" :['MOSTRAR']}],
    'Sentencia' : [{"produccion":['SetenciaFun'], "SD" :['FUNC']}],
    
    'SentenciaSi' : [{"produccion":['SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2'], "SD" :['SI']}],
    'SentenciaSi2' : [{"produccion":['SINO','ListaSentencia','FIN-SI'], "SD" :['SINO']}],
    'SentenciaSi' : [{"produccion":['FIN-SI'], "SD" :['FIN-SI']}],
    
    'SentenciaRepetir' : [{"produccion":['REPETIR','ListaSentencias','HASTA','Expression'], "SD" :['REPETIR','ListaSentencias','HASTA','Expression']}],
    'SentenciaAsig' : [{"produccion":['ID','EQUAL', 'Expression'], "SD" :['ID']}],
    'SentenciaLeer' : [{"produccion":['LEER', 'ID'], "SD" :['LEER']}],
    'SentenciaMostrar' : [{"produccion":['MOSTRAR', 'Expression'], "SD" :['MOSTRAR']}],
    'SetenciaFun' : [{"produccion":['FUNC', 'Proc', 'FINFUNC'], "SD" :['FUNC']}],
    
    'Proc' : [{"produccion":['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias'], "SD" :['ID']}],
    
    'ListaPar' : [{"produccion":['ID','ListaPar2'], "SD" :['ID']}],
    'ListaPar2' : [{"produccion":['PUNTO-COMA', 'ID', 'ListaPar2'], "SD" :['PUNTO-COMA']}],
    'ListaPar2' : [{"produccion":[], "SD" :['Parentensis Cerrado']}],
    
    'Expression' : [{"produccion":['Expresion2', 'ExpressionPrima'], "SD" :['Parentensis Cerrado','NUM','ID']}],
    
    'ExpressionPrima' : [{"produccion":['OPEREL','Expression2'], "SD" :['OPEREL']}],
    'ExpressionPrima' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    'Expresion2' : [{"produccion":['Termino','Expresion22'], "SD" :['Parentensis Cerrado','NUM','ID']}],
    'Expresion22' : [{"produccion":['OPSUM', 'Termino', 'Expresion22'], "SD" :['OPSUM']}],
    'Expresion22' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    'Termino' : [{"produccion":['Factor' , 'Termino2'], "SD" :['Parentesis Abierto', 'NUM' , 'ID']}],
    
    'Termino2' : [{"produccion":['OPMULT','Termino','Termino2'], "SD" :['OPMULT']}],
    'Termino2' : [{"produccion":[], "SD" :['Parentensis Cerrado', '#' ,'PUNTO-COMA', 'FIN-FUNC' ,'FIN-SI' ,'SINO', 'HASTA', 'ENTONCES']}],
    
    
    'Factor' : [{"produccion":['Parentesis Abierto', 'Expression', 'Parentesis Cerrado'], "SD" :['Parentesis Abierto']}],
    'Factor' : [{"produccion":['NUM'], "SD" :['NUM']}],
    'Factor' : [{"produccion":['ID'], "SD" :['ID']}],
    
    
    } 

###SIMBOLOS DIRECTRICES###
 ### RECORDAR QUE SE COPIAN LOS TOKEN ###

SD(Program->ListaSentencias) = {si,repetir,id,leer,mostrar,func}

SD(ListaSentencia -> Sentencia  ListaSentencia2) = {si,repetir,id,leer,mostrar,func}

SD(ListaSentencia2 -> 'PUNTO-COMA','Sentencias','ListaSentencias2' ) = {PUNTO-COMA}
SD(ListaSentencia2 -> λ )  = {# FIN-FUNC  FIN-SI SINO HASTA}   <-----------------------------------------------------------------------
  
SD(Sentencia -> SentenciaSi) = {SI}
SD(Sentencia -> SentenciaRepertir) = {REPETIR}
SD(Sentencia -> SentenciaAsig) = {ID}
SD(Sentencia -> SentenciaLeer) = {LEER}
SD(Sentencia -> SentenciaMostrar) = {MOSTRAR}
SD(Sentencia -> SentenciaFun) = {FUNC}

SD(SentenciaRepetir -> 'REPETIR','ListaSentencias','HASTA','Expression') = {REPETIR}

SD(SentenciaSi ->'SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2') = {SI}
SD(SentenciaSi2 -> 'SINO','ListaSentencia','FIN-SI') = { SINO}
SD(SentenciaSi2 -> FINSI) = {FIN-SI}

SD(SentenciaAsig -> ) = {ID}
SD(SentenciaLeer -> ) = {LEER}
SD(SentenciaMostrar ->) = {MOSTRAR}
SD(SentenciaFun -> ) = {FUNC}

SD(Proc -> ) = {ID}

SD(ListaPar ->  ) = {ID}
SD(ListaPar2 -> 'PUNTO-COMA', 'ID', 'ListaPar2') = {PUNTO-COMA}
SD(ListaPar2 -> λ)  = { ) }   <----------------------------------------------------------------------

SD(Expresion -> 'Expresion2', 'ExpressionPrima') = {(,NUM,ID}
SD(ExpresionPrima -> 'OPEREL','Expression2') {OPEREL}
SD(ExpresionPrima -> Lamda) ={ ) # PUNTO-COMA FIN-FUNC FIN-SI SINO HASTA ENTONCES }    <---------------------------------------------------------------

SD(Exrepssion2 -> 'Termino','Expresion22') = {(, NUM,ID}
SD(Expression22 -> OPTSUMA Termno Expersion22) ={OPTSuma}
SD(Expression22 -> Lambda) ={ ) # PUNTO-COMA OPEREL FIN-FUNC FIN-SI SINO HASTA ENTONCES }       <-------------------------------------------------------

SD(Termino -> Factor Termino2) = {( , NUM , ID}
SD(Termino2 -> OPTMULT Factor TErmino2) = {OPTMULT}
SD(Termino2 -> lambda) = {) # OPTSUMA PUNTO-COMA OPEREL FIN-FUNC FIN-SI SINO HASTA ENTONCES}   <----------------------------------------------------

SD(Factor -> '(' 'Expresion' ')' )= { ( }
SD(Factor -> NUM)= {NUM}
SD(Factor -> ID) = {ID}
"""


for clave in SD['Program']:  
    if clave== datos_locales['index']: 
        for cuerpo_produccion in SD['Program'.get(clave)]: 
            Procesar(cuerpo_produccion,clave)




SD:{ 'Program':{"SI":['ListaSentencias'],
                "REPETIR":['ListaSentencias'],
                "ID":['ListaSentencias'],
                "LEER":['ListaSentencias'],
                "MOSTRAR":['ListaSentencias'],
                "FUNC":['ListaSentencias']},

    'ListaSentencias':{"SI":['Sentencia' ,'ListaSentencia2'],
                "REPETIR":['Sentencia', 'ListaSentencia2'],
                "ID":['Sentencia', 'ListaSentencia2'],
                "LEER":['Sentencia', 'ListaSentencia2'],
                "MOSTRAR":['Sentencia' ,'ListaSentencia2'],
                "FUNC":['Sentencia' ,'ListaSentencia2']},

    'ListaSentencia2':{"PUNTO-COMA":['PUNTO-COMA','Sentencia','ListaSentencia2']},
                       
    'ListaSentencia2':{"FIN-FUNC":[' '],
                       "FIN-SI":[' '],
                       "SINO":[' '],
                       "HASTA":[' ']},

    'Sentencia':{"SI":['SentenciaSi'],
                 "REPETIR":['SentenciaRepetir'],
                 "ID":['SentenciaAsig'],
                 "LEER":['SentenciaLeer'],
                "MOSTRAR":['SentenciaMostrar'],
                "FUNC":['SentenciaFun']},

    'SentenciaRepetir':{"REPETIR":['REPETIR','ListaSentencias','HASTA','Expression']},

    'SentenciaSi':{"SI":['SI','Expression','ENTONCES','ListaSentencias','SentenciaSi2']},

    'SentenciaSi2':{"SINO":['SINO','ListaSentencia','FIN-SI'],
                    "FIN-SI":['FIN-SI']},

    'SentenciaAsig':{"ID":['ID', 'EQUAL' ,'Expression']},

    'SentenciaLeer':{"LEER":['LEER', 'ID']},

    'SentenciaMostrar':{"MOSTRAR":['MOSTRAR', 'Expression']},

    'SentenciaFun':{"FUNC": ['FUNC', 'Proc', 'FINFUNC'] },

    'Proc':{"ID": ['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias']},

    'ListaPar':{"ID":['ID','ListaPar2'],
                "PUNTO-COMA":['PUNTO-COMA', 'ID', 'ListaPar2'],
                "Parentesis Cerrado":[" "]},

    'Expression':{"Parentesis Abierto":['Expresion2', 'ExpressionPrima'],
                 "NUM":['Expresion2', 'ExpressionPrima'],
                 "ID":['Expresion2', 'ExpressionPrima'],
                 },

    'ExpresionPrima':{"OPEREL":['OPEREL','Expression2'],
                      "Parentesis Cerrado":[],
                      "#":[ ],
                      "PUNTO-COMA":[ ],
                      "FIN-FUNC":[ ],
                      "FIN-SI":[ ],
                      "SINO": [],
                      "HASTA":[ ],
                      "ENTONCES": [ ],
                      },

    'Expresion2':{"Parentesis Abierto":['Termino','Expresion22'],
                  "NUM":['Termino','Expresion2'],
                  "ID": ['Termino','Expresion2']}, 

    'Expresion22':{"OPSUM":[ 'OPSUMA','Termino' ,'Expresion22'],
                    "Parentesis Cerrado": [],
                    "#":[ ], 
                    "PUNTO-COMA": [ ],
                    "OPEREL":[],
                    "FIN-FUNC": [ ],
                    "FIN-SI": [ ],
                    "SINO": [ ],
                    "HASTA": [ ],
                    "ENTONCES": [ ]}, 

    'Termino': { "Parentesis Abierto": ['Factor', 'Termino2' ], 
                "NUM":  ['Factor', 'Termino2' ], 
                "ID":  ['Factor', 'Termino2' ] }, 

    'Termino2': {"OPTMULT" : ['OPTMULT', 'Factor', 'Termino2']},
    'Termino2':{"#":[],
                "OPTSUMA" : [],
                "PUNTO-COMA": [],
                "OPEREL":[],
                "FIN-FUNC":[],
                "FIN-SI": [],
                "SINO" : [],
                "HASTA" : [],
                "ENTONCES":[]},
    
    'Factor':{"Parentesis Abierto" : ['Parentesis Abierto',"Expression","Parentesis Cerrado"]},
    'Factor':{"NUM" : ['NUM']},
    'Factor':{"ID": ['ID']}
}
                
