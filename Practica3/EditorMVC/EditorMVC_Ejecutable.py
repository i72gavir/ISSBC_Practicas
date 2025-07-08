# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:19:49 2025

@author: Rafa
"""


import sys
from PyQt5.QtWidgets import QApplication
from EditorMVC_Vista import Vista

app=QApplication([])
vista=Vista()
vista.show()
    
sys.exit(app.exec_())
