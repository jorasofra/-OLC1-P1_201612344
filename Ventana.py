import sys, os
from AnalizadorCSS import AnalizadorCss
from AnalizadorHTML import AnalizadorHTML
from AnalizadorJS import AnalizadorJS
from AnalizadorAritmetico import AnalizadorAritmetico
from AnalizadorSintactico import AnalizadorSintactico
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QInputDialog, QLineEdit, QFileDialog

class Ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventana.ui", self)
        self.setWindowTitle('ML Web Editor')
        self.mAbrir.triggered.connect(self.abrirArchivo)
        self.mAnalizar.triggered.connect(self.analizar)
        self.__fileName = ""
        self.__extesion = ""
        self.__js = AnalizadorJS()
        self.__css = AnalizadorCss()
        self.__ht = AnalizadorHTML()
        self.__arit = AnalizadorAritmetico()

    def abrirArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.__fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "C:/Users/solis/OneDrive/Escritorio/Rafael/Compiladores 1/Laboratorio/Entradas", 
            "JavaScript Files (*.js);; CSS Files (*.css);; HTML Files (*.html);; Analizador Sintactico (*.rmt)", options = options)
        if self.__fileName:
            file = open(self.__fileName, "r")
            texto = file.read()
            self.texto.clear()
            self.texto.appendPlainText(texto)
            self.__extesion = os.path.splitext(self.__fileName)[1]
            file.close()

    def analizar(self):
        if self.__extesion == ".js":
            self.__js.analisis(self.texto.toPlainText())
            self.generarReporteErrores()
        elif self.__extesion == ".css":
            self.__css.analisis(self.texto.toPlainText())
            self.generarReporteErrores()
            bita = self.__css.getBitacora()
            self.consola.clear()
            for b in bita:
                self.consola.appendPlainText(b)
        elif self.__extesion == ".html":
            self.__ht.analisis(self.texto.toPlainText())
            self.generarReporteErrores()
        elif self.__extesion == ".rmt":
            self.__arit.analisis(self.texto.toPlainText())
            print(len(self.__arit.getTokens()))
            sintac = AnalizadorSintactico(self.__arit.getTokens())
            sintac.analizar()
            self.consola.clear()
            self.consola.appendPlainText(sintac.validacion())


    def generarReporteErrores(self):
        archivo = os.path.split(self.__fileName)[1]
        nombreArchivo = os.path.splitext(archivo)[0] + "_errores.html"
        errores = open(nombreArchivo, "w")

        contador = 1

        errores.write("<!DOCTYPE html>\n")
        errores.write("<html>\n")
        errores.write("<h1>Reporte de Errores<h1>\n")

        errores.write("<table class=\"egt\" border=\"1\">\n")
        errores.write("<tr>\n")
        errores.write("<th>No.</th>\n")
        errores.write("<th>Linea</th>\n")
        errores.write("<th>Columna</th>\n")
        errores.write("<th>Descripcion</th>\n")
        errores.write("<th>Simbolo</th>\n")
        errores.write("<tr>\n")

        if self.__extesion == ".js":
            lista = self.__js.getErrores()
            for l in lista:
                errores.write("<tr>\n")
                errores.write("<td>" + str(contador) + "</td>")
                errores.write("<td>" + str(l.getFila()) + "</td>")
                errores.write("<td>" + str(l.getColumna()) + "</td>")
                errores.write("<td>" + l.getDescripcion() + "</td>")
                errores.write("<td>" + l.getLexema() + "</td>")
                errores.write("</tr>\n")
                contador += 1
        elif self.__extesion == ".css":
            lista = self.__css.getErrores()
            for l in lista:
                errores.write("<tr>\n")
                errores.write("<td>" + str(contador) + "</td>")
                errores.write("<td>" + str(l.getFila()) + "</td>")
                errores.write("<td>" + str(l.getColumna()) + "</td>")
                errores.write("<td>" + l.getDescripcion() + "</td>")
                errores.write("<td>" + l.getLexema() + "</td>")
                errores.write("</tr>\n")
                contador += 1
        elif self.__extesion == ".html":
            lista = self.__ht.getErrores()
            for l in lista:
                errores.write("<tr>\n")
                errores.write("<td>" + str(contador) + "</td>")
                errores.write("<td>" + str(l.getFila()) + "</td>")
                errores.write("<td>" + str(l.getColumna()) + "</td>")
                errores.write("<td>" + l.getDescripcion() + "</td>")
                errores.write("<td>" + l.getLexema() + "</td>")
                errores.write("</tr>\n")
                contador += 1
        errores.write("</table>\n")
        errores.write("</html>")
        errores.close()
