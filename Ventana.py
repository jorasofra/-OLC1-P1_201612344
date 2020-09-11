import sys, os
from AnalizadorCSS import AnalizadorCss
from AnalizadorHTML import AnalizadorHTML
from AnalizadorJS import AnalizadorJS
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

    def abrirArchivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.__fileName, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "C:/Users/solis/OneDrive/Escritorio/Rafael/Compiladores 1/Laboratorio/Entradas", 
            "JavaScript Files (*.js);; CSS Files (*.css);; HTML Files (*.html)", options = options)
        if self.__fileName:
            file = open(self.__fileName, "r")
            texto = file.read()
            self.texto.clear()
            self.texto.appendPlainText(texto)
            self.__extesion =os.path.splitext(self.__fileName)[1]
            file.close()

    def analizar(self):
        if self.__extesion == ".js":
            self.__js.analisis(self.texto.toPlainText())
            print("Finalizado")
        elif self.__extesion == ".css":
            self.__css.analisis(self.texto.toPlainText())
            print("Finalizado")
        elif self.__extesion == ".html":
            self.__ht.analisis(self.texto.toPlainText())
            print("Finalizado")
