# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

import rdflib
from rdflib.namespace import FOAF
from rdflib.plugins import sparql

q = sparql.prepareQuery(
    "SELECT ?s WHERE { ?person foaf:knows ?s .}",
    initNs = { "foaf": FOAF }
)

g = rdflib.Graph()
g.parse("foaf.rdf")

tim = rdflib.URIRef("http://www.w3.org/People/Berners-Lee/card#i")

for row in g.query(q, initBindings={'person': tim}):
    print(row)