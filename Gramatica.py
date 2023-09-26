VN = ['Program', 'ListaSentencias', 'Sentencia', 'SentenciaSi',
                    'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                    'SentenciaFun','Proc', 'ListaPar', 'Expression', 'Expresion2', 'Factor',
                    'Termino','ListaSentencias2','ListaPar2','Expresion2','Termino2'
                ]


VT = ["SI","FINSI","OPSUM","OPMULT","EQUAL","LEER","MOSTRAR","REPETIR",
              "HASTA","ENTONCES","MIENTRAS","FUNC","FINFUNC","OPEREL","PUNTO-COMA",
              "Parentensis Cerrado","Parentensis Abierto","NUM","ID"]

dicSD = { 'Program':{"SI":['ListaSentencias'],
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
                       
    'ListaSentencia2':{"FIN-FUNC":[],
                       "FIN-SI":[],
                       "SINO":[],
                       "HASTA":[]},

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
                "Parentesis Cerrado":[]},

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
                
