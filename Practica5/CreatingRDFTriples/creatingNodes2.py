# -*- coding: utf-8 -*-
"""
@author: Rafa
"""

from rdflib import Namespace

n = Namespace("http://example.org/people/")

n.bob  # == rdflib.term.URIRef("http://example.org/people/bob")
n.eve  # == rdflib.term.URIRef("http://example.org/people/eve")