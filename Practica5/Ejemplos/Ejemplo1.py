# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import FOAF, RDF

# Create a Graph
g = Graph()
g.bind("foaf", FOAF)

# Add demo data
bob = URIRef("http://example.org/people/Bob")
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, Literal("Bob")))
g.add((bob, FOAF.age, Literal(38)))

# To get a single value, use 'value'
print(g.value(bob, FOAF.age))
# To change a single of value, use 'set'
g.set((bob, FOAF.age, Literal(39)))
print(g.value(bob, FOAF.age))

# Slicing and printing graph
print("All triples in the graph:")
print(list(g[:]))
print("All objects of bob:")
print(list(g[bob]))
print("All friends of bob (foaf:knows):")
print(list(g[bob: FOAF.knows]))
print("Is bob a person?")
print((bob, RDF.type, FOAF.Person) in g)
print("All subjects related to FOAF.knows:")
print(list(g[:FOAF.knows]))


# Using n3 method
print("N3 representation of bob:")
print(bob.n3())

# Parsing data from string
g2 = Graph().parse(data="<a:> <p:> <p:>.")
print("Triple parsed from string:")
for r in g2.triples((None, None, None)):
    print(r)