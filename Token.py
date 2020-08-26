import TipoToken

class Token:

    __toString={
        1:"Booleano", 
        2:"Cadena",
        3:"Char",
        4:"Coma",
        5:"Comentario",
        6:"Conjuncion",
        7:"Distinto",
        8:"Disyuncion",
        9:"Diagonal",
        10:"Entero",
        11:"Estructura Lambda",
        12:"ID",
        13:"Igual que",
        14:"Llave Abre",
        15:"Llave Cierra",
        16:"Mayor igual",
        17:"Mayor",
        18:"Menor Igual",
        19:"Menor",
        20:"Asterisco",
        21:"Negacion",
        22:"Palabra Reservada",
        23:"Parentesis Abre",
        24:"Parentesis Cierra",
        25:"Punto",
        26:"Punto y Coma",
        27:"Guion",
        28:"Asignacion",
        29:"Signo Igual",
        30:"Signo Mas",
        31:"Numeral",
        32:"Color",
        33:"Decimal",
        34:"Doble dos puntos",
        35:"Unidad de Medida",
        36:"Cierre Etiqueta",
        37:"Etiqueta Apertura",
        38:"Etiqueta Apertura Cierre",
        39:"Cierre Etiqueta Apertura"
        }

    def __init__(self, fila, columna, lexema, tipo_token):
        self.__fila = fila
        self.__columna = columna
        self.__lexema = lexema
        self.__tipo_token = tipo_token
    
    def getTipo(self):
        return self.__tipo_token

    def getFila(self):
        return self.__fila

    def getColumna(self):
        return self.__columna

    def getLexema(self):
        return self.__lexema

    def setTipo(self, tipo):
        self.__tipo_token = tipo

    def setFila(self, fila):
        self.__fila = fila

    def setColumna(self, col):
        self.__columna = col

    def setLexema(self, lex):
        self.__lexema = lex
        
    def getTipoString(self):
        return self.__toString[self.__tipo_token]