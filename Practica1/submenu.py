#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This program creates a submenu.

Author: Rafa
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #Creamos la barra de menu con la etiqueta file
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        #Creamos un nuevo menu
        impMenu = QMenu('Import', self)
        
        #Añadimos acciones al menu
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
