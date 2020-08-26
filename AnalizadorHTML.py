import ErrorLexico
import TipoToken
import Token

class AnalizadorHTML:

    def __init__(self):
        self.__lexema = ""
        self.__fila = 1
        self.__columna = 1
        self.__puntero = 0
        self.__estado = 0
        self.__letra = ''
        self.__listaTokens = []
        self.__listaErrores= []

    def analisis(self, texto):
        texto = texto + " $"

        while texto[self.__puntero] != "$":
            self.__letra = texto[self.__puntero]
            self.__case(self.__estado)
            self.__puntero = self.__puntero + 1
            self.__columna = self.__columna + 1

    def cero(self):
        if self.__letra == "\"":
            self.__estado = 1
            self.__lexema = self.__lexema + self.__letra
        elif self.__letra == "/":
            self.__estado = 3
            self.__lexema = self.__lexema + self.__letra
        elif self.__letra == ">":
            self.__estado = 5
            self.__lexema = self.__lexema + self.__letra
        elif self.__letra == "<":
            self.__estado = 6
            self.__lexema = self.__lexema + self.__letra
        elif self.__letra.isalpha():
            self.__estado = 8
            self.__lexema = self.__lexema + self.__letra
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def uno(self):
        if self.__letra == "\"":
            self.__estado = 2
            self.__lexema = self.__lexema + self.__letra
        else:
            self.__estado = 1
            self.__lexema = self.__lexema + self.__letra

    def dos(self):
        self.__agregarToken(TipoToken.TipoToken.CADENA.value)
        self.__puntero = self.__puntero - 1
        self.__columna = self.__columna - 1
        self.__estado = 0
        self.__lexema = ""

    def tres(self):
        if self.__letra == ">":
            self.__estado = 4
            self.__lexema = self.__lexema + self.__letra
        else:
            self.__agregarError()

    def cuatro(self):
        self.__agregarToken(TipoToken.TipoToken.CIERRE_ETIQUETA_UNILINEA.value)
        self.__puntero = self.__puntero - 1
        self.__columna = self.__columna - 1
        self.__estado = 0
        self.__lexema = ""

    def cinco(self):
        self.__agregarToken(TipoToken.TipoToken.CIERRE_ETIQUETA_APERTURA.value)
        self.__puntero = self.__puntero - 1
        self.__columna = self.__columna - 1
        self.__estado = 0
        self.__lexema = ""
    
    def seis(self):
        if self.__letra == "/":
            self.__estado = 7
            self.__lexema = self.__lexema + self.__letra
        else:
            self.__agregarToken(TipoToken.TipoToken.ETIQUETA_APERTURA.value)
            self.__puntero = self.__puntero - 1
            self.__columna = self.__columna - 1
            self.__estado = 0
            self.__lexema = ""

    def siete(self):
        
        self.__agregarToken(TipoToken.TipoToken.APERTURA_ETIQUETA_CIERRE.value)
        self.__puntero = self.__puntero - 1
        self.__columna = self.__columna - 1
        self.__estado = 0
        self.__lexema = ""

    def ocho(self):
        if self.__letra.isalpha() or self.__letra.isdigit():
            self.__estado = 7
            self.__lexema = self.__lexema + self.__letra
        else:
            self.__agregarToken(TipoToken.TipoToken.PALABRA_RESERVADA.value)
            self.__puntero = self.__puntero - 1
            self.__columna = self.__columna - 1
            self.__estado = 0
            self.__lexema = ""

    def __esVacio(self, caracter):
        if caracter == ' ':
            return True
        elif caracter == '\n':
            self.__fila = self.__fila + 1
            self.__columna = 1
            return True
        elif caracter == '\t':
            return True
        return False

    def __agregarToken(self, tipo):
        nuevo = Token.Token(self.__fila, self.__columna, self.__lexema, tipo)
        self.__listaTokens.append(nuevo)

    def __agregarError(self):
        descr = "No pertenece al lenguaje"
        error = ErrorLexico.ErrorLexico(self.__fila, self.__columna, self.__lexema, descr)
        self.__listaErrores.append(error)

    def getTokens(self):
        return self.__listaTokens

    def getErrores(self):
        return self.__listaErrores

    def __case(self, est):
        estados = {
            0:self.cero,
            1:self.uno,
            2:self.dos,
            3:self.tres,
            4:self.cuatro,
            5:self.cinco,
            6:self.seis,
            7:self.siete,
            8:self.ocho
        }
        func = estados.get(est)
        func()

    def imprimirLista(self):
        for tok in self.__listaTokens:
            print(tok.getLexema())
            print(tok.getTipoString())