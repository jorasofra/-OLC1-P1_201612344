from ErrorLexico import ErrorLexico
from TipoToken import TipoToken
from Token import Token

class AnalizadorAritmetico:
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
        self.__listaTokens.clear()
        self.__listaErrores.clear()
        self.__puntero = 0
        texto = texto + " $"
        while texto[self.__puntero] != "$":
            self.__letra = texto[self.__puntero]
            self.__case(self.__estado)
            self.__puntero = self.__puntero + 1
            self.__columna = self.__columna + 1

    def cero(self):
        if self.__letra == "(":
            self.__estado = 1
            self.__lexema += self.__letra
        elif self.__letra == ")":
            self.__estado = 2
            self.__lexema += self.__letra
        elif self.__letra.isdigit():
            self.__estado = 3
            self.__lexema += self.__letra
        elif self.__letra.isalpha():
            self.__estado = 4
            self.__lexema += self.__letra
        elif self.__letra == "+":
            self.__estado = 5
            self.__lexema += self.__letra
        elif self.__letra == "-":
            self.__estado = 6
            self.__lexema += self.__letra
        elif self.__letra == "*":
            self.__estado = 7
            self.__lexema += self.__letra
        elif self.__letra == "/":
            self.__estado = 8
            self.__lexema += self.__letra
        elif self.__esVacio():
            self.__estado = 0
            self.__lexema = ""
        else:
            self.__lexema += self.__letra
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def uno(self):
        self.__agregarToken(TipoToken.PARENTESIS_ABRE.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def dos(self):
        self.__agregarToken(TipoToken.PARENTESIS_CIERRA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def tres(self):
        if self.__letra.isdigit():
            self.__estado = 3
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.ENTERO.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def cuatro(self):
        if self.__letra.isdigit() or self.__letra.isalpha():
            self.__estado = 4
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.ID.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def cinco(self):
        self.__agregarToken(TipoToken.SIGNO_MAS.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def seis(self):
        self.__agregarToken(TipoToken.GUION.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def siete(self):
        self.__agregarToken(TipoToken.ASTERISCO.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def ocho(self):
        self.__agregarToken(TipoToken.DIAGONAL.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def __esVacio(self):
        if self.__letra == ' ':
            return True
        elif self.__letra == '\n':
            self.__fila = self.__fila + 1
            self.__columna = 1
            return True
        elif self.__letra == '\t':
            return True
        return False

    def __agregarToken(self, tipo):
        nuevo = Token(self.__fila, self.__columna, self.__lexema, tipo)
        self.__listaTokens.append(nuevo)

    def __agregarError(self):
        descr = "No pertenece al lenguaje"
        error = ErrorLexico(self.__fila, self.__columna, self.__lexema, descr)
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
            8:self.ocho,
        }
        func = estados.get(est)
        func()
        