#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we create a simple window in PyQt5.

Author: Rafa 
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    #Creación de instancia
    w = QWidget()
    
    #Modificar tamaño de ventana
    w.resize(250, 150)
    
    #Posicion que ocupara la ventana
    w.move(300, 300)
    
    #Nombre de la ventana
    w.setWindowTitle('Simple')
    
    #Mostrar lo anterior
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
