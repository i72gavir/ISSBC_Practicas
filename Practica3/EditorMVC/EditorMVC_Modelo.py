# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:20:42 2025

@author: Rafa
"""


class Modelo:
    
    def crear_archivo(self, ruta):
        try:
            with open(ruta, 'w') as archivo:
                archivo.write("")
                return True
        except Exception as e:
            print(f"Error al crear archivo: {e}")
            return False
        
        
        def guardar_archivo(self, contenido, ruta):
            try:
                with open(ruta, 'w') as archivo:
                    archivo.write(contenido)
                    return True
            except Exception as e:
                print(f"Error al guardar archivo: {e}")
                return False
            
            
            def abrir_archivo(self, ruta):
                try:
                    with open(ruta, 'r') as archivo:
                        contenido = archivo.read()
                        return contenido
                except Exception as e:
                    print(f"Error al abrir archivo: {e}")
                    return None
            
                