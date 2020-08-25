from enum import Enum

class TipoToken(Enum):
    BOOLENANO = 1
    CADENA = 2
    CHAR = 3
    COMA = 4
    COMENTARIO = 5
    CONJUNCION = 6
    DISTINTO = 7
    DISYUNCION = 8
    DIAGONAL = 9
    ENTERO = 10
    ESTRUCTURA_LAMBDA = 11
    ID = 12
    IGUAL_IGUAL = 13
    LLAVE_ABRE = 14
    LLAVE_CIERRA = 15
    MAYOR_IGUAL = 16
    MAYOR = 17
    MENOR_IGUAL = 18
    MENOR = 19
    ASTERISCO = 20
    NEGACION = 21
    PALABRA_RESERVADA =22
    PARENTESIS_ABRE = 23
    PARENTESIS_CIERRA = 24
    PUNTO = 25
    PUNTO_COMA =26
    GUION = 27
    ASIGNACION = 28
    SIGNO_IGUAL = 29
    SIGNO_MAS = 30
    NUMERAL = 31
    COLOR = 32
    DECIMAL = 33
    DOBLE_DOS_PUNTOS = 34
    UNIDAD_MEDIDA = 35
    CIERRE_ETIQUETA_UNILINEA = 36
    ETIQUETA_APERTURA = 37
    APERTURA_ETIQUETA_CIERRE = 38
    CIERRE_ETIQUETA_APERTURA = 39 