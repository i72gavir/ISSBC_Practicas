# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

import rdflib

g = rdflib.Graph()
qres = g.query(
    """
    SELECT ?s
    WHERE {
      SERVICE <https://dbpedia.org/sparql> {
        ?s a ?o .
      }
    }
    LIMIT 3
    """
)

for row in qres:
    print(row.s)