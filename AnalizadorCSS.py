from ErrorLexico import ErrorLexico
from TipoToken import TipoToken
from Token import Token

class AnalizadorCss:
    def __init__(self):
        self.__lexema = ""
        self.__fila = 1
        self.__columna = 1
        self.__puntero = 0
        self.__estado = 0
        self.__letra = ''
        self.__listaTokens = []
        self.__listaErrores= []
        self.__reservadas = (
            "color",
            "border",
            "text-align",
            "font-weight",
            "padding-left",
            "padding-top",
            "line-height",
            "margin-top",
            "margin-left",
            "display",
            "top",
            "float",
            "min-width",
            "background-color",
            "opacity",
            "font-family",
            "font-size",
            "padding-right",
            "padding",
            "width",
            "margin-right",
            "margin",
            "position",
            "right",
            "clear",
            "max-height",
            "background-image",
            "background",
            "font-style",
            "font",
            "padding-bottom",
            "height",
            "margin-bottom",
            "border-style",
            "bottom",
            "left",
            "max-width",
            "min-height",
            "rgba",
            "url"
        )
        self.__medida = (
            "px",
            "em",
            "vh",
            "vw",
            "in",
            "cm",
            "mm",
            "pt",
            "pc"
        )

    def analisis(self, texto):
        texto = texto + " $"
        while texto[self.__puntero] != "$":
            self.__letra = texto[self.__puntero]
            self.__case(self.__estado)
            self.__puntero = self.__puntero + 1
            self.__columna = self.__columna + 1

    def cero(self):
        if self.__letra == "-":
            self.__estado = 6
            self.__lexema += self.__letra
        elif self.__letra == "/":
            self.__estado = 12
            self.__lexema += self.__letra
        elif self.__letra == "\"":
            self.__estado = 1
            self.__lexema += self.__letra
        elif self.__letra == "#":
            self.__estado = 3
            self.__lexema += self.__letra
        elif self.__letra == "(":
            self.__estado = 5
            self.__lexema += self.__letra
        elif self.__letra == ")":
            self.__estado = 16
            self.__lexema += self.__letra
        elif self.__letra == "*":
            self.__estado = 17
            self.__lexema += self.__letra
        elif self.__letra == ",":
            self.__estado = 18
            self.__lexema += self.__letra
        elif self.__letra == ".":
            self.__estado = 19
            self.__lexema += self.__letra
        elif self.__letra == ":":
            self.__estado = 15
            self.__lexema += self.__letra
        elif self.__letra == ";":
            self.__estado = 20
            self.__lexema += self.__letra
        elif self.__letra == "{":
            self.__estado = 21
            self.__lexema += self.__letra
        elif self.__letra == "}":
            self.__estado = 22
            self.__lexema += self.__letra
        elif self.__letra.isalpha():
            self.__estado = 11
            self.__lexema += self.__letra
        elif self.__letra.isdigit():
            self.__estado = 7
            self.__lexema += self.__letra
        elif self.__esVacio():
            self.__estado = 0
            self.__lexema = ""
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def uno(self):
        if self.__letra == "\"":
            self.__estado = 2
            self.__lexema += self.__letra
        else:
            self.__estado = 1
            self.__lexema += self.__letra

    def dos(self):
        self.__agregarToken(TipoToken.CADENA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def tres(self):
        if self.__letra.isalpha() or self.__letra.isdigit():
            self.__estado = 4
            self.__lexema += self.__letra
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def cuatro(self):
        if self.__letra.isalpha() or self.__letra.isdigit():
            self.__estado = 4
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.COLOR.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def cinco(self):
        self.__agregarToken(TipoToken.PARENTESIS_ABRE.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def seis(self):
        if self.__letra.isalpha():
            self.__estado = 11
            self.__lexema += self.__letra
        elif self.__letra.isdigit():
            self.__estado = 7
            self.__lexema += self.__letra
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def siete(self):
        if self.__letra.isdigit():
            self.__estado = 7
            self.__lexema += self.__letra
        elif self.__letra == ".":
            self.__estado = 9
            self.__lexema += self.__letra
        elif self.__letra == "%":
            self.__estado = 8
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.ENTERO.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def ocho(self):
        self.__agregarToken(TipoToken.ENTERO.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def nueve(self):
        if self.__letra.isdigit():
            self.__estado = 10
            self.__lexema += self.__letra
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def diez(self):
        if self.__letra.isdigit():
            self.__estado = 10
            self.__lexema += self.__letra
        elif self.__letra == "%":
            self.__estado = 23
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.DECIMAL.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def once(self):
        if self.__letra.isdigit() or self.__letra.isalpha() or self.__letra == "-":
            self.__estado = 11
            self.__lexema += self.__letra
        else:
            if self.__lexema in self.__reservadas:
                self.__agregarToken(TipoToken.PALABRA_RESERVADA.value)
            elif self.__lexema in self.__medida:
                self.__agregarToken(TipoToken.UNIDAD_MEDIDA.value)
            else:
                self.__agregarToken(TipoToken.ID.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def doce(self):
        if self.__letra == "*":
            self.__estado = 13
            self.__lexema += self.__letra
        else:
            self.__agregarError()
            self.__estado = 0
            self.__lexema = ""

    def trece(self):
        if self.__letra == "*":
            self.__estado = 14
            self.__lexema += self.__letra
        else:
            self.__estado = 13
            self.__lexema += self.__letra
    
    def catorce(self):
        if self.__letra == "/":
            self.__estado = 24
            self.__lexema += self.__letra
        elif self.__letra == "*":
            self.__estado = 14
            self.__lexema += self.__letra
        else:
            self.__estado = 13
            self.__lexema += self.__letra

    def quince(self):
        if self.__letra == ":":
            self.__estado = 25
            self.__lexema += self.__letra
        else:
            self.__agregarToken(TipoToken.DOS_PUNTOS.value)
            self.__puntero -= 1
            self.__columna -= 1
            self.__estado = 0
            self.__lexema = ""

    def dieciseis(self):
        self.__agregarToken(TipoToken.PARENTESIS_CIERRA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def diecisiete(self):
        self.__agregarToken(TipoToken.ASTERISCO.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def dieciocho(self):
        self.__agregarToken(TipoToken.COMA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def diecinueve(self):
        self.__agregarToken(TipoToken.PUNTO.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veinte(self):
        self.__agregarToken(TipoToken.PUNTO_COMA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veintiuno(self):
        self.__agregarToken(TipoToken.LLAVE_ABRE.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veintidos(self):
        self.__agregarToken(TipoToken.LLAVE_CIERRA.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veintitres(self):
        self.__agregarToken(TipoToken.DECIMAL.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veinticuatro(self):
        self.__agregarToken(TipoToken.COMENTARIO.value)
        self.__puntero -= 1
        self.__columna -= 1
        self.__estado = 0
        self.__lexema = ""

    def veinticinco(self):
        self.__agregarToken(TipoToken.DOBLE_DOS_PUNTOS.value)
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
        print(self.__lexema)
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
            9:self.nueve,
            10:self.diez,
            11:self.once,
            12:self.doce,
            13:self.trece,
            14:self.catorce,
            15:self.quince,
            16:self.dieciseis,
            17:self.diecisiete,
            18:self.dieciocho,
            19:self.diecinueve,
            20:self.veinte,
            21:self.veintiuno,
            22:self.veintidos,
            23:self.veintitres,
            24:self.veinticuatro,
            25:self.veinticinco
        }
        func = estados.get(est)
        func()

    def imprimirLista(self):
        for tok in self.__listaTokens:
            print(tok.getLexema())
            print(tok.getTipoString())