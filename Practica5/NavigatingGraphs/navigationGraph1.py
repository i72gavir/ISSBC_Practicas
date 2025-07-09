# -*- coding: utf-8 -*-
"""

@author: Rafa
"""

from rdflib import URIRef, Graph
from rdflib.namespace import RDF, FOAF

graph = Graph()

bob = URIRef("http://example.org/people/bob")
graph.add((bob, RDF.type, FOAF.Person))

#Verificar si Bob es una persona en el grafo
if (bob, RDF.type, FOAF.Person) in graph:
    print("This graph knows that Bob is a person!")