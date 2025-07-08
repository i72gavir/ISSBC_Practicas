#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on a window and a button.

Author: Rafa
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        #Tamaño y tipo de letra
        QToolTip.setFont(QFont('SansSerif', 10))

        #Crear ayuda
        self.setToolTip('This is a <b>QWidget</b> widget')

        #Crear boton
        btn = QPushButton('Button', self)
        
        #Crear ayuda pra boton
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        #Tamaño boton
        btn.resize(btn.sizeHint())
        
        #Posicion boton
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
