from TipoToken import TipoToken as t

class AnalizadorSintactico:
    
    def __init__(self, listaTokens):
        self.__preanalisis = None
        self.__listaTokens = listaTokens
        self.__contador = 0
        self.__bandera = False
        self.__listaErrores = []
    
    def analizar(self):
        self.__contador = 0
        self.__preanalisis = self.__listaTokens[self.__contador]
        self.__E()

    def __E(self):
        self.__T()
        self.__EP()

    def __EP(self):
        if self.__preanalisis.getTipo() == t.SIGNO_MAS.value:
            self.__parea(t.SIGNO_MAS.value)
            self.__T()
            self.__EP()
        elif self.__preanalisis.getTipo() == t.GUION.value:
            self.__parea(t.GUION.value)
            self.__T()
            self.__EP()

    def __T(self):
        self.__F()
        self.__TP()

    def __TP(self):
        if self.__preanalisis.getTipo() == t.ASTERISCO.value:
            self.__parea(t.ASTERISCO.value)
            self.__T()
            self.__EP()
        elif self.__preanalisis.getTipo() == t.DIAGONAL.value:
            self.__parea(t.DIAGONAL.value)
            self.__T()
            self.__EP()

    def __F(self):
        if self.__preanalisis.getTipo() == t.PARENTESIS_ABRE.value:
            self.__parea(t.PARENTESIS_ABRE.value)
            self.__E()
            self.__parea(t.PARENTESIS_CIERRA.value)
        elif self.__preanalisis.getTipo() == t.ENTERO.value:
            self.__parea(t.ENTERO.value)
        elif self.__preanalisis.getTipo() == t.ID.value:
            self.__parea(t.ID.value)
        else:
            self.__listaErrores.append("Error")

    def __parea(self, terminal):
        if self.__preanalisis.getTipo() == terminal:
            self.__contador += 1
            if (self.__contador) < (len(self.__listaTokens)):
                self.__preanalisis = self.__listaTokens[self.__contador]
                self.__bandera = True
        else:
            self.__listaErrores.append("Error")

    def validacion(self):
        if len(self.__listaErrores) > 0:
            print("No valido")
        else:
            print("Valido")
