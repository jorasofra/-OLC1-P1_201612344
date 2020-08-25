class ErrorLexico:
    def __init__(self, fila, columna, lexema, descripcion):
        self.__fila = fila
        self.__columna = columna
        self.__lexema = lexema
        self.__descripcion = descripcion

    def setFila(self, fila):
        self.__fila = fila

    def getFila(self):
        return self.__fila

    def setColumna(self, columna):
        self.__columna = columna

    def getColumna(self):
        return self.__columna

    def setLexema(self, lexema):
        self.__lexema = lexema

    def getLexema(self):
        return self.__lexema

    def setDescripcion(self, desc):
        self.__descripcion = desc

    def getDescripcion(self):
        return self.__descripcion