# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:24:30 2025

@author: Rafa
"""


from EditorMVC_Modelo import Modelo

class Controlador:
    
    def __init__(self):
        self.modelo = Modelo()

    def crear_archivo(self, ruta):
        return self.modelo.crear_archivo(ruta)

    def guardar_archivo(self, contenido, ruta):
        return self.modelo.guardar_archivo(contenido, ruta)

    def abrir_archivo(self, ruta):
        return self.modelo.abrir_archivo(ruta)
    