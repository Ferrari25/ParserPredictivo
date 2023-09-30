VN = ['Program', 
      'ListaSentencias',
      'ListaSentencias_prima',
      'Sentencia',
      'SentenciaSi',
      'SentenciaSi_prima',
      'SentenciaRepetir',
      'SentenciaAsig',
      'SentenciaLeer',
      'SentenciaMostrar',
      'SentenciaFun'
      'Proc',
      'ListaPar',
      'ListaPar_prima',
      'Expresion',
      'Expresion_prima',
      'Expresion2',
      'Expresion2_prima',
      'Termino',
      'Termino_prima',
      'Factor',
     ]


VT = ["Parentensis Cerrado",
      "Parentensis Abierto",
      "PUNTO-COMA",
      "ENTONCES",
      "EQUAL",
      "FINFUNC",
      "FINSI",
      "FUNC",
      "HASTA",
      "LEER",
      "MOSTRAR",
      "REPETIR",
      "SI",
      "SINO"
      "OPREL",
      "OPMULT",
      "OPSUMA",
      "EQUAL",
      "ENTONCES",
      "NUM",
      "ID",
      "#",]

P = {
    "Program": {
        "SI":      ["ListaSentencias"],
        "REPETIR": ["ListaSentencias"],
        "ID":      ["ListaSentencias"],
        "LEER":    ["ListaSentencias"],
        "MOSTRAR": ["ListaSentencias"],
        "FUNC":    ["ListaSentencias"],

    },

    "ListaSentencias": {
        "SI":      ["Sentencia", "ListaSentencias_prima"],
        "REPETIR": ["Sentencia", "ListaSentencias_prima"],
        "ID":      ["Sentencia", "ListaSentencias_prima"],
        "LEER":    ["Sentencia", "ListaSentencias_prima"],
        "MOSTRAR": ["Sentencia", "ListaSentencias_prima"],
        "FUNC":    ["Sentencia", "ListaSentencias_prima"],
    },

    "ListaSentencias_prima": {
        "PUNTO-COMA": ["PUNTO-COMA", "Sentencia", "ListaSentencias_prima"],
        "#":          [],
        "FINFUNC":    [],
        "FINSI":      [],
        "SINO":       [],
        "HASTA":      [],
    },

    "Sentencia": {
        "SI":      ["SentenciaSi"],
        "REPETIR": ["SentenciaRepetir"],
        "ID":      ["SentenciaAsig"],
        "LEER":    ["SentenciaLeer"],
        "MOSTRAR": ["SentenciaMostrar"],
        "FUNC":    ["SentenciaFun"],
    },

    "SentenciaRepetir": {
        "REPETIR":  ["REPETIR", "ListaSentencias", "HASTA", "Expresion"],
    },

    "SentenciaSi": {
        "SI":  ["SI", "Expresion", "ENTONCES", "ListaSentencias","SentenciaSi_prima"],
    },

    "SentenciaSi_prima": {
        "SINO":  ["SINO", "ListaSentencias", "FINSI"],
        "FINSI": ["FINSI"],
    },

    "SentenciaAsig": {
        "ID": ["ID", "EQUAL", "Expresion"],
    },

    "SentenciaLeer": {
        "LEER": ["LEER", "ID"],
    },

    "SentenciaMostrar": {
        "MOSTRAR": ["MOSTRAR", "Expresion"],
    },

    "SentenciaFun": {"FUNC": ["FUNC", "Proc", "FINFUNC"],},

    "Proc": {
        "ID": ["ID", "Parentesis Abierto", "ListaPar", "Parentesis Cerrado", "ListaSentencias"],
    },

    "ListaPar": {"ID": ["ID", "ListaPar_prima"],},

    "ListaPar_prima": {
        "PUNTO-COMA":           ["PUNTO-COMA", "ID", "ListaPar_prima"],
        "Parentesis Cerrado":   [],},

    "Expresion": {
        "Parentesis Abierto": ["Expresion2", "Expresion_prima"],
        "NUM":                ["Expresion2", "Expresion_prima"],
        "ID":                 ["Expresion2", "Expresion_prima"],
    },

    "Expresion_prima": {
        "OPREL":                ["OPREL", "Expresion2"],
        "Parentesis Cerrado":   [],
        "#":                    [],
        "PUNTO-COMA":           [],
        "FINFUNC":              [],
        "FINSI":                [],
        "SINO":                 [],
        "HASTA":                [],
        "ENTONCES":             [],
    },

    "Expresion2": {
        "Parentesis Abierto": ["Termino", "Expresion2_prima"],
        "NUM":                ["Termino", "Expresion2_prima"],
        "ID":                 ["Termino", "Expresion2_prima"],
    },

    "Expresion2_prima": {
        "OPSUMA":               ["OPSUMA", "Termino", "Expresion2_prima"],
        "OPREL":                [],
        "Parentesis Cerrado":   [],
        "#":                    [],
        "PUNTO-COMA":           [],
        "FINFUNC":              [],
        "FINSI":                [],
        "SINO":                 [],
        "HASTA":                [],
        "ENTONCES":             [],
    },

    "Termino": {
        "Parentesis Abierto": ["Factor", "Termino_prima"],
        "NUM":                ["Factor", "Termino_prima"],
        "ID":                 ["Factor", "Termino_prima"],
    },

    "Termino_prima": {
        "OPMULT":              ["OPMULT", "Factor", "Termino_prima"],
        "OPSUMA":              [],
        "OPREL":               [],
        "Parentesis Cerrado":  [],
        "#":                   [],
        "PUNTO-COMA":          [],
        "FINFUNC":             [],
        "FINSI":               [],
        "SINO":                [],
        "HASTA":               [],
        "ENTONCES":            [],
    },

    "Factor": {
        "Parentesis Abierto": ["Parentesis Abierto", "Expresion", "Parentesis Cerrado"],
        "NUM":                ["NUM"],
        "ID":                 ["ID"]
    }
}