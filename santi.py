# TOKENS_POSIBLES = [("SI", automata_si),
#                    ("FINSI", automata_finsi),
#                    ("OPSUMA", automata_opsuma),
#                    ("OPMULT", automata_opmult),
#                    ("EQUAL", automata_equal),
#                    ("LEER", automata_leer),
#                    ("MOSTRAR", automata_mostrar),
#                    ("REPETIR", automata_repetir),
#                    ("HASTA", automata_hasta),
#                    ("ENTONCES", automata_entonces),
#                    ("MIENTRAS", automata_mientras),
#                    ("FUNC", automata_func),
#                    ("FINFUNC", automata_finfunc),
#                    ("OPREL", automata_oprel),
#                    ("PUNTO-COMA",automataPuntoComa),
#                    ("Parentesis Cerrado",automataParenClose),
#                    ("Parentesis Abierto",automataParenOpen),
#                    ("NUM",automata_num),
#                    ("ID", automata_id)]


VT = ["Parentesis Cerrado",
      "Parentesis Abierto",
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
      "NUM",
      "ID",
      "#",]

VN = ["Program", "ListaSentencias", "ListaSentencias_p", "Sentencia", "SentenciaSi", "SentenciaSi_p", "SentenciaRepetir", "SentenciaAsig", "SentenciaLeer",
      "SentenciaMostrar", "SentenciaFun", "Proc", "ListaPar", "ListaPar_p", "Expresion", "Expresion_p", "Expresion2", "Expresion2_p", "Termino", "Termino_p", "Factor", ]



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
        "SI":      ["Sentencia", "ListaSentencias_p"],
        "REPETIR": ["Sentencia", "ListaSentencias_p"],
        "ID":      ["Sentencia", "ListaSentencias_p"],
        "LEER":    ["Sentencia", "ListaSentencias_p"],
        "MOSTRAR": ["Sentencia", "ListaSentencias_p"],
        "FUNC":    ["Sentencia", "ListaSentencias_p"],
    },

    "ListaSentencias_p": {
        "PUNTO-COMA": ["PUNTO-COMA", "Sentencia", "ListaSentencias_p"],
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
        "SI":  ["SI", "Expresion", "ENTONCES", "ListaSentencias","SentenciaSi_p"],
    },

    "SentenciaSi_p": {
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

    "ListaPar": {"ID": ["ID", "ListaPar_p"],},

    "ListaPar_p": {
        "PUNTO-COMA": ["PUNTO-COMA", "ID", "ListaPar_p"],
        "Parentesis Cerrado":   [],},

    "Expresion": {
        "Parentesis Abierto": ["Expresion2", "Expresion_p"],
        "NUM":      ["Expresion2", "Expresion_p"],
        "ID":       ["Expresion2", "Expresion_p"],
    },

    "Expresion_p": {
        "OPREL":      ["OPREL", "Expresion2"],
        "Parentesis Cerrado":   [],
        "#":          [],
        "PUNTO-COMA": [],
        "FINFUNC":    [],
        "FINSI":      [],
        "SINO":       [],
        "HASTA":      [],
        "ENTONCES":   [],
    },

    "Expresion2": {
        "Parentesis Abierto": ["Termino", "Expresion2_p"],
        "NUM":      ["Termino", "Expresion2_p"],
        "ID":       ["Termino", "Expresion2_p"],
    },

    "Expresion2_p": {
        "OPSUMA":     ["OPSUMA", "Termino", "Expresion2_p"],
        "OPREL":      [],
        "Parentesis Cerrado":   [],
        "#":          [],
        "PUNTO-COMA": [],
        "FINFUNC":    [],
        "FINSI":      [],
        "SINO":       [],
        "HASTA":      [],
        "ENTONCES":   [],
    },

    "Termino": {
        "Parentesis Abierto": ["Factor", "Termino_p"],
        "NUM":      ["Factor", "Termino_p"],
        "ID":       ["Factor", "Termino_p"],
    },

    "Termino_p": {
        "OPMULT":    ["OPMULT", "Factor", "Termino_p"],
        "OPSUMA":    [],
        "OPREL":     [],
        "Parentesis Cerrado":  [],
        "#":         [],
        "PUNTO-COMA":[],
        "FINFUNC":   [],
        "FINSI":     [],
        "SINO":      [],
        "HASTA":     [],
        "ENTONCES":  [],
    },

    "Factor": {
        "Parentesis Abierto": ["Parentesis Abierto", "Expresion", "Parentesis Cerrado"],
        "NUM":      ["NUM"],
        "ID":       ["ID"]
    }
}