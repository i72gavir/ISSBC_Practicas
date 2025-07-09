# -*- coding: utf-8 -*-
"""

@author: Rafa
"""

from rdflib import URIRef, Graph
from rdflib.namespace import RDF, FOAF

g = Graph()

bob = URIRef("http://example.org/people/bob")
alice = URIRef("http://example.org/people/alice")
carol = URIRef("http://example.org/people/carol")

# Agregar tripletas
g.add((bob, RDF.type, FOAF.Person))
g.add((alice, RDF.type, FOAF.Person))
g.add((carol, RDF.type, FOAF.Person))
   
    
g.parse("some_foaf.ttl")
# find all subjects (s) of type (rdf:type) person (foaf:Person)
for s, p, o in g.triples((None, RDF.type, FOAF.Person)):
    print(f"{s} is a person")

# find all subjects of any type
for s, p, o in g.triples((None,  RDF.type, None)):
    print(f"{s} is a {o}")

# create a graph
bobgraph = Graph()
# add all triples with subject 'bob'
bobgraph += g.triples((bob, None, None))

for person in g.subjects(RDF.type, FOAF.Person):
    print("{} is a person".format(person))