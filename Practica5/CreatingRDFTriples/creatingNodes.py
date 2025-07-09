# -*- coding: utf-8 -*-
"""

@author: Rafa
"""

from rdflib import URIRef, BNode, Literal

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated

name = Literal("Bob")  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float