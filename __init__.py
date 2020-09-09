import Token
import TipoToken
import AnalizadorHTML
from Ventana import Ventana
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())