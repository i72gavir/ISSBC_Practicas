# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

from rdflib import Graph, URIRef, Literal
from rdflib.namespace import FOAF, RDF

g = Graph()
g.bind("foaf", FOAF)


# Demo data
bob = URIRef("http://example.org/people/Bob")
alice = URIRef("http://example.org/people/Alice")

# Add Bob's data
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, Literal("Bob")))
g.add((bob, FOAF.age, Literal(38)))
g.add((bob, FOAF.knows, alice))

# Add Alice's data
g.add((alice, RDF.type, FOAF.Person))
g.add((alice, FOAF.name, Literal("Alice")))
g.add((alice, FOAF.age, Literal(28)))

# Use 'value' to get a single value
print(f"Bob's age is: {g.value(bob, FOAF.age)}")

# Use 'set' to change a single value
g.set((bob, FOAF.age, Literal(39)))
print(f"Bob's age after birthday is: {g.value(bob, FOAF.age)}")

# Use 'slice' to get subjects of type FOAF.Person
print("People in the graph:")
for person in g[:RDF.type:FOAF.Person]:
    print(f"Name: {g.value(person, FOAF.name)}, Age: {g.value(person,FOAF.age)}")

# Print who Bob knows
print("Bob knows:")
for friend in g[bob:FOAF.knows:]:
    print(g.value(friend, FOAF.name))