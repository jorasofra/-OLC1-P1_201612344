import Token
import TipoToken
import AnalizadorHTML

analizador = AnalizadorHTML.AnalizadorHTML()
analizador.analisis("\" Hola \"")
print(analizador.imprimirLista())