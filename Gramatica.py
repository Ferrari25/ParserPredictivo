VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expresion', 'Expresion2', 'Factor',
                    'Termino','ListaSentencias2','ListaPar2','Expresion22','Termino2'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID","#"]

P = { 'Program':{"SI":['ListaSentencias'],
                "REPETIR":['ListaSentencias'],
                "ID":['ListaSentencias'],
                "LEER":['ListaSentencias'],
                "MOSTRAR":['ListaSentencias'],
                "FUNC":['ListaSentencias']},

    'ListaSentencias':{"SI":['Sentencia' ,'ListaSentencias2'],
                "REPETIR":['Sentencia', 'ListaSentencias2'],
                "ID":['Sentencia', 'ListaSentencias2'],
                "LEER":['Sentencia', 'ListaSentencias2'],
                "MOSTRAR":['Sentencia' ,'ListaSentencias2'],
                "FUNC":['Sentencia' ,'ListaSentencias2']},

    'ListaSentencias2':{"PUNTO-COMA":['PUNTO-COMA','Sentencia','ListaSentencias2'],
                       "FIN-FUNC":[],
                       "FIN-SI":[],
                       "SINO":[],
                       "HASTA":[],
                       "#":[]},

    'Sentencia':{"SI":['SentenciaSi'],
                 "REPETIR":['SentenciaRepetir'],
                 "ID":['SentenciaAsig'],
                 "LEER":['SentenciaLeer'],
                "MOSTRAR":['SentenciaMostrar'],
                "FUNC":['SentenciaFun']},

    'SentenciaRepetir':{"REPETIR":['REPETIR','ListaSentencias','HASTA','Expresion']},

    'SentenciaSi':{"SI":['SI','Expresion','ENTONCES','ListaSentencias','SentenciaSi2']},

    'SentenciaSi2':{"SINO":['SINO','ListaSentencias','FIN-SI'],
                    "FIN-SI":['FIN-SI']},

    'SentenciaAsig':{"ID":['ID', 'EQUAL' ,'Expresion']},

    'SentenciaLeer':{"LEER":['LEER', 'ID']},

    'SentenciaMostrar':{"MOSTRAR":['MOSTRAR', 'Expresion']},

    'SentenciaFun':{"FUNC": ['FUNC', 'Proc', 'FINFUNC'] },

    'Proc':{"ID": ['ID', 'Parentensis Abierto' , 'ListaPar' , 'Parentensis Cerrado','ListaSentencias']},

    'ListaPar':{"ID":['ID','ListaPar2']},

    'ListaPar2':{"PUNTO-COMA": ['PUNTO-COMA', 'ID', 'ListaPar2'],
                 "Parentesis Cerrado": []},

    'Expresion':{"Parentesis Abierto":['Expresion2', 'ExpresionPrima'],
                 "NUM":['Expresion2', 'ExpresionPrima'],
                 "ID":['Expresion2', 'ExpresionPrima'],
                 },

    'ExpresionPrima':{"OPEREL":['OPEREL','Expresion2'],
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
                  "NUM":['Termino','Expresion22'],
                  "ID": ['Termino','Expresion22']}, 

    'Expresion22':{"OPSUM":[ 'OPSUM','Termino' ,'Expresion22'],
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

    'Termino2': {"OPMULT" : ['OPMULT', 'Factor', 'Termino2'],
                "#":[],
                "OPSUM" : [],
                "PUNTO-COMA": [],
                "OPEREL":[],
                "FIN-FUNC":[],
                "FIN-SI": [],
                "SINO" : [],
                "HASTA" : [],
                "ENTONCES":[],
                "Parentesis Cerrado":[]},
    
    'Factor':{"Parentesis Abierto" : ['Parentesis Abierto',"Expresion","Parentesis Cerrado"],
              "NUM" : ['NUM'],
              "ID": ['ID']}
}

                

